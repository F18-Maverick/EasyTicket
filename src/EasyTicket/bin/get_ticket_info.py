import os
import ssl
import json
import tkinter
import threading
import http.cookiejar
import urllib.request
import tkinter.messagebox
from .train_info_interface import train_ticket_choose_UI
class get_ticket_station_info:
    def __init__(self, main_window_height, main_window_width):
        self.dir_bar_list = []
        self.dir_bar = ""
        self.current_dir_this_file = os.path.dirname(os.path.abspath(__file__))
        for i in range(len(self.current_dir_this_file)):
            self.dir_bar += self.current_dir_this_file[i]
            if self.current_dir_this_file[i] == "/" or self.current_dir_this_file[i] == "\\":
                self.dir_bar_list.append(self.dir_bar)
                self.dir_bar = ""
        self.current_dir_this_file = ""
        for j in self.dir_bar_list:
            self.current_dir_this_file += j
        self.ssl_context_dir=os.path.join(self.current_dir_this_file, "ticket_12306_prog_addition", "cacert.pem")
        self.temp_dir = os.path.join(self.current_dir_this_file, "temp")
        self.main_window_height=main_window_height
        self.main_window_width=main_window_width
        self.constant=ssl.create_default_context(cafile=self.ssl_context_dir)
        self.ticket_all_info_dict=[]
        self.station_start_symbol=None
        self.station_end_symbol=None
        self.station_name_dict={}
        self.start_city=None
        self.end_city=None
        self.date_start=None
        if os.path.exists(self.temp_dir):
            self.temp_dir_start = os.path.join(self.temp_dir, "data_socket_start_station.log")
            self.temp_dir_end = os.path.join(self.temp_dir, "data_socket_end_station.log")
            self.temp_dir_date = os.path.join(self.temp_dir, "data_socket_start_date.log")
            with open(self.temp_dir_start, "r", encoding="utf-8") as read_start:
                self.read_condition_start=read_start.read()
            with open(self.temp_dir_end, "r", encoding="utf-8") as read_end:
                self.read_condition_end=read_end.read()
            with open(self.temp_dir_end, "r", encoding="utf-8") as read_date:
                self.read_condition_date=read_date.read()
        self.condition=(
                not os.path.exists(self.temp_dir) or self.read_condition_start==""
                or self.read_condition_end=="" or self.read_condition_date=="")
        if self.condition:
            self.error_box=tkinter.messagebox.showerror(
                title="未找到文件",
                message="请填写购票信息(出发时间, 出发车站, 到达车站)")
        else:
            self.Download_get_station_info()
    def Download_get_station_info(self):
        self.header = {
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            "User-Agent":
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            "Cookie":
                'JSESSIONID=9A3A60B55A2ACC51B24B6742E68E6230; RAIL_EXPIRATION=1582469373862; RAIL_DEVICEID=ERLN34ss4QuQiVGSBZaJz35V5mfm37V7QotSqYowrxa7ljZeEnI-RQjWRUTV8qjMdb5w8sps-WX286eIS9RF7Y_TOr4Cj6wSa_4UIfjh8GwzQPfWOV6nz8EIIIEfX-3ciBnc11jpF14E5BBpRzAqtiV8gdANBiKr; BIGipServerpool_passport=267190794.50215.0000; route=495c805987d0f5c8c84b14f60212447d; _jc_save_toDate=2020-02-20; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2020-02-20; BIGipServerotn=451936778.24610.0000; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E4C%u9C81%u6728%u9F50%2CWAR'
        }
        self.cookie_jar = http.cookiejar.CookieJar()
        self.cookie_handler = urllib.request.HTTPCookieProcessor(self.cookie_jar)
        self.opener = urllib.request.build_opener(self.cookie_handler)
        self.station_name_url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9330"
        self.train_info_url=\
            "https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes={}"
        self.add_url_headers = urllib.request.Request(url=self.station_name_url, headers=self.header)
        self.response_url=urllib.request.urlopen(self.add_url_headers, context=self.constant)
        self.station_name_info=self.response_url.read().decode("utf-8")
        self.count=0
        self.count_1 = []
        self.count_4=[]
        self.station_info_section_list_index=[]
        self.station_info_section_list=[]
        self.station_symbol_list=[]
        self.station_name_list=[]
        self.station_info_dict={}
        for every_letter in self.station_name_info:
            self.count+=1
            if every_letter=="@":
                self.station_info_section_list_index.append(self.count-1)
        for index in range(len(self.station_info_section_list_index)-1):
            self.station_info_section = ""
            for section_index in range(
                    self.station_info_section_list_index[index], self.station_info_section_list_index[index+1]):
                self.station_info_section+=self.station_name_info[section_index]
            self.station_info_section_list.append(self.station_info_section)
        for all_station in self.station_info_section_list:
            self.count_2=0
            self.count_3=0
            for symbol_index in range(len(all_station)):
                if all_station[symbol_index]=="|":
                    self.count_1.append(symbol_index)
                    self.count_2+=1
                    if self.count_2==2:
                        break
            for all_station_name_index in range(len(self.count_1)-1):
                self.station_name=""
                for station_name_index in range(self.count_1[all_station_name_index]+1, self.count_1[all_station_name_index+1]):
                    self.station_name+=all_station[station_name_index]
            self.station_name_list.append(self.station_name)
            for symbol_index_1 in range(len(all_station)):
                if all_station[symbol_index_1]=="|":
                    self.count_3+=1
                    if self.count_3==2:
                        self.count_4.append(symbol_index_1)
                    elif self.count_3==3:
                        self.count_4.append(symbol_index_1)
                        break
            for all_station_symbol_index in range(len(self.count_4)-1):
                self.station_symbol=""
                for station_symbol_index in range(self.count_4[all_station_symbol_index]+1, self.count_4[all_station_symbol_index+1]):
                    self.station_symbol+=all_station[station_symbol_index]
            self.station_symbol_list.append(self.station_symbol)
        for all_station_info_index in range(len(self.station_name_list)):
            self.station_info_dict[self.station_name_list[all_station_info_index]]=self.station_symbol_list[all_station_info_index]
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        with open(os.path.join(self.temp_dir, "station_name_info.json"), "w", encoding="utf-8") as datalog_write:
            json.dump(self.station_info_dict, datalog_write, indent=4, ensure_ascii=False)
        with open(self.temp_dir_start, "r", encoding="utf-8") as datalog_city_start_read:
            self.start_city=datalog_city_start_read.read()
        with open(self.temp_dir_end, "r", encoding="utf-8") as datalog_city_end_read:
            self.end_city=datalog_city_end_read.read()
        with open(self.temp_dir_date, "r", encoding="utf-8") as datalog_city_start_date_read:
            self.date_start = datalog_city_start_date_read.read()
        if self.start_city not in self.station_info_dict:
            self.error_box = tkinter.messagebox.showerror(
                title="未找到文件",
                message="请填写正确的购票信息(出发时间, 出发车站, 到达车站)")
        else:
            self.station_start_symbol=self.station_info_dict[self.start_city].upper()
        if self.end_city not in self.station_info_dict:
            self.error_box = tkinter.messagebox.showerror(
                title="未找到文件",
                message="请填写正确的购票信息(出发时间, 出发车站, 到达车站)")
        else:
            self.station_end_symbol=self.station_info_dict[self.end_city].upper()
        self.train_info_url_compleat=self.train_info_url.format(self.date_start, self.station_start_symbol, self.station_end_symbol, "ADULT")
        self.add_url_headers_train_info = urllib.request.Request(url=self.train_info_url_compleat, headers=self.header)
        self.response_url_train = urllib.request.urlopen(self.add_url_headers_train_info, context=self.constant)
        self.statude_code=self.response_url_train.getcode()
        self.train_info = self.response_url_train.read().decode("utf-8")
        self.train_info_dict=json.loads(self.train_info)
        self.train_code_list=[]
        self.train_start_station_list=[]
        self.train_end_station_list=[]
        self.peo_want_start_station_list=[]
        self.peo_want_end_station_list=[]
        self.train_start_time_list=[]
        self.train_end_time_list=[]
        self.pass_time_list=[]
        self.ticket_can_get_Y_N=[]
        self.reflex_table={} # key值是项目UI输入index，value是12306官网按钮的index
        for all_train_info in self.train_info_dict["data"]["result"]:
            self.count_5 = 0
            self.count_6 = 0
            self.count_7 = 0
            self.count_8 = 0
            self.count_9 = 0
            self.count_10 = 0
            self.count_11 = 0
            self.count_12 = 0
            self.count_13 = 0
            self.train_code=""
            self.train_start_station=""
            self.train_end_station=""
            self.peo_want_start_station=""
            self.peo_want_end_station=""
            self.train_start_time=""
            self.train_end_time=""
            self.pass_time=""
            self.Y_N=""
            self.ticket_Y_N=None
            for symbol_index_2 in range(len(all_train_info)):
                if all_train_info[symbol_index_2]=="|":
                    self.count_5+=1
                if self.count_5==3:
                    self.train_code+=all_train_info[symbol_index_2+1]
                    if self.count_5==4:
                        break
            self.train_code_list.append(self.train_code.rstrip("|"))
            for symbol_index_3 in range(len(all_train_info)):
                if all_train_info[symbol_index_3]=="|":
                    self.count_6+=1
                if self.count_6==4:
                    self.train_start_station+=all_train_info[symbol_index_3+1]
                    if self.count_6==5:
                        break
            self.train_start_station_list.append(self.train_start_station.rstrip("|"))
            for symbol_index_4 in range(len(all_train_info)):
                if all_train_info[symbol_index_4]=="|":
                    self.count_7+=1
                if self.count_7==5:
                    self.train_end_station+=all_train_info[symbol_index_4+1]
                    if self.count_7==6:
                        break
            self.train_end_station_list.append(self.train_end_station.rstrip("|"))
            for symbol_index_5 in range(len(all_train_info)):
                if all_train_info[symbol_index_5]=="|":
                    self.count_8+=1
                if self.count_8==6:
                    self.peo_want_start_station+=all_train_info[symbol_index_5+1]
                    if self.count_8==7:
                        break
            self.peo_want_start_station_list.append(self.peo_want_start_station.rstrip("|"))
            for symbol_index_6 in range(len(all_train_info)):
                if all_train_info[symbol_index_6]=="|":
                    self.count_9+=1
                if self.count_9==7:
                    self.peo_want_end_station+=all_train_info[symbol_index_6+1]
                    if self.count_9==8:
                        break
            self.peo_want_end_station_list.append(self.peo_want_end_station.rstrip("|"))
            for symbol_index_7 in range(len(all_train_info)):
                if all_train_info[symbol_index_7]=="|":
                    self.count_10+=1
                if self.count_10==8:
                    self.train_start_time+=all_train_info[symbol_index_7+1]
                    if self.count_10==9:
                        break
            self.train_start_time_list.append(self.train_start_time.rstrip("|"))
            for symbol_index_8 in range(len(all_train_info)):
                if all_train_info[symbol_index_8]=="|":
                    self.count_11+=1
                if self.count_11==9:
                    self.train_end_time+=all_train_info[symbol_index_8+1]
                    if self.count_11==10:
                        break
            self.train_end_time_list.append(self.train_end_time.rstrip("|"))
            for symbol_index_9 in range(len(all_train_info)):
                if all_train_info[symbol_index_9]=="|":
                    self.count_12+=1
                if self.count_12==10:
                    self.pass_time+=all_train_info[symbol_index_9+1]
                    if self.count_12==11:
                        break
            self.pass_time_list.append(self.pass_time.rstrip("|"))
            for symbol_index_10 in range(len(all_train_info)):
                if all_train_info[symbol_index_10]=="|":
                    self.count_13+=1
                if self.count_13==11:
                    self.Y_N+=all_train_info[symbol_index_10+1]
                    if self.count_13==12:
                        break
            self.Y_N_after=self.Y_N.rstrip("|")
            if str(self.Y_N_after)=="Y":
                self.ticket_Y_N="允许继续购票"
            elif str(self.Y_N_after)=="N":
                self.ticket_Y_N="票已售罄，无法购票"
            else:
                self.ticket_Y_N="该票未起售"
            self.ticket_can_get_Y_N.append(self.ticket_Y_N)
        for all_info_index in range(len(self.train_code_list)):
            self.reflex_table[all_info_index]=all_info_index
            self.train_info_dict = []
            self.every_train_info={}
            self.train_info_dict.append(self.train_start_station_list[all_info_index])
            self.train_info_dict.append(self.train_end_station_list[all_info_index])
            self.train_info_dict.append(self.peo_want_start_station_list[all_info_index])
            self.train_info_dict.append(self.peo_want_end_station_list[all_info_index])
            self.train_info_dict.append(self.train_start_time_list[all_info_index])
            self.train_info_dict.append(self.train_end_time_list[all_info_index])
            self.train_info_dict.append(self.pass_time_list[all_info_index])
            self.train_info_dict.append(self.ticket_can_get_Y_N[all_info_index])
            self.every_train_info[self.train_code_list[all_info_index]]=self.train_info_dict
            self.ticket_all_info_dict.append(self.every_train_info)
        for count_index in range(len(self.ticket_can_get_Y_N)):
            if self.ticket_can_get_Y_N[count_index]=="该票未起售":
                del self.reflex_table[count_index]
        self.reflex_table_keys_list=list(self.reflex_table.keys())
        self.reflex_table_values_list=list(self.reflex_table.values())
        for count_train_code_index in range(len(self.reflex_table)-1):
            for left_train_code_index in range(count_train_code_index+1, len(self.reflex_table)):
                if (self.train_code_list[self.reflex_table_values_list[count_train_code_index]]==
                    self.train_code_list[self.reflex_table_values_list[left_train_code_index]]):
                    self.reflex_table_values_list.insert(
                        count_train_code_index,
                        self.reflex_table_values_list[left_train_code_index])
                    del self.reflex_table_values_list[left_train_code_index+1]
        for index in range(len(self.reflex_table_values_list)):
            self.reflex_table[self.reflex_table_keys_list[index]]=self.reflex_table_values_list[index]
        print(self.reflex_table)
        with open(os.path.join(self.temp_dir, "all_TrainStation_info.json"), "w", encoding="utf-8") as train_info_json:
            train_info_json.write(json.dumps(self.ticket_all_info_dict, ensure_ascii=False))
        self.ticket_choose_interface_thread=threading.Thread(
            target=train_ticket_choose_UI,
            args=(self.ticket_all_info_dict, self.main_window_height, self.main_window_width,
                  self.date_start, self.start_city, self.end_city, self.reflex_table),
            name="thread5", daemon=True)
        self.ticket_choose_interface_thread_start=self.ticket_choose_interface_thread.start()


















