import os
import sys
import ast
import time
import threading
import tkinter.messagebox
from selenium import webdriver
from .sign_in_UI import sign_in
from . import browsers_searcher
from . select_ticket_buyer_UI import buyer_selection
from .get_valid_code_UI import get_valid_code
from . import deal_browser_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class get_ticket:
    def __init__(self, train_code, choose_start_station, choose_end_station, period_start_station, period_end_station,
                 train_go_date, condition, choose_index_train, train_start_time, train_code_list, reflex_table, file_dir,
                 computer_screen_height, computer_screen_width, total_ticket_num):
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
        self.file_dir_name = file_dir
        self.temp_dir = os.path.join(self.file_dir_name, 'temp')
        self.init_url = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.is_already_error=False
        self.button_xpath = None
        self.driver=None
        self.train_code_index = -1
        self.train_go_date = train_go_date
        self.train_code = train_code
        self.choose_start_station = choose_start_station
        self.choose_end_station = choose_end_station
        self.period_start_station=period_start_station
        self.period_end_station=period_end_station
        self.condition = condition
        self.choose_index_train = choose_index_train
        self.train_start_time=train_start_time
        self.train_code_list=train_code_list
        self.reflex_table=reflex_table
        self.computer_width=computer_screen_width
        self.computer_high=computer_screen_height
        self.total_ticket_num=total_ticket_num
        print(self.total_ticket_num)
        self.cookies = [{"name": "JSESSIONID", "value": "9A3A60B55A2ACC51B24B6742E68E6230"},
                        {"name": "RAIL_EXPIRATION", "value": "1582469373862"},
                        {"name": "RAIL_DEVICEID",
                         "value": "ERLN34ss4QuQiVGSBZaJz35V5mfm37V7QotSqYowrxa7ljZeEnI-RQjWRUTV8qjMdb5w8sps-WX286eIS9RF7Y_TOr4Cj6wSa_4UIfjh8GwzQPfWOV6nz8EIIIEfX-3ciBnc11jpF14E5BBpRzAqtiV8gdANBiKr"},
                        {"name": "BIGipServerpool_passport", "value": "267190794.50215.0000"},
                        {"name": "route", "value": "495c805987d0f5c8c84b14f60212447d"}]
        print(train_code, choose_start_station, choose_end_station, period_start_station, period_end_station,
              train_go_date, condition, choose_index_train, train_start_time, train_code_list, self.reflex_table)
        self.open_browsers()
    def open_browsers(self):
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
        for inborn_driver in self.inborn_driver_list:
            for host_browser in self.browsers_list:
                if inborn_driver==host_browser["browser_type"]:
                    self.choosed_driver=inborn_driver
                    self.browser_dir=host_browser["path"]
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
                            tkinter.messagebox.showerror(
                                title="不兼容",
                                message="本项目未自带本机中浏览器的驱动程序。请阅读readme文件，并指定驱动和下载地址。如问题仍未解决，请发布issue")
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
                            tkinter.messagebox.showerror(
                                title="不兼容",
                                message="本项目未自带本机中浏览器的驱动程序。请阅读readme文件，并指定驱动和下载地址。如问题仍未解决，请发布issue")
                    elif self.system_type=="darwin":
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
                            tkinter.messagebox.showerror(
                                title="不兼容",
                                message="本项目未自带本机中浏览器的驱动程序。请阅读readme文件，并指定驱动和下载地址。如问题仍未解决，请发布issue")
                    else:
                        tkinter.messagebox.showerror(
                            title="不兼容",
                            message="如果您正在使用源码运行该项目，说明该源码暂时不兼容您的操作系统，请阅读readme文件并安装本项目以更好的兼容。如问题仍未解决，请发布issue")
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
                    self.contant=self.driver.get(self.init_url)
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
                    self.contant=self.driver.get(self.init_url)
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
                    self.contant=self.driver.get(self.init_url)
                    for cookies in self.cookies:
                        self.driver.add_cookie(cookies)
                    self.web_get_ticket()
                else:
                    tkinter.messagebox.showerror(title="Error", message="Error")
            except:
                continue
            break
        if self.count==len(self.choosed_driver_name_list):
            tkinter.messagebox.showerror(title="Error", message="无法使用任何浏览器，请确保您的系统浏览器或浏览器驱动已升级到最新。")
            deal_browser_driver.check_browsers_drivers_error(
                self.browsers_dir_list, self.choosed_driver_name_list, self.computer_width, self.computer_high)
        else:
            pass
    def get_train_ticket_button(self):
        for ticket_range_index in range(self.total_ticket_num):
            self.train_ticket_label_xpath=(
                r"/html/body/div[2]/div[7]/div[13]/table/tbody/tr[{}]".formate(ticket_range_index*2))
            self.ticket_label_element=self.driver.find_element(By.XPATH, self.train_ticket_label_xpath)
            self.ticket_label_html=self.ticket_label_element.get_attribute("outerHTML")
        self.select_info_list=None
        self.reflex_table_keys=list(self.reflex_table.keys())
        self.reflex_table_values=list(self.reflex_table.values())
        if self.condition == "1":
            self.index = self.reflex_table_values.index(self.train_code-1)
            self.range_value = self.reflex_table_keys[self.index]+1
            for index in range(self.range_value):
                self.train_code_index += 2
            self.select_info_list=[self.train_code_list[self.train_code-1], self.train_start_time,
                                   self.period_start_station, self.period_end_station]
        elif self.condition == "2":
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
                title="Get ticket error",
                message="Can not get ticket correctly, please try share these bug in our github issues")
            pass
        if self.is_already_error==True:
            tkinter.messagebox.showerror(
                title="Get ticket error",
                message="Can not get ticket correctly, please try share these bug in our github issues")
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
        self.sign_in_socket_file=os.path.join(self.temp_dir, "data_socket_user_sign_in_info.log")
        self.valid_code_socket_file=os.path.join(self.temp_dir, "data_socket_user_valid_code_info.log")
        self.valid_code_resend_file=os.path.join(self.temp_dir, "data_socket_user_resend_valid_code_info.log")
        if os.path.exists(self.valid_code_socket_file):
            os.remove(self.valid_code_socket_file)
        if not os.path.exists(self.sign_in_socket_file):
            tkinter.messagebox.showerror(title="登录", message="请先登录")
            sign_in(self.computer_width, self.computer_high, self.file_dir_name)
        while self.is_exist!=True:
            if os.path.exists(self.sign_in_socket_file)==True:
                self.is_exist=True
        self.is_exist=False
        with open(self.sign_in_socket_file, "r", encoding="utf-8") as sign_in_info:
            self.sign_in_info=sign_in_info.read()
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
        while self.is_statement_exit!=True:
            try:
                if self.driver.find_element(By.XPATH, self.sign_in_statement_xpath).is_displayed()==True:
                    self.is_statement_exit=True
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
        self.get_valid_code_thread=threading.Thread(
            target=get_valid_code,
            args=(self.computer_width, self.computer_high, self.file_dir_name, self.sign_in_info[0]),
            daemon=True)
        self.get_valid_code_thread.start()
        while self.is_exist!=True:
            if os.path.exists(self.valid_code_socket_file)==True:
                self.is_exist=True
            if os.path.exists(self.valid_code_resend_file)==True:
                self.get_valid_code_button = WebDriverWait(self.driver, timeout=20).until(
                    EC.element_to_be_clickable((By.XPATH, self.get_valid_code_xpath)))
                self.get_valid_code_button.click()
                os.remove(self.valid_code_resend_file)
        self.is_exist=False
        with open(self.valid_code_socket_file, "r", encoding="utf-8") as valid_code_info:
            self.valid_code_info=valid_code_info.read()
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
        while self.is_statement_exit!=True or self.is_over_time==False:
            try:
                self.sign_in_statement = self.driver.find_element(By.XPATH, self.sign_in_statement_xpath)
                if self.sign_in_statement.is_displayed()==True:
                    self.is_statement_exit = True
                self.next_page_statement=self.driver.find_element(By.XPATH, self.next_page_xpath)
                if self.next_page_statement.is_displayed()==True:
                    self.is_statement_exit=True
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
                    self.valid_code_statement_text=="很抱歉，您输入的短信验证码有误。"):
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
        print(self.is_over_time)
    def ensure_ticket_info(self):
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
        while self.is_exist!=True:
            if os.path.exists(self.passengers_name_file)==True:
                self.is_exist=True
        self.is_exist=False
        with open(self.passengers_name_file, "r", encoding="utf-8") as passengers_name_file:
            self.passengers_name_read=passengers_name_file.read()
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
        while self.is_statement_exit!=True:
            try:
                if self.driver.find_element(By.XPATH, self.ticket_get_succeess_xpath).is_displayed()==True:
                    self.is_statement_exit=True
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

# /html/body/div[1]/div[2]/div[2]/div[2]/div[12]/p/span/a
# /html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[3]/td[1]/label/input
# /html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div[2]/select
# /html/body/div[1]/div[3]/div[2]/a[2]




















