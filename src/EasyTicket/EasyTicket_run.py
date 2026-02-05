import os
import ast
import sys
import tomllib
import argparse
import threading
from bin import get_ticket_info
class Set_up_backend:
    def __init__(self):
        self.file_dir=os.path.dirname(os.path.abspath(__file__))
        self.file_dir_parents=os.path.dirname(os.path.dirname(
            self.file_dir))
        self.temp_dir=os.path.join(
            self.file_dir, 'temp')
        self.thread_setup_num=0
        self.setup_thread_log_path=os.path.join(
            self.temp_dir, 
            "data_socket_backend_thread_setup_num.log")
        self.sign_in_log_path=os.path.join(
            self.temp_dir, 
            "data_socket_user_sign_in_info.log")
        self.buyer_name_log_path=None
        self.start_station_log_path=None
        self.end_station_log_path=None
        self.start_date_log_path=None
        self.passenger_name=None # 未第参
        self.start_station=None # 未第参
        self.end_station=None # 未第参
        self.start_date=None # 未第参 
        self.toml_path=os.path.join(
            self.file_dir_parents, 
            "pyproject.toml")
        with open(self.toml_path, 'rb') as config_file:
            self.config_data=tomllib.load(config_file)
        self.version_info=self.config_data["project"]["version"]
        parser = argparse.ArgumentParser(
            description="Welcome to use the EasyTicket backend application.")
        parser.add_argument("-v", "--version", 
                            action="version", 
                            version="EasyTicket-Backend version {}".format(self.version_info))
        parser.add_argument("-so", "--sign_out", 
                            action="store_true", 
                            dest='sign_out', 
                            help="sign out and delete the sign in information log file")
        args=parser.parse_args()
        if args.sign_out:
            try:
                os.remove(self.sign_in_log_path)
                print("Successfully signed out.")
                sys.exit(0)
            except:
                print("sign out error!")
                sys.exit(1)
        self.user_name_info=None
        self.user_account_password=None
        self.user_id_card_num=None
        if os.path.exists(self.sign_in_log_path):
            with open(
                self.sign_in_log_path, "r", encoding="utf-8") as sign_in_read:
                self.sign_in_info=ast.literal_eval(sign_in_read.read())
            self.user_name_info=self.sign_in_info[0]
            self.user_account_password=self.sign_in_info[1]
            self.user_id_card_num=self.sign_in_info[2]
        else:
            self.sign_in()
        def get_passenger_name_func():
            self.passenger_name=input(
                "Please choose the passenger name:\t")
            with open(os.path.join(
                self.temp_dir, 
                "data_socket_buyer_name_info_{}.log".format(self.thread_setup_num)), "w", 
                encoding="utf-8") as passenger_name_write:
                passenger_name_write.write(str(self.passenger_name))
        def get_ticket_info_func():
            self.start_station=input(
                "Please choose the start station:\t")
            self.end_station=input(
                "Please choose the end station:\t")
            self.start_date=input(
                "Please choose the start date (YYYY-MM-DD):\t")
            with open(os.path.join(
                self.temp_dir, 
                "data_socket_start_station_info_{}.log".format(self.thread_setup_num)), "w", 
                encoding="utf-8") as start_station_write:
                start_station_write.write(str(self.start_station))
            with open(os.path.join(
                self.temp_dir, 
                "data_socket_end_station_info_{}.log".format(self.thread_setup_num)), "w", 
                encoding="utf-8") as end_station_write:
                end_station_write.write(str(self.end_station))
            with open(os.path.join(
                self.temp_dir, 
                "data_socket_start_date_info_{}.log".format(self.thread_setup_num)), "w", 
                encoding="utf-8") as start_date_write:
                start_date_write.write(str(self.start_date))
        if os.path.exists(self.temp_dir):
            if os.path.exists(self.setup_thread_log_path):
                with open(self.setup_thread_log_path, 
                            "r", encoding="utf-8") as thread_setup_read:
                    self.thread_setup_num_list=ast.literal_eval(
                        thread_setup_read.read())
                    self.thread_setup_num=int(self.thread_setup_num_list[0])
                    self.dealed_thread_num=int(self.thread_setup_num_list[1])
                for thread_index in range(
                    self.dealed_thread_num, self.thread_setup_num+1):
                    if os.path.exists(os.path.join(
                        self.temp_dir, 
                        "data_socket_buyer_name_info_{}.log".format(thread_index))):
                        if (not (os.path.exists(os.path.join(
                                self.temp_dir, 
                                "data_socket_start_station_info_{}.log".format(thread_index)))) or 
                            not (os.path.exists(os.path.join(
                                self.temp_dir, 
                                "data_socket_end_station_info_{}.log".format(thread_index)))) or 
                            not (os.path.exists(os.path.join(
                                self.temp_dir, 
                                "data_socket_start_date_info_{}.log".format(thread_index))))):
                            with open(os.path.join(
                                self.temp_dir, 
                                "data_socket_buyer_name_info_{}.log".format(thread_index)), 
                                "r", encoding="utf-8") as passenger_name_read:
                                self.passenger_name=passenger_name_read.read()
                            get_ticket_info_func()
                        else:
                            with open(os.path.join(
                                self.temp_dir, 
                                "data_socket_buyer_name_info_{}.log".format(thread_index)), 
                                "r", encoding="utf-8") as passenger_name_read:
                                self.passenger_name=passenger_name_read.read()
                            with open(os.path.join(
                                self.temp_dir, 
                                "data_socket_start_station_info_{}.log".format(thread_index)), 
                                "r", encoding="utf-8") as start_station_read:
                                self.start_station=start_station_read.read()
                            with open(os.path.join(
                                self.temp_dir, 
                                "data_socket_end_station_info_{}.log".format(thread_index)), 
                                "r", encoding="utf-8") as end_station_read:
                                self.end_station=end_station_read.read()
                            with open(os.path.join(
                                self.temp_dir, 
                                "data_socket_start_date_info_{}.log".format(thread_index)), 
                                "r", encoding="utf-8") as start_date_read:
                                self.start_date=start_date_read.read()
                        thread_check_ticket_info=(
                            threading.Thread(
                                            target=get_ticket_info.get_ticket_station_info, 
                                            args=(self.start_station, self.end_station, 
                                                    self.start_date, self.thread_setup_num),
                                            name="thread_check_ticket_info", 
                                            daemon=True))
                        print("Starting thread {} to check ticket info...".format(
                            thread_check_ticket_info.name))
                        thread_check_ticket_info.start()
                    else:
                        get_passenger_name_func()
                        get_ticket_info_func()
                        thread_check_ticket_info=(
                            threading.Thread(
                                            target=get_ticket_info.get_ticket_station_info, 
                                            args=(self.start_station, self.end_station, 
                                                    self.start_date, self.thread_setup_num),
                                            name="thread_check_ticket_info", 
                                            daemon=True))
                        print("Starting thread {} to check ticket info...".format(
                            thread_check_ticket_info.name))
                        thread_check_ticket_info.start()
            else:
                pass
        else:
            pass
        while True:
            if os.path.exists(self.sign_in_log_path):
                get_passenger_name_func()
                get_ticket_info_func()
                with open(self.setup_thread_log_path, "w", 
                    encoding="utf-8") as thread_setup_write:
                    thread_setup_write.write(str([self.thread_setup_num, 0]))
                thread_check_ticket_info=(
                    threading.Thread(
                                    target=get_ticket_info.get_ticket_station_info, 
                                    args=(self.start_station, self.end_station, 
                                          self.start_date, self.thread_setup_num),
                                    name="thread_check_ticket_info", 
                                    daemon=True))
                print("Starting thread {} to check ticket info...".format(
                            thread_check_ticket_info.name))
                thread_check_ticket_info.start()
                self.thread_setup_num+=1
            else:
                pass
    def sign_in(self):
        print("login first to continue...")
        self.user_name_info=input(
            "Please enter your 12306 account username/phone number/email:\t")
        self.user_account_password=input(
            "Please enter your 12306 account password:\t")
        self.user_id_card_num=input(
            "Please enter the last 4 digits of your ID card number:\t")
        self.info_is_valid_state=(self.user_name_info==None or 
                                  len(str(self.user_name_info).lstrip())==0 or
                                  self.user_account_password==None or 
                                  len(str(self.user_account_password).lstrip())==0 or
                                  self.user_id_card_num==None or 
                                  len(str(self.user_id_card_num).lstrip())==0 or
                                  len(self.user_account_password)<6 or 
                                  len(self.user_id_card_num)<4 or 
                                  len(self.user_id_card_num)>4)
        if self.info_is_valid_state:
            print("Error: Please enter valid login information.")
            self.sign_in()
        else:
            self.get_result=[
                self.user_name_info, self.user_account_password, self.user_id_card_num]
            if not os.path.exists(self.temp_dir):
                os.makedirs(self.temp_dir)
            with open(self.sign_in_log_path, "w", 
                encoding="utf-8") as datalog_write:
                datalog_write.write(str(self.get_result))
if __name__=="__main__":
    backend_setup = Set_up_backend()
