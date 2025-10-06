import os
import tkinter
from analyze_json.analyze_city_json import all_city
from analyze_json.analyze_city_station_json import all_city_station
class choose_start_station:
    def __init__(self, computer_info_width, computer_info_height):
        self.file_dir_name = os.path.dirname(os.path.abspath(__file__))
        self.temp_dir = os.path.join(self.file_dir_name, 'temp')
        self.all_city_name=all_city().get_city_name()
        self.all_city_adCode=all_city().get_city_adCode()
        self.all_city_code=all_city().get_city_code()
        self.all_city_station_name=all_city_station().get_station_name()
        self.all_city_station_first_code=all_city_station().get_station_first_code()
        self.all_city_station_generateId=all_city_station().get_station_generatedId()
        self.all_city_station_ID=all_city_station().get_station_Id()
        self.all_city_station_pycode=all_city_station().get_station_py_code()
        self.windows_choose_start_station = tkinter.Toplevel()
        # self.windows_choose_start_station_icon = self.windows_choose_start_station.iconbitmap(
        #     r"./ticket_12306_prog_addition/download_photo.ico")
        self.start_station_entery = tkinter.Entry(
            self.windows_choose_start_station, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.x_entry = 50
        self.y_entry = 80 / 3
        self.start_station_entery.place(x=self.x_entry, y=self.y_entry)
        self.title_1 = self.windows_choose_start_station.title("请选择出发车站")
        self.windows_choose_start_station_height = 300
        self.windows_choose_start_station_width = 500
        self.unresizeable = self.windows_choose_start_station.resizable(False, False)
        self.screen_choose_start_station_x = int((computer_info_width - self.windows_choose_start_station_width) / 2)
        self.screen_choose_start_station_y = int((computer_info_height - self.windows_choose_start_station_height) / 2)
        self.windows_choose_start_station_position_str = "{}x{}+{}+{}".format(
            self.windows_choose_start_station_width, self.windows_choose_start_station_height,
            self.screen_choose_start_station_x, self.screen_choose_start_station_y)
        self.New_choose_start_station_Windows = self.windows_choose_start_station.geometry(
            self.windows_choose_start_station_position_str)
        self.button_research_get_info()
        self.button_sure_get_info()
        print(self.all_city_name, "\n", self.all_city_station_name)
    def search_button_operate(self):
        self.get_text_res = self.start_station_entery.get()
        for all_city_name in self.all_city_name:
            if self.get_text_res==all_city_name:
                self.label=tkinter.Label(self.windows_choose_start_station, text="{}(城)".format(all_city_name))
                self.pack=self.label.pack(pady=30)
        for all_city_station_name in self.all_city_station_name:
            if self.get_text_res==all_city_station_name:
                self.label = tkinter.Label(self.windows_choose_start_station, text="{}(站)".format(all_city_station_name))
                self.pack = self.label.pack(pady=30)
    def sure_button_operate(self):
        self.get_text_res = self.start_station_entery.get()
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        with open(os.path.join(self.temp_dir, "data_socket_start_station.log"), "w", encoding="utf-8") as datalog_write:
            datalog_write.write(self.get_text_res)
        self.windows_choose_start_station.destroy()
    def button_research_get_info(self):
        self.button_get_start_station = tkinter.Button(
            self.windows_choose_start_station, text="查询车站", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_get_start_place=self.button_get_start_station.pack(side=tkinter.TOP)
        self.bind_func_research=self.button_get_start_station.bind("<Button-1>", lambda event: self.search_button_operate())
    def button_sure_get_info(self):
        self.button_get_start_station_sure = tkinter.Button(
            self.windows_choose_start_station, text="确认", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_get_start_place_sure=self.button_get_start_station_sure.pack(side=tkinter.BOTTOM)
        self.bind_func_sure=self.button_get_start_station_sure.bind("<Button-1>", lambda event: self.sure_button_operate())





