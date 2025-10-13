import os
import tkinter
from tkinter import messagebox
class buyer_selection:
    def __init__(self, computer_info_width, computer_info_height, file_dir):
        self.is_info_invalid=False
        self.buyer_input_field_list=[]
        self.computer_info_width=computer_info_width
        self.computer_info_height=computer_info_height
        self.file_dir=file_dir
        self.temp_dir = os.path.join(self.file_dir, 'temp')
        self.x_entry = 50
        self.y_entry = (80/3)-25
        self.windows_buyer = tkinter.Toplevel()
        # self.windows_buyer = tkinter.Tk()
        # self.windows_choose_start_time_icon = self.windows_choose_start_time.iconbitmap(
        #     r"./ticket_12306_prog_addition/download_photo.ico")
        self.title_1 = self.windows_buyer.title("填写登录信息")
        self.windows_choose_buyer_height = 300
        self.windows_choose_buyer_width = 500
        #self.unresizeable = self.windows_buyer.resizable(False, True)
        self.screen_buyer_x = int((computer_info_width - self.windows_choose_buyer_width) / 2)
        self.screen_buyer_y = int((computer_info_height - self.windows_choose_buyer_height) / 2)
        self.windows_buyer_position_str = "{}x{}+{}+{}".format(
            self.windows_choose_buyer_width, self.windows_choose_buyer_height,
            self.screen_buyer_x, self.screen_buyer_y)
        self.New_choose_buyer_Windows = self.windows_buyer.geometry(
            self.windows_buyer_position_str)
        self.buyer_name_text = tkinter.Label(self.windows_buyer, text="乘车人")
        self.buyer_name_text.place(x=self.x_entry, y=self.y_entry)
        self.button=self.button_get_buyer_name_info()
        self.add_buyer_input_field()
    def add_buyer_input_field(self):
        self.y_entry+=25
        self.buyer_name_entry = tkinter.Entry(
            self.windows_buyer, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.buyer_name_entry.place(x=self.x_entry, y=self.y_entry)
        self.buyer_input_field_list.append(self.buyer_name_entry)
    def delete_buyer_input_field(self):
        if len(self.buyer_input_field_list)!=1:
            self.y_entry-=25
            self.buyer_input_field_list[len(self.buyer_input_field_list)-1].destroy()
            self.buyer_input_field_list.remove(
                self.buyer_input_field_list[len(self.buyer_input_field_list)-1])
            print(self.buyer_input_field_list)
        else:
            tkinter.messagebox.showerror(title="选择乘车人错误", message="至少需要有一位乘车人")
            buyer_selection(self.computer_info_width, self.computer_info_height, self.file_dir)
            self.is_info_invalid=True
    def get_data(self):
        self.buyers_list=[]
        for buyer_input in self.buyer_input_field_list:
            self.passenger_name=buyer_input.get()
            self.buyers_list.append(self.passenger_name)
            if self.passenger_name==None or len(str(self.passenger_name).lstrip())==0:
                tkinter.messagebox.showerror(title="选择乘车人错误", message="乘车人选择错误")
                buyer_selection(self.computer_info_width, self.computer_info_height, self.file_dir)
                self.is_info_invalid=True
        if self.is_info_invalid==False:
            if not os.path.exists(self.temp_dir):
                os.makedirs(self.temp_dir)
            with open(os.path.join(self.temp_dir, "data_socket_buyer_name_info.log"), "w", encoding="utf-8") as datalog_write:
                datalog_write.write(str(self.buyers_list))
        self.windows_buyer.destroy()
    def button_get_buyer_name_info(self):
        self.button_buyer_sure = tkinter.Button(
            self.windows_buyer, text="确认", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_get_start_time_sure_pack = self.button_buyer_sure.pack(side=tkinter.BOTTOM)
        self.bind_func_sure = self.button_buyer_sure.bind("<Button-1>", lambda event: self.get_data())
        self.button_add_buyer_input_field = tkinter.Button(
            self.windows_buyer, text="增加乘车人", width=10, height=1, font=("Arial", 8, "underline"))
        self.button_add_buyer_pack=self.button_add_buyer_input_field.place(x=0, y=self.windows_choose_buyer_height, anchor="sw")
        self.bind_func_buyer = self.button_add_buyer_input_field.bind("<Button-1>", lambda event: self.add_buyer_input_field())
        self.button_delete_buyer_input_field=tkinter.Button(
            self.windows_buyer, text="减少乘车人", width=10, height=1, font=("Arial", 8, "underline"))
        self.button_delete_buyer_pack=self.button_delete_buyer_input_field.place(
            x=self.windows_choose_buyer_width, y=self.windows_choose_buyer_height, anchor="se")
        self.bind_func_delete_buyer=self.button_delete_buyer_input_field.bind(
            "<Button-1>", lambda event: self.delete_buyer_input_field())


# if __name__=="__main__":
#     buyer_selection(2560, 1600, r"D:\project\python\pythonProject1\Web_Crawler\Analyze_Number\Numers_Analyze_Beta\Analyze_number_mainfile\ticket_12306")
#     tkinter.mainloop()














