import os
import json
class all_city:
    def __init__(self):
        self.dir_bar_list=[]
        self.dir_bar=""
        self.current_dir_this_file = os.path.dirname(os.path.abspath(__file__))
        for i in range(len(self.current_dir_this_file)):
            self.dir_bar+=self.current_dir_this_file[i]
            if self.current_dir_this_file[i]=="/" or self.current_dir_this_file[i]=="\\":
                self.dir_bar_list.append(self.dir_bar)
                self.dir_bar=""
        self.current_dir_this_file=""
        for j in self.dir_bar_list:
            self.current_dir_this_file+=j
        self.city_json_path = os.path.join(self.current_dir_this_file, 'ticket_12306_prog_addition', 'city.json')
        self.city_data=None
        self.all_city=[]
        self.ad_code=[]
        self.city_code=[]
        with open(self.city_json_path, 'r', encoding="utf-8") as self.city_json_file:
            self.city_data = json.load(self.city_json_file)
    def get_city_name(self):
        for list_letter_index in range(len(self.city_data)):
            self.letter_city_list=self.city_data[list_letter_index]["list"]
            for city_info in self.letter_city_list:
                self.city_name=city_info["name"]
                self.all_city.append(self.city_name)
        return self.all_city
    def get_city_adCode(self):
        for list_letter_index in range(len(self.city_data)):
            self.letter_city_list=self.city_data[list_letter_index]["list"]
            for city_info in self.letter_city_list:
                self.city_adCode = city_info["adCode"]
                self.ad_code.append(self.city_adCode)
        return self.ad_code
    def get_city_code(self):
        for list_letter_index in range(len(self.city_data)):
            self.letter_city_list=self.city_data[list_letter_index]["list"]
            for city_info in self.letter_city_list:
                self.city_Code = city_info["cityCode"]
                self.city_code.append(self.city_Code)
        return self.city_code





