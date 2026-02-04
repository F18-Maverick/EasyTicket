import os
import sys
import argparse
class Set_up_backend:
    def __init__(self):
        self.temp_dir=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'temp')
        parser = argparse.ArgumentParser(
            description="Welcome to use the EasyTicket backend application.")
        parser.add_argument("-v", "--version", 
                            action="version", 
                            version="EasyTicket-Backend version 1.0.0")
        parser.parse_args()
        self.sign_in()
        self.thread_setup_num=0
        while True:
            if os.path.exists(
                os.path.join(self.temp_dir, "data_socket_user_sign_in_info.log")):
                with open(os.path.join(
                    self.temp_dir, "data_socket_backend_thread_setup_num.log"), "r", 
                    encoding="utf-8") as thread_setup_write:
                    thread_setup_write.write(str(self.thread_setup_num))
                self.passenger_name=input()
                # ...
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
            with open(os.path.join(
                self.temp_dir, "data_socket_user_sign_in_info.log"), "w", 
                encoding="utf-8") as datalog_write:
                datalog_write.write(str(self.get_result))
if __name__=="__main__":
    backend_setup = Set_up_backend()
