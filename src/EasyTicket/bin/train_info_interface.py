import os
import sys
import json
import tkinter
import threading
from tkinter import font
import tkinter.messagebox
from .get_train_code_ticket import get_ticket
class train_ticket_choose_UI:
    def __init__(self, train_info, main_window_height, main_window_width, train_date,
                 choosed_start_station, choosed_end_station, reflex_table):
        self.main_window_height=main_window_height
        self.main_window_width=main_window_width
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
        self.station_name_dir=os.path.join(self.current_dir_this_file, "temp", "station_name_info.json")
        self.train_code_dir=os.path.join(self.current_dir_this_file, "temp", "data_socket_train_code.log")
        self.train_index=0
        self.reflex_table=reflex_table
        self.condition=None
        self.period_start_name = None
        self.period_end_name = None
        self.train_start_name = None
        self.train_end_name = None
        self.train_go_date=train_date
        self.choosed_start_station=choosed_start_station
        self.choosed_end_station=choosed_end_station
        self.choose_train_ticket=[]
        self.train_code_list=[]
        self.train_ticket_condition=[]
        self.train_info_lists=[]
        self.message_bar=[]
        self.train_info_dict=train_info
        self.text_font=font.Font(family="微软雅黑", size=10)
        self.sapce_length=self.text_font.measure(" ")
        self.text_info = self.text_font.metrics()
        self.text_height = self.text_info["ascent"] + self.text_info["descent"]
        with open(self.station_name_dir, "r", encoding="utf-8") as station_name:
            self.station_name_info=station_name.read()
        self.interface_width=1000
        self.interface_height=800
        self.ListBox_width = self.interface_width
        self.ListBox_height = int(self.interface_height / self.text_height)-1
        if sys.platform=="linux":
            self.ListBox_height = int(self.interface_height / self.text_height) - 5
        self.every_lettice_length = self.ListBox_width / 6
        self.screen_choose_ticket_x = int((self.main_window_width - self.interface_width) / 2)
        self.screen_choose_ticket_y = int((self.main_window_height - self.interface_height) / 2)
        self.info_UI()
        self.train_ticket_UI=tkinter.Toplevel()
        self.windows_choose_ticket_position_str = "{}x{}+{}+{}".format(
            self.interface_width, self.interface_height, self.screen_choose_ticket_x, self.screen_choose_ticket_y)
        self.train_ticket_UI.geometry(self.windows_choose_ticket_position_str)
        self.scrollbar=tkinter.Scrollbar(self.train_ticket_UI)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.train_ticket_list = tkinter.Listbox(
            self.train_ticket_UI, yscrollcommand=self.scrollbar.set, width=self.ListBox_width, height=self.ListBox_height)
        self.title_label=tkinter.Label(self.train_ticket_UI, text=self.title_complete, font=self.text_font)
        for index in self.message_bar:
            self.train_ticket_list.insert(tkinter.END, index)
        self.train_ticket_list.pack(side=tkinter.BOTTOM)
        self.scrollbar.config(command=self.train_ticket_list.yview)
        self.title_label.pack(side=tkinter.TOP)
        self.entery_start = tkinter.Entry(
            self.train_ticket_UI, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=80, relief="solid", insertwidth=1)
        self.x_entry_start = 0
        self.y_entry_start = self.text_height + 3
        self.entery_start.place(x=self.x_entry_start, y=self.y_entry_start)
        self.button_sure=self.button_sure_ticket()
    def info_UI(self):
        for train_ticket_info in self.train_info_dict:
            self.train_index+=1
            self.train_number=list(train_ticket_info.keys())[0]
            self.left_ticket_info = train_ticket_info[self.train_number][7]
            self.period_start_time = train_ticket_info[self.train_number][4]
            self.period_end_time = train_ticket_info[self.train_number][5]
            self.need_time = train_ticket_info[self.train_number][6]
            self.train_code_list.append(self.train_number)
            self.train_ticket_condition.append(self.left_ticket_info)
            for station_name, station_code in json.loads(self.station_name_info).items():
                if train_ticket_info[list(train_ticket_info.keys())[0]][0]==station_code:
                    self.train_start_name=station_name
                elif train_ticket_info[list(train_ticket_info.keys())[0]][1]==station_code:
                    self.train_end_name=station_name
                if train_ticket_info[list(train_ticket_info.keys())[0]][2]==station_code:
                    self.period_start_name=station_name
                elif train_ticket_info[list(train_ticket_info.keys())[0]][3]==station_code:
                    self.period_end_name=station_name
            self.complete_peorid_station="{}-{}".format(self.train_start_name, self.train_end_name)
            self.choose_peorid_station="{}-{}".format(self.period_start_name, self.period_end_name)
            self.choose_time_peorid="{}-{}".format(self.period_start_time, self.period_end_time)
            self.space_length_1=(
                int((self.every_lettice_length-self.text_font.measure(str(self.train_number)))/self.sapce_length))
            self.space_length_2=(
                int((self.every_lettice_length-self.text_font.measure(str(self.complete_peorid_station)))/self.sapce_length))
            self.space_length_3=(
                int((self.every_lettice_length-self.text_font.measure(str(self.left_ticket_info)))/self.sapce_length))
            self.space_length_4=(
                int((self.every_lettice_length-self.text_font.measure(str(self.choose_peorid_station)))/self.sapce_length))
            self.space_length_5=(
                int((self.every_lettice_length-self.text_font.measure(str(self.choose_time_peorid)))/self.sapce_length))
            self.space_length_6=30
            self.train_info="{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
                self.train_number, " "*self.space_length_1, self.complete_peorid_station, " "*self.space_length_2,
                self.left_ticket_info, " "*self.space_length_3, self.choose_peorid_station, " "*self.space_length_4,
                self.choose_time_peorid, " "*self.space_length_5, self.need_time, " "*self.space_length_6, str(self.train_index))
            self.message_bar.append(self.train_info)
            self.train_info_lists.append([self.train_number, train_ticket_info[list(train_ticket_info.keys())[0]][2],
                                          train_ticket_info[list(train_ticket_info.keys())[0]][3], self.period_start_time])
        self.title_list=["车次", "列车始发/终点站", "余票情况", "选择的始发/终点站", "列车始发/终到时间", "中途耗时", "列车编号"]
        self.space_num_list=[]
        self.title_each_length=self.interface_width/7
        for titles in self.title_list:
            self.space_length=int((self.title_each_length-self.text_font.measure(titles))/self.sapce_length)
            self.space_num_list.append(self.space_length)
        self.title_complete="{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
            self.title_list[0], self.space_num_list[0]*" ", self.title_list[1], self.space_num_list[1]*" ", self.title_list[2],
            self.space_num_list[2]*" ", self.title_list[3], self.space_num_list[3]*" ", self.title_list[4], self.space_num_list[4]*" ",
            self.title_list[5], self.space_num_list[5]*" ", self.title_list[6], self.space_num_list[6]*" ")
    def get_ticket_thread(self):
        print(self.train_code_list)
        self.ticket_choose_train_thread = threading.Thread(
            target=get_ticket,
            args=(self.text_train_code, self.choosed_start_station, self.choosed_end_station,
                  self.period_start_name, self.period_end_name, self.train_go_date, self.condition,
                  self.choose_train_ticket, self.period_start_time, self.train_code_list,
                  self.reflex_table, self.current_dir_this_file, self.main_window_height, self.main_window_width, 
                  len(self.train_info_dict)),
            name="thread10", daemon=True)
        self.ticket_choose_train_thread_start = self.ticket_choose_train_thread.start()
    def get_enter_contant(self):
        self.count=0
        self.count_1=0
        self.count_2=0
        self.check_condition=False
        self.text_train_code=self.entery_start.get()
        print(self.train_info_lists)
        try:
            int(self.text_train_code)
            self.condition="1"
        except ValueError:
            self.condition="2"
            pass
        if self.condition=="1":
            if int(self.text_train_code) > int(self.train_index):
                self.error_box = tkinter.messagebox.showerror(
                    title="为找到车次",
                    message="请填写正确的车次")
            elif (self.train_ticket_condition[int(self.text_train_code)-1]=="票已售罄，无法购票" or
                  self.train_ticket_condition[int(self.text_train_code)-1]=="该票未起售"):
                self.error_box = tkinter.messagebox.showerror(
                    title="为找到车次",
                    message="该车票无法购买")
            else:
                self.text_train_code = int(self.text_train_code)
                self.period_start_name=self.train_info_lists[self.text_train_code-1][1]
                self.period_end_name=self.train_info_lists[self.text_train_code-1][2]
                self.period_start_time=self.train_info_lists[self.text_train_code-1][3]
                with open(self.train_code_dir, "w", encoding="utf-8") as train_code:
                    train_code.write(str(self.text_train_code))
                self.get_ticket_thread()
        elif self.condition=="2":
            self.period_start_name=[]
            self.period_end_name=[]
            self.period_start_time=[]
            for i in range(len(self.train_code_list)):
                if self.text_train_code == self.train_code_list[i]:
                    self.count_2+=1
                    self.check_condition=True
                    if (self.train_ticket_condition[i]== "票已售罄，无法购票" or
                        self.train_ticket_condition[i]=="该票未起售"):
                        self.count_1+=1
                    else:
                        self.choose_train_ticket.append(i)
                        self.period_start_name.append(self.train_info_lists[i][1])
                        self.period_end_name.append(self.train_info_lists[i][2])
                        self.period_start_time.append(self.train_info_lists[i][3])
                    with open(self.train_code_dir, "w", encoding="utf-8") as train_code:
                        train_code.write(self.text_train_code)
                else:
                    self.count += 1
            if self.count==len(self.train_code_list) and self.check_condition==False:
                self.error_box = tkinter.messagebox.showerror(
                    title="未找到车次",
                    message="请正确填写车次")
            else:
                if self.count_1==self.count_2:
                    self.error_box = tkinter.messagebox.showerror(title="未找到车次", message="该车票无法购买")
                else:
                    self.get_ticket_thread()
    def button_sure_ticket(self):
        self.button_get_train_code = tkinter.Button(
            self.train_ticket_UI, text="确定", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_get_train_code_width = self.button_get_train_code.winfo_width()
        self.button_get_train_code_height = self.button_get_train_code.winfo_height()
        self.x = int(self.interface_width - self.button_get_train_code_width)-15
        self.y = self.text_height+3
        self.butoon_get_train_code_place = self.button_get_train_code.place(x=self.x, y=self.y, anchor="ne")
        self.get_train_code = self.button_get_train_code.bind(
            "<Button-1>", lambda event: self.get_enter_contant())











