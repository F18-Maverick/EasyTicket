import os
import time
import tkinter
class choose_start_time:
    def __init__(self, computer_info_width, computer_info_height):
        self.file_dir_name = os.path.dirname(os.path.abspath(__file__))
        self.temp_dir = os.path.join(self.file_dir_name, 'temp')
        self.x_entry = 50
        self.y_entry = 80 / 3
        self.windows_choose_start_time = tkinter.Toplevel()
        self.windows_width=self.windows_choose_start_time.winfo_width()
        self.date_local = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.date_local_label = tkinter.Label(self.windows_choose_start_time, text="现在是:{}".format(self.date_local))
        self.data_local_date_pack=self.date_local_label.place(x=self.windows_width/2, y=self.y_entry+90)
        # self.windows_choose_start_time_icon = self.windows_choose_start_time.iconbitmap(
        #     r"./ticket_12306_prog_addition/download_photo.ico")
        self.title_1 = self.windows_choose_start_time.title("请选择日期和时间")
        self.windows_choose_start_time_height = 300
        self.windows_choose_start_time_width = 500
        self.unresizeable = self.windows_choose_start_time.resizable(False, False)
        self.screen_choose_start_time_x = int((computer_info_width - self.windows_choose_start_time_width) / 2)
        self.screen_choose_start_time_y = int((computer_info_height - self.windows_choose_start_time_height) / 2)
        self.windows_choose_start_time_position_str = "{}x{}+{}+{}".format(
            self.windows_choose_start_time_width, self.windows_choose_start_time_height,
            self.screen_choose_start_time_x, self.screen_choose_start_time_y)
        self.New_choose_start_time_Windows = self.windows_choose_start_time.geometry(
            self.windows_choose_start_time_position_str)
        self.year_text=tkinter.Label(self.windows_choose_start_time, text="年")
        self.year_text.place(x=self.x_entry-20, y=self.y_entry)
        self.start_time_entery_year = tkinter.Entry(
            self.windows_choose_start_time, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.start_time_entery_year.place(x=self.x_entry, y=self.y_entry)
        self.month_text = tkinter.Label(self.windows_choose_start_time, text="月")
        self.month_text.place(x=self.x_entry-20, y=self.y_entry+30)
        self.start_time_entery_month = tkinter.Entry(
            self.windows_choose_start_time, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.start_time_entery_month.place(x=self.x_entry, y=self.y_entry+30)
        self.day_text = tkinter.Label(self.windows_choose_start_time, text="日")
        self.day_text.place(x=self.x_entry-20, y=self.y_entry+60)
        self.start_time_entery_day = tkinter.Entry(
            self.windows_choose_start_time, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.start_time_entery_day.place(x=self.x_entry, y=self.y_entry+60)
        self.button=self.button_get_start_time()
    def get_data(self):
        self.years=self.start_time_entery_year.get()
        self.months=self.start_time_entery_month.get()
        self.days=self.start_time_entery_day.get()
        if len(self.days)>=2 and len(self.months)>=2:
            self.get_result="{}-{}-{}".format(self.years, self.months, self.days)
        elif len(self.days)<2:
            self.get_result="{}-{}-0{}".format(self.years, self.months, self.days)
        elif len(self.months)<2:
            self.get_result="{}-0{}-{}".format(self.years, self.months, self.days)
        elif len(self.days)<2 and len(self.months)<2:
            self.get_result="{}-0{}-0{}".format(self.years, self.months, self.days)
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        with open(os.path.join(self.temp_dir, "data_socket_start_date.log"), "w", encoding="utf-8") as datalog_write:
            datalog_write.write(self.get_result)
        self.windows_choose_start_time.destroy()
    def button_get_start_time(self):
        self.button_get_start_time_sure = tkinter.Button(
            self.windows_choose_start_time, text="确认", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_get_start_time_sure_pack = self.button_get_start_time_sure.pack(side=tkinter.BOTTOM)
        self.bind_func_sure = self.button_get_start_time_sure.bind("<Button-1>", lambda event: self.get_data())










