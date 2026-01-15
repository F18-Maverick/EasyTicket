import os
import sys
import ast
import time
import threading
import tkinter.messagebox
from selenium import webdriver
from .sign_in_UI import sign_in
from . import browsers_searcher
from . import deal_browser_driver
from . import get_new_browser_driver_UI
from . select_ticket_buyer_UI import buyer_selection
from .get_valid_code_UI import get_valid_code
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class get_ticket:
    def __init__(self, **kwargs):
        self.kwargs=kwargs
        self.inital_vars(kwargs)
        self.open_browsers()
    def inital_vars(self, kwargs):
        self.button_xpath=None
        self.is_exist=False
        self.is_over_time=False
        self.is_valid_code_pass=None
        self.sign_sure_button_xapth=None
        self.passenger_name_input_xpath=None
        self.ID_code_entry_xpath=None
        self.reget_valid_code_xpath=None
        self.before_valid_code_xpath=None
        self.sign_in_statement_xpath=None
        self.is_statement_exit=None
        self.file_dir_name = kwargs["file_dir"]
        self.temp_dir = os.path.join(self.file_dir_name, 'temp')
        self.init_url = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.is_already_error=False
        self.button_xpath = None
        self.driver=None
        self.train_code_index = -1
        self.train_go_date = kwargs["train_go_date"]
        self.train_code = kwargs["train_code"]
        self.choose_start_station = kwargs["choose_start_station"]
        self.choose_end_station = kwargs["choose_end_station"]
        self.period_start_station=kwargs["period_start_station"]
        self.period_end_station=kwargs["period_end_station"]
        self.condition = kwargs["condition"]
        self.choose_index_train = kwargs["choose_index_train"]
        self.train_start_time=kwargs["train_start_time"]
        self.train_code_list=kwargs["train_code_list"]
        self.reflex_table=kwargs["reflex_table"]
        self.computer_width=kwargs["computer_screen_width"]
        self.computer_high=kwargs["computer_screen_height"]
        self.total_ticket_num=kwargs["total_ticket_num"]
        print(self.total_ticket_num)
        self.cookies = [{"name": "JSESSIONID", "value": "9A3A60B55A2ACC51B24B6742E68E6230"},
                        {"name": "RAIL_EXPIRATION", "value": "1582469373862"},
                        {"name": "RAIL_DEVICEID",
                         "value": "ERLN34ss4QuQiVGSBZaJz35V5mfm37V7QotSqYowrxa7ljZeEnI-RQjWRUTV8qjMdb5w8sps-WX286eIS9RF7Y_TOr4Cj6wSa_4UIfjh8GwzQPfWOV6nz8EIIIEfX-3ciBnc11jpF14E5BBpRzAqtiV8gdANBiKr"},
                        {"name": "BIGipServerpool_passport", "value": "267190794.50215.0000"},
                        {"name": "route", "value": "495c805987d0f5c8c84b14f60212447d"}]
        print(self.train_code, self.choose_start_station, self.choose_end_station, self.period_start_station, self.period_end_station,
              self.train_go_date, self.condition, self.choose_index_train, self.train_start_time, self.train_code_list, self.reflex_table)
    def open_browsers(self):
        self.add_uknown_browser_driver_log=os.path.join(
                self.temp_dir, "data_socket_unknown_browser_driver_info.log")
        self.new_browser_driver_info=None
        self.browsers_dir_copy_list=[]
        self.copy_browser_dir=os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), 
                    "driver", "browser")
        self.count=0
        self.abs_dir = os.path.dirname(os.path.abspath(__file__))
        self.inborn_driver_list=["firefox", "waterfox", "firefox-developer", "firefox-nightly", "msedge", "msedge-dev", "msedge-beta",
                                 "msedge-canary", "chromium", "chrome", "chrome-canary", "chrome-dev", "ungoogled-chromium"]
        self.browsers_list=browsers_searcher.get()
        self.choosed_driver_type_list=[]
        self.choosed_driver_name_list=[]
        self.choosed_browsers_dir_list=[]
        self.browsers_dir_list=[]
        self.system_type=sys.platform
        self.choosed_driver=None
        self.choosed_driver_name=None
        self.browser_dir=None
        self.is_already_add_new_browser_driver=False
        if len(self.browsers_list)==0:
            get_new_browser_driver_UI.AddUnknownBrowserDriverWindow(self.temp_dir)
            while True:
                if os.path.exists(self.add_uknown_browser_driver_log)==True:
                    break
        def deal_add_new_log():
            with open(
                self.add_uknown_browser_driver_log, 
                "r", 
                encoding="utf-8") as uknown_browser_driver_info:
                self.new_browser_driver_info=ast.literal_eval(
                    uknown_browser_driver_info.read())
        def add_new_browser_driver_to_list():
            tkinter.messagebox.showerror(
                title="不兼容",
                message="本项目不支持操作系统中现有的浏览器")
            if self.is_already_add_new_browser_driver==False:
                get_new_browser_driver_UI.AddUnknownBrowserDriverWindow(self.temp_dir)
                while True:
                    if os.path.exists(self.add_uknown_browser_driver_log)==True:
                        break
                deal_add_new_log()
            self.choosed_driver_name=os.path.basename(
                self.new_browser_driver_info[0]["driver_path"])
            self.choosed_driver=self.new_browser_driver_info[0]["browser_type"]
            self.browser_dir=self.new_browser_driver_info[0]["browser_path"]
            self.choosed_driver_name_list.append(self.choosed_driver_name)
            self.choosed_driver_type_list.append(self.choosed_driver)
            self.choosed_browsers_dir_list.append(self.browser_dir)
            self.is_already_add_new_browser_driver=True
        if os.path.exists(self.add_uknown_browser_driver_log)==True:
            deal_add_new_log()
            self.browsers_list.append(
                {"browser_type": self.new_browser_driver_info[
                    len(self.new_browser_driver_info)-1]["browser_type"], 
                 "path": self.new_browser_driver_info[
                    len(self.new_browser_driver_info)-1]["browser_path"]})
            self.is_already_add_new_browser_driver=True
        for inborn_driver in self.inborn_driver_list:
            self.count_compare_time=0
            for host_browser in self.browsers_list:
                if inborn_driver==host_browser["browser_type"]:
                    self.choosed_driver=inborn_driver
                    self.browser_dir=host_browser["path"]
                    self.browsers_dir_copy_list.append(self.browser_dir)
                    if os.path.exists(self.copy_browser_dir)==True:
                        self.browser_dir=os.path.join(self.copy_browser_dir, os.path.basename(self.browser_dir))
                    self.browsers_dir_list.append(self.browser_dir)
                    if (self.system_type=="win32" or self.system_type=="cygwin" or self.system_type=="win64"
                        or self.system_type=="windows" or self.system_type=="Windows"):
                        if (self.choosed_driver=="firefox" or self.choosed_driver=="waterfox" or self.choosed_driver=="firefox-developer"
                            or self.choosed_driver=="firefox-nightly"):
                            self.choosed_driver_name="geckodriver.exe"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif (self.choosed_driver=="msedge" or self.choosed_driver=="msedge-dev" or self.choosed_driver=="msedge-beta"
                              or self.choosed_driver=="msedge-canary"):
                            self.choosed_driver_name="msedgedriver.exe"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif self.choosed_driver=="chromium" or self.choosed_driver=="chrome" or self.choosed_driver=="chrome-canary":
                            self.choosed_driver_name="chromedriver.exe"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        else:
                            self.count_compare_time+=1
                            if self.count_compare_time==len(self.browsers_list):
                                add_new_browser_driver_to_list()
                    elif self.system_type=="linux" or self.system_type=="Linux":
                        if self.choosed_driver=="firefox" or self.choosed_driver=="waterfox":
                            self.choosed_driver_name="geckodriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif self.choosed_driver=="msedge" or self.choosed_driver=="msedge-dev":
                            self.choosed_driver_name="msedgedriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif (self.choosed_driver=="chrome" or self.choosed_driver=="chrome-dev" or self.choosed_driver=="chromium"
                              or self.choosed_driver=="ungoogled-chromium"):
                            self.choosed_driver_name="chromedriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        else:
                            self.count_compare_time+=1
                            if self.count_compare_time==len(self.browsers_list):
                                add_new_browser_driver_to_list()
                    elif self.system_type=="darwin":
                        tkinter.messagebox.showinfo(
                            title="提示",
                            message="本项目没有自带该系统的驱动程序，请手动下载并通过接下来的提示手动添加驱动程序")
                        if (self.choosed_driver_name=="firefox" or self.choosed_driver_name=="firefox-developer" or
                            self.choosed_driver_name=="firefox-nightly"):
                            self.choosed_driver_name = "geckodriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif (self.choosed_driver_name=="msedge" or self.choosed_driver_name=="msedge-beta" or
                              self.choosed_driver_name=="msedge-dev" or self.choosed_driver_name=="msedge-canary"):
                            self.choosed_driver_name = "msedgedriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif (self.choosed_driver=="chrome" or self.choosed_driver=="chrome-beta" or self.choosed_driver=="chrome-canary"
                              or self.choosed_driver=="chrome-dev" or self.choosed_driver_name=="chrome-test" or
                              self.choosed_driver_name=="chromium"):
                            self.choosed_driver_name="chromedriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        else:
                            self.count_compare_time+=1
                            if self.count_compare_time==len(self.browsers_list):
                                add_new_browser_driver_to_list()
                    else:
                        tkinter.messagebox.showerror(
                            title="不兼容",
                            message="如果您正在使用源码运行该项目，说明该源码暂时不兼容您的操作系统，请阅读readme文件并安装本项目以更好的兼容。如问题仍未解决，请发布issue")
                        add_new_browser_driver_to_list()
        print(self.choosed_driver_type_list, "...", self.choosed_driver_name_list, "...", self.choosed_browsers_dir_list, "...", self.browsers_dir_list)
        for index in range(len(self.choosed_driver_name_list)):
            self.driver_dir = os.path.join(self.abs_dir, "driver", self.choosed_driver_name_list[index])
            try:
                if (self.choosed_driver_type_list[index]=="firefox" or self.choosed_driver_type_list[index]=="waterfox" or
                    self.choosed_driver_type_list[index]=="firefox-developer" or self.choosed_driver_type_list[index]=="firefox-nightly"):
                    self.count += 1
                    from selenium.webdriver.firefox.options import Options
                    from selenium.webdriver.firefox.service import Service
                    self.options = Options()
                    # self.options.add_argument('--headless')
                    self.options.binary_location = self.browsers_dir_list[index]
                    self.web_driver=Service(executable_path=self.driver_dir)
                    self.driver = webdriver.Firefox(service=self.web_driver, options=self.options)
                    self.driver.get(self.init_url)
                    for cookies in self.cookies:
                        self.driver.add_cookie(cookies)
                    self.web_get_ticket()
                elif (self.choosed_driver_type_list[index]=="msedge" or self.choosed_driver_type_list[index]=="msedge-dev"
                      or self.choosed_driver_type_list[index]=="msedge-beta" or self.choosed_driver_type_list[index]=="msedge-canary"):
                    self.count += 1
                    from selenium.webdriver.edge.options import Options
                    from selenium.webdriver.edge.service import Service
                    self.options = Options()
                    # self.options.add_argument('--headless')
                    self.options.binary_location = self.browsers_dir_list[index]
                    self.web_driver = Service(executable_path=self.driver_dir)
                    self.driver=webdriver.Edge(service=self.web_driver, options=self.options)
                    self.driver.get(self.init_url)
                    for cookies in self.cookies:
                        self.driver.add_cookie(cookies)
                    self.web_get_ticket()
                elif (self.choosed_driver_type_list[index]=="chrome" or self.choosed_driver_type_list[index]=="chrome-dev"
                      or self.choosed_driver_type_list[index]=="chromium" or self.choosed_driver_type_list[index]=="chrome-canary"
                      or self.choosed_driver_type_list[index]=="ungoogled-chromium" or self.choosed_driver_type_list[index]=="chrome-beta"
                      or self.choosed_driver_type_list[index]=="chrome-test"):
                    self.count += 1
                    from selenium.webdriver.chrome.options import Options
                    from selenium.webdriver.chrome.service import Service
                    self.options = Options()
                    # self.options.add_argument('--headless')
                    self.options.binary_location = self.browsers_dir_list[index]
                    self.web_driver = Service(executable_path=self.driver_dir)
                    self.driver=webdriver.Chrome(service=self.web_driver, options=self.options)
                    self.driver.get(self.init_url)
                    for cookies in self.cookies:
                        self.driver.add_cookie(cookies)
                    self.web_get_ticket()
                elif (self.choosed_driver_type_list[index]=="ie"):
                    self.count+=1
                    from selenium.webdriver.ie.options import Options
                    from selenium.webdriver.ie.service import Service
                    self.options = Options()
                    # self.options.add_argument('--headless')
                    self.options.binary_location = self.browsers_dir_list[index]
                    self.web_driver = Service(executable_path=self.driver_dir)
                    self.driver=webdriver.Ie(service=self.web_driver, options=self.options)
                    self.driver.get(self.init_url)
                    for cookies in self.cookies:
                        self.driver.add_cookie(cookies)
                    self.web_get_ticket()
                elif (self.choosed_driver_type_list[index]=="safari"):
                    self.count+=1
                    from selenium.webdriver.safari.options import Options
                    from selenium.webdriver.safari.service import Service
                    self.options = Options()
                    # self.options.add_argument('--headless')
                    self.options.binary_location = self.browsers_dir_list[index]
                    self.web_driver = Service(executable_path=self.driver_dir)
                    self.driver=webdriver.Safari(service=self.web_driver, options=self.options)
                    self.driver.get(self.init_url)
                    for cookies in self.cookies:
                        self.driver.add_cookie(cookies)
                    self.web_get_ticket()
                else:
                    tkinter.messagebox.showerror(title="调用错误", 
                                                 message="未找到可用的浏览器驱动，请检查输入的浏览器类型是否正确")
                    self.open_browsers()
            except:
                self.inital_vars(self.kwargs)
                continue
            break
        if self.count==len(self.choosed_driver_name_list):
            self.result_record_file_name="data_socket_error_deal_result.log"
            self.record_result_file_dir=os.path.join(
                self.temp_dir, self.result_record_file_name)
            self.deal_result=None
            tkinter.messagebox.showerror(title="错误", message="无法使用任何浏览器，请确保您的系统浏览器或浏览器驱动已升级到最新。")
            deal_func_init=deal_browser_driver.check_browsers_drivers_error(
                self.browsers_dir_copy_list, self.choosed_driver_name_list, 
                self.computer_width, self.computer_high, self.temp_dir)
            deal_func_init.show_info_window()
            while True:
                if os.path.exists(self.record_result_file_dir)==True:
                    break
            if os.path.exists(self.record_result_file_dir)==True:
                with open(self.record_result_file_dir, "r", encoding="utf-8") as deal_result_read:
                    self.deal_result=deal_result_read.read()
                os.remove(self.record_result_file_dir)
                if self.deal_result=="True":
                    self.open_browsers()
                else:
                    tkinter.messagebox.showerror(title="未能解决", message="无法解决问题, 请阅读readme或发布issue")
            else:
                pass
        else:
            pass
    def get_train_ticket_button(self):
        self.is_find_button_success=None
        self.select_info_list=None
        self.reflex_table_keys=list(self.reflex_table.keys())
        self.reflex_table_values=list(self.reflex_table.values())
        if self.condition == "1":
            try:
                for ticket_range_index in range(1, self.total_ticket_num+1):
                    if self.is_find_button_success==True:
                        break
                    self.train_ticket_label_xpath=(
                        r"/html/body/div[2]/div[7]/div[13]/table/tbody/tr[{}]".format(ticket_range_index*2))
                    self.ticket_label_element=WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, self.train_ticket_label_xpath)))
                    self.ticket_label_html=self.ticket_label_element.get_attribute("outerHTML")
                    for element_attribute in self.ticket_label_html.split(" "):
                        if element_attribute=='datatran="{}"'.format(self.train_code_list[self.train_code-1]):
                            self.train_code_index=-1
                            self.range_value=ticket_range_index
                            for index in range(self.range_value):
                                self.train_code_index+=2
                            self.button_xpath = (
                                "/html/body/div[2]/div[7]/div[13]/table/tbody/tr[{}]/td[13]/a".format(self.train_code_index))
                            self.ticket_button_element=WebDriverWait(self.driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, self.button_xpath)))
                            self.ticket_button_html=self.ticket_button_element.get_attribute("outerHTML")
                            ticket_attribute_list=self.ticket_button_html.split(" ")
                            ticket_button_js_list=ticket_attribute_list[3].split(",")
                            if (ticket_button_js_list[3]=="'{}'".format(self.period_start_station) and 
                                ticket_button_js_list[4]=="'{}'".format(self.period_end_station)):
                                self.is_find_button_success=True
                                break
            except:
                self.index = self.reflex_table_values.index(self.train_code-1)
                self.range_value = self.reflex_table_keys[self.index]+1
                for index in range(self.range_value):
                    self.train_code_index += 2
            self.select_info_list=[self.train_code_list[self.train_code-1], self.train_start_time,
                                   self.period_start_station, self.period_end_station]
        elif self.condition == "2":
            self.train_index_list=[]
            try:
                for ticket_range_index in range(1, self.total_ticket_num+1):
                    self.train_ticket_label_xpath=(
                        r"/html/body/div[2]/div[7]/div[13]/table/tbody/tr[{}]".format(ticket_range_index*2))
                    self.ticket_label_element=WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, self.train_ticket_label_xpath)))
                    self.ticket_label_html=self.ticket_label_element.get_attribute("outerHTML")
                    for element_attribute in self.ticket_label_html.split(" "):
                        if element_attribute=='datatran="{}"'.format(self.train_code):
                            self.train_code_index=-1
                            self.range_value=ticket_range_index
                            for index in range(self.range_value):
                                self.train_code_index+=2
                            self.train_index_list.append(self.train_code_index)
                self.train_code_index=self.train_index_list[int(len(self.train_index_list)/2)]
            except:
                self.ticket_index=int(len(self.choose_index_train)/2)
                self.index = self.reflex_table_values.index(self.choose_index_train[self.ticket_index])
                self.range_value = self.reflex_table_keys[self.index]+1
                for index in range(self.range_value):
                    self.train_code_index += 2
            self.select_info_list=[self.train_code, self.train_start_time[self.ticket_index],
                                   self.period_start_station[self.ticket_index], self.period_end_station[self.ticket_index]]
        print(self.train_code_index)
        if self.is_already_error==False:
            try:
                self.button_xpath = (
                    "/html/body/div[2]/div[7]/div[13]/table/tbody/tr[{}]/td[13]/a".format(self.train_code_index))
                print(self.button_xpath)
                self.button_get_choose_ticket = WebDriverWait(self.driver, timeout=20).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_xpath)))
                self.button_get_choose_ticket.click()
            except:
                self.is_already_error=True
        else:
            tkinter.messagebox.showerror(
                title="未知错误",
                message="无法解决的问题，请在本项目的issues区发布issue")
            pass
        if self.is_already_error==True:
            tkinter.messagebox.showerror(
                title="未知错误",
                message="无法解决的问题，请在本项目的issues区发布issue")
        else:
            pass
    def sign_in(self):
        self.sign_in_info=None
        self.is_exist=False
        self.is_statement_exit=False
        self.contact_input_xpath=r"/html/body/div[2]/div[33]/div[2]/div[1]/div[1]/div[1]/input"
        self.password_input_xpath=r"/html/body/div[2]/div[33]/div[2]/div[1]/div[1]/div[2]/input"
        self.sure_sign_in_info_xpath=r"/html/body/div[2]/div[33]/div[2]/div[1]/div[1]/div[4]/a"
        self.ID_code_entry_xpath=r"/html/body/div[2]/div[35]/div[2]/div[1]/div/div[1]/input"
        self.get_valid_code_xpath=r"/html/body/div[2]/div[35]/div[2]/div[1]/div/div[2]/a"
        self.input_valid_code_xpath=r"/html/body/div[2]/div[35]/div[2]/div[1]/div/div[2]/input"
        self.sure_valid_code_button_xpath=r"/html/body/div[2]/div[35]/div[2]/div[1]/div/div[4]/a"
        self.sign_in_statement_xpath=r"/html/body/div[2]/div[35]/div[2]/div[1]/div/div[3]/p"
        self.before_valid_code_xpath=r"/html/body/div[2]/div[35]/div[1]/a"
        self.reget_valid_code_xpath=r"/html/body/div[2]/div[35]/div[2]/ul/li[2]/a"
        self.passenger_name_input_xpath=r"/html/body/div[1]/div[11]/div[3]/div[1]/div/input[1]"
        self.sign_sure_button_xapth=r"/html/body/div[6]/div[2]/div[2]/div[2]/a"
        self.next_page_xpath=r"/html/body/div[1]/div[11]/div[1]/div[1]"
        self.train_ticket_list_xpath=r"/html/body/div[2]/div[7]/div[13]"
        self.choose_valid_way_window_xpath=r"/html/body/div[2]/div[35]"
        self.sign_in_slide_mask_xpath=r"/html/body/div[2]/div[31]"
        self.sign_in_window_xpath=r"/html/body/div[2]/div[33]"
        self.sign_in_socket_file=os.path.join(self.temp_dir, "data_socket_user_sign_in_info.log")
        self.valid_code_socket_file=os.path.join(self.temp_dir, "data_socket_user_valid_code_info.log")
        self.valid_code_resend_file=os.path.join(self.temp_dir, "data_socket_user_resend_valid_code_info.log")
        if os.path.exists(self.valid_code_socket_file):
            os.remove(self.valid_code_socket_file)
        if not os.path.exists(self.sign_in_socket_file):
            tkinter.messagebox.showerror(title="登录", message="请先登录")
            sign_in(self.computer_width, self.computer_high, self.file_dir_name)
        while True:
            if os.path.exists(self.sign_in_socket_file)==True:
                try:
                    with open(self.sign_in_socket_file, "r", encoding="utf-8") as sign_in_info:
                        self.sign_in_info=sign_in_info.read()
                    self.is_exist=True
                    break
                except:
                    pass
        self.is_exist=False
        self.sign_in_info=ast.literal_eval(self.sign_in_info)
        self.contact_info_input=WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.contact_input_xpath)))
        self.contact_info_input.click()
        self.contact_info_input.clear()
        self.contact_info_input.send_keys(self.sign_in_info[0])
        self.password_info_input=WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.password_input_xpath)))
        self.password_info_input.click()
        self.password_info_input.clear()
        self.password_info_input.send_keys(self.sign_in_info[1])
        self.sure_sign_in_info_button=WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.sure_sign_in_info_xpath)))
        self.sure_sign_in_info_button.click()
        self.ID_code_input=WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.ID_code_entry_xpath)))
        self.ID_code_input.click()
        self.ID_code_input.clear()
        self.ID_code_input.send_keys(self.sign_in_info[2])
        self.get_valid_code_button=WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.get_valid_code_xpath)))
        self.get_valid_code_button.click()
        while True:
            try:
                if self.driver.find_element(By.XPATH, self.sign_in_statement_xpath).is_displayed()==True:
                    self.is_statement_exit=True
                    break
                if self.driver.find_element(By.XPATH, self.sure_valid_code_button_xpath).is_displayed() == False:
                    self.is_statement_exit = True
                    break
            except:
                tkinter.messagebox.showerror(title="登录错误", message="请填写正确的登录信息")
        self.is_statement_exit=False
        self.valid_code_statement_text = self.driver.find_element(By.XPATH, self.sign_in_statement_xpath).text
        print(self.valid_code_statement_text)
        if self.valid_code_statement_text=="请输入正确的用户信息!":
            tkinter.messagebox.showerror(title="登录错误", message="请输入正确的用户信息!")
            os.remove(self.sign_in_socket_file)
            self.before_valid_code_button = WebDriverWait(self.driver, timeout=20).until(
                EC.element_to_be_clickable((By.XPATH, self.before_valid_code_xpath)))
            self.before_valid_code_button.click()
            self.sign_in()
        self.get_sure_valid_code()
    def get_sure_valid_code(self):
        self.valid_code_info=None
        self.get_valid_code_thread=threading.Thread(
            target=get_valid_code,
            args=(self.computer_width, self.computer_high, self.file_dir_name, self.sign_in_info[0]),
            daemon=True)
        self.get_valid_code_thread.start()
        while True: # Why this fucking code always can't work in the expression
            if os.path.exists(self.valid_code_socket_file)==True:
                try:
                    with open(self.valid_code_socket_file, "r", encoding="utf-8") as valid_code_info:
                        self.valid_code_info=valid_code_info.read()
                    self.is_exist=True
                    break
                except:
                    pass
            if os.path.exists(self.valid_code_resend_file)==True:
                self.get_valid_code_button = WebDriverWait(self.driver, timeout=20).until(
                    EC.element_to_be_clickable((By.XPATH, self.get_valid_code_xpath)))
                self.get_valid_code_button.click()
                os.remove(self.valid_code_resend_file)
        self.is_exist=False
        self.valid_code_input=WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.input_valid_code_xpath)))
        self.valid_code_input.click()
        self.valid_code_input.clear()
        self.valid_code_input.send_keys(self.valid_code_info)
        self.sure_valid_code_button=WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.sure_valid_code_button_xpath)))
        self.sure_valid_code_button.click()
        try:
            self.sure_tip_button = WebDriverWait(self.driver, timeout=2).until(
                EC.element_to_be_clickable((By.XPATH, self.sign_sure_button_xapth)))
            self.sure_tip_button.click()
        except:
            pass
        timeout_thread=threading.Thread(target=self.time_out_check, daemon=True)
        timeout_thread.start()
        while self.is_statement_exit!=True and self.is_over_time==False: # Who knows why the fucking code is always buggy
            time.sleep(0.5)
            try:
                self.sign_in_statement = self.driver.find_element(By.XPATH, self.sign_in_statement_xpath)
                if self.sign_in_statement.is_displayed()==True:
                    self.is_statement_exit = True
                    break
                self.next_page_statement=self.driver.find_element(By.XPATH, self.next_page_xpath)
                if self.next_page_statement.is_displayed()==True:
                    self.is_statement_exit=True
                    break
                self.is_sign_in_success=self.driver.find_element(By.XPATH, self.sign_in_slide_mask_xpath)
                self.mask_html_code=self.is_sign_in_success.get_attribute("outerHTML")
                self.maks_html_propties_list=self.mask_html_code.split(" ")
                for per_property in self.maks_html_propties_list:
                    if per_property=='none;"></div>': # bug
                        self.is_statement_exit=True
                        break
            except:
                continue
        self.is_statement_exit=False
        try:
            if self.driver.find_element(By.XPATH, self.sign_in_statement_xpath).is_displayed()==True:
                self.valid_code_statement_text = self.driver.find_element(By.XPATH, self.sign_in_statement_xpath).text
                if self.valid_code_statement_text == "用户名或密码错误。":
                    tkinter.messagebox.showerror(title="登录错误", message="用户名或密码错误。")
                    os.remove(self.sign_in_socket_file)
                    self.before_valid_code_button = WebDriverWait(self.driver, timeout=20).until(
                        EC.element_to_be_clickable((By.XPATH, self.before_valid_code_xpath)))
                    self.before_valid_code_button.click()
                    self.sign_in()
                if (self.valid_code_statement_text == "请输入正确验证码" or 
                    self.valid_code_statement_text=="很抱歉，您输入的短信验证码有误。" or 
                    self.valid_code_statement_text=="请输入验证码"):
                    tkinter.messagebox.showerror(title="登录错误", message="短信验证码有误。")
                    os.remove(self.valid_code_socket_file)
                    self.before_valid_code_button = WebDriverWait(self.driver, timeout=20).until(
                        EC.element_to_be_clickable((By.XPATH, self.before_valid_code_xpath)))
                    self.before_valid_code_button.click()
                    time.sleep(0.5)
                    self.sure_sign_in_info_button = WebDriverWait(self.driver, timeout=20).until(
                        EC.element_to_be_clickable((By.XPATH, self.sure_sign_in_info_xpath)))
                    self.sure_sign_in_info_button.click()
                    self.ID_code_input = WebDriverWait(self.driver, timeout=20).until(
                        EC.element_to_be_clickable((By.XPATH, self.ID_code_entry_xpath)))
                    self.ID_code_input.click()
                    self.ID_code_input.clear()
                    self.ID_code_input.send_keys(self.sign_in_info[2])
                    self.get_valid_code_button = WebDriverWait(self.driver, timeout=20).until(
                        EC.element_to_be_clickable((By.XPATH, self.get_valid_code_xpath)))
                    self.get_valid_code_button.click()
                    self.get_sure_valid_code()
            else:
                pass
        except:
            pass
        try:
            self.button_xpath = (
                "/html/body/div[2]/div[7]/div[13]/table/tbody/tr[{}]/td[13]/a".format(self.train_code_index))
            self.button_get_choose_ticket = WebDriverWait(self.driver, timeout=20).until(
                EC.element_to_be_clickable((By.XPATH, self.button_xpath)))
            self.button_get_choose_ticket.click()
        except:
            pass
        print(self.valid_code_info)
        print(self.sign_in_info)
    def time_out_check(self):
        self.time_count_total=2
        while self.time_count_total!=0:
            time.sleep(1)
            self.time_count_total-=1
        self.is_over_time=True
        print(self.is_over_time, "exit the loop")
    def ensure_ticket_info(self):
        self.passengers_name_read=None
        self.give_ticket_info_xpath=r"/html/body/div[1]/div[11]/div[5]/a[2]"
        self.ticket_sure_xpath=r"/html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[8]/a[2]"
        self.tip_sure_xpath=r"/html/body/div[4]/div[2]/div[2]/div[2]/a"
        self.ticket_get_succeess_xpath=r"/html/body/div[1]/div[2]/div[1]/div/h3/span"
        self.passengers_name_file=os.path.join(self.temp_dir, "data_socket_buyer_name_info.log")
        if os.path.exists(self.passengers_name_file):
            os.remove(self.passengers_name_file)
        self.passenger_name_UI_thread=threading.Thread(
            target=buyer_selection,
            args=(self.computer_width, self.computer_high, self.file_dir_name),
            daemon=True)
        self.passenger_name_UI_thread.start()
        while True:
            if os.path.exists(self.passengers_name_file)==True:
                try:
                    with open(self.passengers_name_file, "r", encoding="utf-8") as passengers_name_file:
                        self.passengers_name_read=passengers_name_file.read()
                    self.is_exist=True
                    break
                except:
                    pass
        self.is_exist=False
        self.passengers_name_list=ast.literal_eval(self.passengers_name_read)
        for passenger_name in self.passengers_name_list:
            self.label_index = 0
            while self.label_index<=len(self.passengers_name_list)-1:
                self.passenger_name_label_xpath = (
                    r"/html/body/div[1]/div[11]/div[3]/div[2]/div[1]/div[2]/ul/li[{}]/label".format(
                        self.label_index + 1))
                self.passenger_choose_xpath = (
                    r"/html/body/div[1]/div[11]/div[3]/div[2]/div[1]/div[2]/ul/li[{}]/input".format(
                        self.label_index + 1))
                self.name_label=self.driver.find_element(By.XPATH, self.passenger_name_label_xpath)
                self.name_text=self.name_label.text
                if self.name_text==passenger_name:
                    self.passenger_name_input = WebDriverWait(self.driver, timeout=20).until(
                        EC.element_to_be_clickable((By.XPATH, self.passenger_choose_xpath)))
                    self.passenger_name_input.click()
                self.label_index+=1
                pass
            if self.label_index==len(self.passengers_name_list)-1:
                tkinter.messagebox.showerror(title="选择乘车人错误", message="没有对应的乘车人，请确保已经在12306官网添加乘车人")
                self.ensure_ticket_info()
        self.give_ticket_info_button = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.give_ticket_info_xpath)))
        self.give_ticket_info_button.click()
        try:
            self.tip_sure_button = WebDriverWait(self.driver, timeout=2).until(
                EC.element_to_be_clickable((By.XPATH, self.tip_sure_xpath)))
            self.tip_sure_button.click()
        except:
            pass
        self.sure_ticket_button = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.ticket_sure_xpath)))
        self.sure_ticket_button.click()
        while True:
            try:
                if self.driver.find_element(By.XPATH, self.ticket_get_succeess_xpath).is_displayed()==True:
                    self.is_statement_exit=True
                    break
            except:
                pass
        self.is_statement_exit=False
        tkinter.messagebox.showinfo(title="抢票成功", message="成功抢票，请在浏览器中完成订单支付")
    def web_get_ticket(self):
        self.from_station_input = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.ID, "fromStationText")))
        self.from_station_input.clear()
        self.from_station_input.click()
        self.from_station_input.send_keys(self.choose_start_station)
        self.from_station_input.send_keys(Keys.ENTER)
        self.end_station_input = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.ID, "toStationText")))
        self.end_station_input.clear()
        self.end_station_input.click()
        self.end_station_input.send_keys(self.choose_end_station)
        self.end_station_input.send_keys(Keys.ENTER)
        self.date_input = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.ID, "train_date")))
        self.date_input.clear()
        self.date_input.click()
        self.date_input.send_keys(self.train_go_date)
        self.date_input.send_keys(Keys.ENTER)
        self.button_get_left_ticket = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.ID, "query_ticket")))
        self.button_get_left_ticket.click()
        self.get_train_ticket_button()
        self.sign_in()
        self.ensure_ticket_info()





















