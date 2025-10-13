import threading
from bin import get_ticket_info
from choose_start_time_UI import choose_start_time
from choose_end_station_UI import choose_end_station
from choose_start_station_UI import choose_start_station
from bin.sign_in_UI import sign_in
class thread_all:
    def choose_start_station_UI_thread(self, computer_width, computer_height):
        self.thread_choose_UI=threading.Thread(target=choose_start_station, args=(computer_width, computer_height),
                                               name="thread1", daemon=True)
        self.thread_choose_UI_start=self.thread_choose_UI.start()
    def choose_end_station_UI_thread(self, computer_width, computer_height):
        self.thread_choose_UI=threading.Thread(target=choose_end_station, args=(computer_width, computer_height),
                                               name="thread2", daemon=True)
        self.thread_choose_UI_end=self.thread_choose_UI.start()
    def choose_start_time_UI_thread(self, computer_width, computer_height):
        self.thread_choose_UI=threading.Thread(target=choose_start_time, args=(computer_width, computer_height),
                                               name="thread3", daemon=True)
        self.thread_choose_UI_date=self.thread_choose_UI.start()
    def user_sign_in_UI_thread(self, computer_width, computer_high, file_dir):
        self.thread_sign_in_UI=threading.Thread(target=sign_in, args=(computer_width, computer_high, file_dir),
                                         name="thread5", daemon=True)
        self.thread_sign_in_UI=self.thread_sign_in_UI.start()
    def download_ticket_station_info_thread(self, computer_height, computer_width):
        self.thread_station_info=threading.Thread(
            target=get_ticket_info.get_ticket_station_info, args=(computer_height, computer_width),
            name="thread4", daemon=True)
        self.thread_station_name=self.thread_station_info.start()












