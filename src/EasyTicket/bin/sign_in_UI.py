import os
import tkinter
from tkinter import messagebox
class sign_in:
    def __init__(self, computer_info_width, computer_info_height, file_dir):
        self.computer_info_width=computer_info_width
        self.computer_info_height=computer_info_height
        self.file_dir=file_dir
        self.temp_dir = os.path.join(self.file_dir, 'temp')
        self.x_entry = 50
        self.y_entry = 80 / 3
        self.windows_sign_in = tkinter.Toplevel()
        # self.windows_choose_start_time_icon = self.windows_choose_start_time.iconbitmap(
        #     r"./ticket_12306_prog_addition/download_photo.ico")
        self.title_1 = self.windows_sign_in.title("填写登录信息")
        self.windows_choose_sign_in_height = 300
        self.windows_choose_sign_in_width = 500
        self.unresizeable = self.windows_sign_in.resizable(False, False)
        self.screen_sign_in_x = int((computer_info_width - self.windows_choose_sign_in_width) / 2)
        self.screen_sign_in_y = int((computer_info_height - self.windows_choose_sign_in_height) / 2)
        self.windows_sign_in_position_str = "{}x{}+{}+{}".format(
            self.windows_choose_sign_in_width, self.windows_choose_sign_in_height,
            self.screen_sign_in_x, self.screen_sign_in_y)
        self.New_choose_sign_in_Windows = self.windows_sign_in.geometry(
            self.windows_sign_in_position_str)
        self.contact_info_text = tkinter.Label(self.windows_sign_in, text="用户名/邮箱/手机号")
        self.contact_info_text.place(x=self.x_entry, y=self.y_entry-20)
        self.contact_info_entry = tkinter.Entry(
            self.windows_sign_in, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.contact_info_entry.place(x=self.x_entry, y=self.y_entry)
        self.password_text = tkinter.Label(self.windows_sign_in, text="密码")
        self.password_text.place(x=self.x_entry, y=self.y_entry+25)
        self.password_entry = tkinter.Entry(
            self.windows_sign_in, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.password_entry.place(x=self.x_entry, y=self.y_entry+45)
        self.ID_card_num_text = tkinter.Label(self.windows_sign_in, text="身份证后4位")
        self.ID_card_num_text.place(x=self.x_entry, y=self.y_entry+70)
        self.ID_card_entry = tkinter.Entry(
            self.windows_sign_in, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.ID_card_entry.place(x=self.x_entry, y=self.y_entry + 95)
        self.button=self.button_get_sign_in_info()
    def get_data(self):
        self.contact_info=self.contact_info_entry.get()
        self.password=self.password_entry.get()
        self.ID_card_value=self.ID_card_entry.get()
        self.info_is_valid_state=(self.contact_info==None or len(str(self.contact_info).lstrip())==0 or
                                  self.password==None or len(str(self.password).lstrip())==0 or
                                  self.ID_card_value==None or len(str(self.ID_card_value).lstrip())==0 or
                                  len(self.password)<6 or len(self.ID_card_value)<4 or len(self.ID_card_value)>4)
        if self.info_is_valid_state:
            tkinter.messagebox.showerror(title="登录错误", message="请输入正确的登录信息")
            self.windows_sign_in.destroy()
            sign_in(self.computer_info_width, self.computer_info_height, self.file_dir)
        else:
            self.get_result=[self.contact_info, self.password, self.ID_card_value]
            if not os.path.exists(self.temp_dir):
                os.makedirs(self.temp_dir)
            with open(os.path.join(self.temp_dir, "data_socket_user_sign_in_info.log"), "w", encoding="utf-8") as datalog_write:
                datalog_write.write(str(self.get_result))
            self.windows_sign_in.destroy()
    def button_get_sign_in_info(self):
        self.button_sign_in_sure = tkinter.Button(
            self.windows_sign_in, text="确认", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_get_start_time_sure_pack = self.button_sign_in_sure.pack(side=tkinter.BOTTOM)
        self.bind_func_sure = self.button_sign_in_sure.bind("<Button-1>", lambda event: self.get_data())












