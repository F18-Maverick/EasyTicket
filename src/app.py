import tkinter
from get_ticket_interface import Get_ticket_interface
class main_loop:
    def __init__(self):
        self.Main_loop=tkinter.mainloop()
class run_function:
    def __init__(self):
        self.run_get_ticket = Get_ticket_interface()
        self.entry_place = self.run_get_ticket.Entry_Function()
        self.entry_button = self.run_get_ticket.Windows_Button()
        self.Main_Loop = main_loop()





