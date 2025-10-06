import os
import json
class all_city_station:
    def __init__(self):
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
        self.city_station_json_path = os.path.join(self.current_dir_this_file, 'ticket_12306_prog_addition', 'cityTrain.json')
        self.city_data=None
        with open(self.city_station_json_path, 'r', encoding="utf-8") as self.city_station_json_file:
            self.city_data = json.load(self.city_station_json_file)
        self.city_station_all_info=self.city_data["cityTrain"]
    def get_station_name(self):
        self.station_name=None
        self.station_list=[]
        for every_city_info in self.city_station_all_info:
            self.station_name=every_city_info["value"]
            self.station_list.append(self.station_name)
        return self.station_list
    def get_station_first_code(self):
        self.station_firstCode=None
        self.station_firstCode_list=[]
        for every_city_info in self.city_station_all_info:
            self.station_firstCode=every_city_info["first_code"]
            self.station_firstCode_list.append(self.station_firstCode)
        return self.station_firstCode_list
    def get_station_generatedId(self):
        self.station_generatedID=None
        self.station_generatedID_list=[]
        for every_city_info in self.city_station_all_info:
            self.station_generatedID=every_city_info["generatedId"]
            self.station_generatedID_list.append(self.station_generatedID)
        return self.station_generatedID_list
    def get_station_Id(self):
        self.station_ID=None
        self.station_ID_list=[]
        for every_city_info in self.city_station_all_info:
            self.station_ID=every_city_info["id"]
            self.station_ID_list.append(self.station_ID)
        return self.station_ID_list
    def get_station_py_code(self):
        self.station_py_code=None
        self.station_py_code_list=[]
        for every_city_info in self.city_station_all_info:
            self.station_py_code=every_city_info["py_code"]
            self.station_py_code_list.append(self.station_py_code)
        return self.station_py_code_list








