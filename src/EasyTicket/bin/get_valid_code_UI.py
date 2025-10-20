import os
import time
import tkinter
import threading
from tkinter import messagebox
class get_valid_code:
    def __init__(self, computer_info_width, computer_info_height, file_dir, phone_number):
        self.computer_info_width=computer_info_width
        self.computer_info_height=computer_info_height
        self.file_dir=file_dir
        self.phone_number=phone_number
        self.is_window_destory=False
        self.count_total_run=0
        self.button_resend_valid_code=None
        self.file_dir_name = file_dir
        self.temp_dir = os.path.join(self.file_dir_name, 'temp')
        self.x_entry = 50
        self.y_entry = 80 / 3
        self.windows_get_valid_code = tkinter.Toplevel()
        # self.windows_get_valid_code = tkinter.Tk()
        # self.windows_choose_start_time_icon = self.windows_choose_start_time.iconbitmap(
        #     r"./ticket_12306_prog_addition/download_photo.ico")
        self.title_1 = self.windows_get_valid_code.title("填写登录信息")
        self.windows_get_valid_code_height = 300
        self.windows_get_valid_code_width = 500
        self.unresizeable = self.windows_get_valid_code.resizable(False, False)
        self.screen_get_valid_code_x = int((computer_info_width - self.windows_get_valid_code_width) / 2)
        self.screen_get_valid_code_y = int((computer_info_height - self.windows_get_valid_code_height) / 2)
        self.windows_get_valid_code_position_str = "{}x{}+{}+{}".format(
            self.windows_get_valid_code_width, self.windows_get_valid_code_height,
            self.screen_get_valid_code_x, self.screen_get_valid_code_y)
        self.New_choose_get_valid_code_Windows = self.windows_get_valid_code.geometry(
            self.windows_get_valid_code_position_str)
        self.valid_code_text = tkinter.Label(self.windows_get_valid_code, text="验证码")
        self.valid_code_text.place(x=self.x_entry, y=self.y_entry-20)
        self.valid_code_entry = tkinter.Entry(
            self.windows_get_valid_code, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.valid_code_entry.place(x=self.x_entry, y=self.y_entry)
        self.button=self.button_get_sign_in_info()
        self.loading_valid_code="已经验证码发送给:{}".format(phone_number)
        self.loading_valid_code_text=tkinter.Label(self.windows_get_valid_code, text=self.loading_valid_code)
        self.loading_valid_code_text.place(x=self.x_entry, y=self.y_entry+40)
        try:
            self.time_count_bind()
        except:
            pass
    def time_count_bind(self):
        self.count_total_run+=1
        def time_count_down():
            self.time_count_total=60
            # if self.is_window_destory == False:
            while self.time_count_total!=0 and self.is_window_destory==False:
                self.time_text=tkinter.Label(self.windows_get_valid_code, text="重新发送({}秒)".format(self.time_count_total))
                self.time_text.place(x=self.x_entry, y=self.y_entry+60)
                self.time_count_total-=1
                time.sleep(1)
                self.time_text.destroy()
            try:
                self.button_resend_valid_code = tkinter.Button(
                    self.windows_get_valid_code, text="重新发送验证码", width=24, height=1,
                    font=("Arial", 8, "underline"))
                self.button_resend_valid_code.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
                self.bind_resend_code = self.button_resend_valid_code.bind(
                    "<Button-1>", lambda evnet: self.time_count_bind())
            except:
                pass
        def time_count_down_thread():
            self.time_countdown_thread=threading.Thread(target=time_count_down, daemon=True)
            self.time_countdown_thread.start()
        if self.count_total_run!=1:
            with open(os.path.join(self.temp_dir, "data_socket_user_resend_valid_code_info.log"),
                      "w", encoding="utf-8") as datalog_write:
                datalog_write.write(str(1))
        time_count_down_thread()
        if self.count_total_run!=1:
            self.button_resend_valid_code.destroy()
    def get_data(self):
        self.is_window_destory=True
        self.contact_info=self.valid_code_entry.get()
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        if self.contact_info==None or len(str(self.contact_info).lstrip())==0:
            tkinter.messagebox.showerror(title="验证码错误", message="请输入正确的验证码")
            self.windows_get_valid_code.destroy()
            get_valid_code(self.computer_info_width, self.computer_info_height, self.file_dir, self.phone_number)
        else:
            with open(os.path.join(self.temp_dir, "data_socket_user_valid_code_info.log"), "w", encoding="utf-8") as datalog_write:
                datalog_write.write(str(self.contact_info))
            self.windows_get_valid_code.destroy()
    def button_get_sign_in_info(self):
        self.button_sign_in_sure = tkinter.Button(
            self.windows_get_valid_code, text="确认", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_get_start_time_sure_pack = self.button_sign_in_sure.pack(side=tkinter.BOTTOM)
        self.bind_func_sure = self.button_sign_in_sure.bind("<Button-1>", lambda event: self.get_data())

# if __name__=="__main__":
#     get_valid_code(2560, 1600, r"D:\project\python\pythonProject1\Web_Crawler\Analyze_Number\Numers_Analyze_Beta\Analyze_number_mainfile\ticket_12306", "15955152788")
#     tkinter.mainloop()
















