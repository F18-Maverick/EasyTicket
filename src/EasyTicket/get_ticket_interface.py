import os
import tkinter
import threading
import tkinter.messagebox
from all_threads import thread_all
class Get_ticket_interface:
    def __init__(self):
        self.file_dir_name=os.path.dirname(os.path.abspath(__file__))
        self.temp_dir = os.path.join(self.file_dir_name, 'temp')
        self.entery_start=None
        self.entery_end=None
        self.entery_date=None
        self.Windows = tkinter.Tk()
        self.title = self.Windows.title("Numbers Analyze tool")
        self.Windows_height = 450
        self.Windows_width = 1000
        self.progress_windows = None
        self.computer_info_height = self.Windows.winfo_screenheight()
        self.computer_info_width = self.Windows.winfo_screenwidth()
        self.screen_x = int((self.computer_info_width-self.Windows_width) / 2)
        self.screen_y = int((self.computer_info_height-self.Windows_height) / 2)
        self.size_position_str = "{}x{}+{}+{}".format(
            self.Windows_width, self.Windows_height, self.screen_x, self.screen_y)
        self.New_Windows = self.Windows.geometry(self.size_position_str)
        #self.windows_icon = self.Windows.iconbitmap(r"./ticket_12306_prog_addition/download_photo.ico")
        self.label_start=tkinter.Label(self.Windows, text="出发城市/车站:", font=("微软雅黑", 12))
        self.label_start_pack=self.label_start.pack(side="top", pady=20)
        self.label_end = tkinter.Label(self.Windows, text="到达城市/车站:", font=("微软雅黑", 12))
        self.label_end_place = self.label_end.place(x=self.Windows_width/2-58, y=75)
        self.label_date = tkinter.Label(self.Windows, text="出发日期:", font=("微软雅黑", 12))
        self.label_date_place = self.label_date.place(x=self.Windows_width / 2 - 58, y=125)
    def Entry_Function(self):
        self.entery_start=tkinter.Entry(
            self.Windows, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体",15,"underline"),
            width=88, relief="solid", insertwidth=1)
        self.x_entry_start=50
        self.y_entry_start=50
        self.entery_start.place(x=self.x_entry_start, y=self.y_entry_start)
        self.entery_end = tkinter.Entry(
            self.Windows, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=88, relief="solid", insertwidth=1)
        self.x_entry_end = 50
        self.y_entry_end = 100
        self.entery_end.place(x=self.x_entry_end, y=self.y_entry_end)
        self.entery_date = tkinter.Entry(
            self.Windows, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=88, relief="solid", insertwidth=1)
        self.x_entry_date = 50
        self.y_entry_date = 150
        self.entery_date.place(x=self.x_entry_date, y=self.y_entry_date)
    def get_text_condition(self):
        self.start_station=self.entery_start.get()
        self.end_station=self.entery_end.get()
        self.date=self.entery_date.get()
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
            with open(os.path.join(self.temp_dir, "data_socket_start_station.log"), "w", encoding="utf-8") as datalog_write:
                datalog_write.write(self.start_station)
            with open(os.path.join(self.temp_dir, "data_socket_end_station.log"), "w", encoding="utf-8") as datalog_write_1:
                datalog_write_1.write(self.end_station)
            with open(os.path.join(self.temp_dir, "data_socket_start_date.log"), "w", encoding="utf-8") as datalog_write_2:
                datalog_write_2.write(self.date)
        elif os.path.exists(self.temp_dir):
            with open(os.path.join(self.temp_dir, "data_socket_start_station.log"), "w", encoding="utf-8") as datalog_write:
                datalog_write.write(self.start_station)
            with open(os.path.join(self.temp_dir, "data_socket_end_station.log"), "w", encoding="utf-8") as datalog_write_1:
                datalog_write_1.write(self.end_station)
            with open(os.path.join(self.temp_dir, "data_socket_start_date.log"), "w", encoding="utf-8") as datalog_write_2:
                datalog_write_2.write(self.date)
        self.get_ticket_info_func=thread_all().download_ticket_station_info_thread(
            self.computer_info_height, self.computer_info_width)
        self.entery_start.delete(0, tkinter.END)
        self.entery_end.delete(0, tkinter.END)
        self.entery_date.delete(0, tkinter.END)
    def update_info(self):
        if (not os.path.exists(self.temp_dir) or
            not os.path.exists(os.path.join(self.temp_dir, "data_socket_start_station.log")) or
            not os.path.exists(os.path.join(self.temp_dir, "data_socket_end_station.log")) or
            not os.path.exists(os.path.join(self.temp_dir, "data_socket_start_date.log"))):
            self.error_box = tkinter.messagebox.showerror(
                title="未找到文件",
                message="请填写购票信息(出发时间, 出发车站, 到达车站)")
        elif os.path.exists(self.temp_dir):
            with open(os.path.join(self.temp_dir, "data_socket_start_station.log"), "r", encoding="utf-8") as datalog_read:
                self.start_place=datalog_read.read()
            with open(os.path.join(self.temp_dir, "data_socket_end_station.log"), "r", encoding="utf-8") as datalog_read_1:
                self.end_place=datalog_read_1.read()
            with open(os.path.join(self.temp_dir, "data_socket_start_date.log"), "r", encoding="utf-8") as datalog_read_2:
                self.date=datalog_read_2.read()
            self.entery_start.delete(0, tkinter.END)
            self.entery_start.insert(0, self.start_place)
            self.entery_end.delete(0, tkinter.END)
            self.entery_end.insert(0, self.end_place)
            self.entery_date.delete(0, tkinter.END)
            self.entery_date.insert(0, self.date)
    def update_station_info_thread(self):
        self.thread_station_info_update=threading.Thread(
            target=self.update_info, name="thread5", daemon=True)
        self.thread_station_name_update=self.thread_station_info_update.start()
    def Windows_Button(self):
        self.button_search_start_station=tkinter.Button(
            self.Windows, text="查询车站", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_search_start_station_width=self.button_search_start_station.winfo_width()
        self.button_search_start_station_height=self.button_search_start_station.winfo_height()
        self.x=int(self.Windows_width-self.button_search_start_station_width)
        self.y=25
        self.butoon_search_start_station_place=self.button_search_start_station.place(x=self.x, y=self.y, anchor="ne")
        self.use_choose_start_station_UI=self.button_search_start_station.bind(
            "<Button-1>", lambda event: thread_all().choose_start_station_UI_thread(
                self.computer_info_width, self.computer_info_height))
        self.button_search_end_station=tkinter.Button(
            self.Windows, text="查询车站", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_search_end_station_width = self.button_search_end_station.winfo_width()
        self.button_search_end_station_height = self.button_search_end_station.winfo_height()
        self.x_1=int(self.Windows_width - self.button_search_end_station_width)
        self.y_1=75
        self.button_search_end_station_place=self.button_search_end_station.place(x=self.x_1, y=self.y_1, anchor="ne")
        self.use_choose_end_station_UI=self.button_search_end_station.bind(
            "<Button-1>", lambda event_1: thread_all().choose_end_station_UI_thread(
                self.computer_info_width, self.computer_info_height))
        self.button_search_date = tkinter.Button(
            self.Windows, text="选择日期", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_search_date_width = self.button_search_date.winfo_width()
        self.button_search_date_height = self.button_search_date.winfo_height()
        self.x_2 = int(self.Windows_width - self.button_search_date_width)
        self.y_2 = 125
        self.button_search_date_place = self.button_search_date.place(x=self.x_2, y=self.y_2, anchor="ne")
        self.use_choose_start_time_UI = self.button_search_date.bind(
            "<Button-1>", lambda event_1: thread_all().choose_start_time_UI_thread(
                self.computer_info_width, self.computer_info_height))
        self.button_search_sure=tkinter.Button(
            self.Windows, text="确认", width=25, height=5, font=("Arial", 10, "underline"))
        self.button_search_sure_width=self.button_search_sure.winfo_width()
        self.button_search_sure_height=self.button_search_sure.winfo_height()
        self.x_3=int(self.Windows_width-self.button_search_sure_width)
        self.y_3=300
        self.button_search_sure_place=self.button_search_sure.place(x=self.x_3/2, y=self.y_3, anchor="center")
        self.sure_button_operate = self.button_search_sure.bind(
            "<Button-1>", lambda event_1: self.get_text_condition())
        self.button_update_info = tkinter.Button(
            self.Windows, text="同步选择信息(必选)", width=20, height=1, font=("Arial", 8, "underline"))
        self.button_update_width = self.button_update_info.winfo_width()
        self.button_update_height = self.button_update_info.winfo_height()
        self.x_4 = int(self.Windows_width - self.button_update_width)
        self.y_4 = 200
        self.button_update_info_place = self.button_update_info.place(x=self.x_4/2, y=self.y_4, anchor="center")
        self.update_info_control = self.button_update_info.bind(
            "<Button-1>", lambda event_1: self.update_station_info_thread())
        self.button_sign_in = tkinter.Button(
            self.Windows, text="登录", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_sign_in_width = self.button_sign_in.winfo_width()
        self.button_sign_in_height = self.button_sign_in.winfo_height()
        self.x_5 = int(self.Windows_width - self.button_sign_in_width)
        self.y_5 = 200
        self.button_sign_in_place = self.button_sign_in.place(x=self.x_5, y=self.y_5, anchor="ne")
        self.sign_in_control = self.button_sign_in.bind(
            "<Button-1>", lambda event_1: thread_all().user_sign_in_UI_thread(
                self.computer_info_width, self.computer_info_height, self.file_dir_name))






















