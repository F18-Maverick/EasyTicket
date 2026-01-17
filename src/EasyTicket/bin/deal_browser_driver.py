import os
import time
import shutil
import subprocess
from tkinter import font
import tkinter.messagebox
class check_browsers_drivers_error:
    def __init__(self, browser_dir_list, driver_list, screen_width, screen_height, temp_dir):
        self.show_info_UI=None
        self.error_deal_result=None
        self.temp_dir=temp_dir
        self.show_info_UI=None
        self.driver_executable_dir=os.path.join(
                    os.path.dirname(
                        os.path.abspath(__file__)), "driver")
        self.browser_copy_dir=os.path.join(
                    self.driver_executable_dir, "browser")
        self.is_version_same=None
        self.deal_error_window_width=600
        self.deal_error_window_height=600
        self.screen_width=screen_width
        self.screen_height=screen_height
        self.deal_error_window_x = int((self.screen_width - self.deal_error_window_width) / 2)
        self.deal_error_window_y = int((self.screen_height - self.deal_error_window_height) / 2)
        self.browsers_dir_list=browser_dir_list
        self.driver_list=driver_list
        self.driver_version=None
        self.browser_version=None
    def deal_result_record(self, deal_result):
        self.deal_result=deal_result
        self.result_record_file_name="data_socket_error_deal_result.log"
        self.record_result_file_dir=os.path.join(
            self.temp_dir, self.result_record_file_name)
        with open(self.record_result_file_dir, "w", encoding="utf-8") as result_record_file:
            result_record_file.write(str(self.deal_result))
        self.show_info_UI.destroy()
    def show_info_window(self):
        if len(self.browsers_dir_list)!=0:
            for each_browser_index in range(len(self.browsers_dir_list)):
                if self.error_deal_result==True:
                    break
                self.error_deal_result=None
                self.driver_executable_name=self.driver_list[each_browser_index]
                self.driver_executable_path=os.path.join(
                        self.driver_executable_dir, self.driver_executable_name)
                self.browser_executable_path=self.browsers_dir_list[each_browser_index]
                self.browser_dirname=os.path.dirname(self.browser_executable_path)
                try:
                    self.driver_version=self.check_version(
                        self.driver_executable_path)
                    self.browser_version=self.check_version(
                        self.browser_executable_path)
                except:
                    tkinter.messagebox.showerror("错误", "缺失浏览器或驱动程序")
                self.showinfo=(
                    "驱动器版本: {}\n\n浏览器版本: {}\n\n请确认驱动器版本与浏览器版本是否相匹配".format(
                        self.driver_version, self.browser_version))
                self.show_info_UI=tkinter.Toplevel()
                self.text_font=font.Font(family="微软雅黑", size=10)
                self.deal_error_window_position_str = "{}x{}+{}+{}".format(
                    self.deal_error_window_width, self.deal_error_window_height, 
                    self.deal_error_window_x, self.deal_error_window_y)
                self.show_info_UI.geometry(self.deal_error_window_position_str)
                self.show_info_label=tkinter.Label(
                    self.show_info_UI, text=self.showinfo, font=self.text_font)
                self.show_info_label.pack(side=tkinter.TOP)
                self.button_version_same = tkinter.Button(
                    self.show_info_UI, text="版本一致", width=8, 
                    height=1, font=("Arial", 8, "underline"))
                self.x = (
                    int((self.deal_error_window_width + 60)/4))
                self.y = self.deal_error_window_height-30
                self.button_version_same.place(x=self.x, y=self.y, anchor="ne")
                self.run_version_same = self.button_version_same.bind(
                    "<Button-1>", lambda event: self.version_same_func(
                        self.browser_dirname, self.browser_copy_dir))
                self.button_version_unsame = tkinter.Button(
                    self.show_info_UI, text="版本不一致", width=8, 
                    height=1, font=("Arial", 8, "underline"))
                self.x = (
                    int((self.deal_error_window_width + 60)/4*3))
                self.y = self.deal_error_window_height-30
                self.button_version_unsame.place(x=self.x, y=self.y, anchor="ne")
                self.run_version_unsame = self.button_version_unsame.bind(
                    "<Button-1>", lambda event: self.version_unsame_func(self.driver_executable_dir))
                while True:
                    time.sleep(0.5)
                    if (self.error_deal_result==False or 
                        self.error_deal_result==True or 
                        self.show_info_UI.winfo_exists()!=True):
                        break
            self.deal_result_record(self.error_deal_result)
        else:
            tkinter.messagebox.showinfo(
                title="浏览器错误", 
                message="未安装浏览器")
    def check_version(self, executable_path, version_flag="--version"):
        try:
            self.result = subprocess.run(
                [executable_path, version_flag],
                capture_output=True,
                text=True,
                check=True
            )
            self.version=self.result.stdout.strip()
            return self.version
        except subprocess.CalledProcessError as e:
            print(f"错误: {e}")
            self.error_deal_result=False
            self.show_info_UI.destroy()
            return False
        except FileNotFoundError:
            print(f"未找到可执行文件: {executable_path}")
            pass
    def version_same_func(self, src_dir, dst_dir):
        self.show_info_UI.destroy()
        if not os.path.exists(src_dir):
            print(f"错误: 源目录 '{src_dir}' 不存在")
            self.error_deal_result=False
            self.show_info_UI.destroy()
            return False
        if not os.path.isdir(src_dir):
            print(f"错误: '{src_dir}' 不是一个目录")
            self.error_deal_result=False
            self.show_info_UI.destroy()
            return False
        try:
            os.makedirs(dst_dir, exist_ok=True)
            for filename in os.listdir(dst_dir):
                file_path = os.path.join(dst_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        print(f"已删除文件: {file_path}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"已删除目录: {file_path}")
                except Exception as e:
                    tkinter.messagebox.showerror(
                        title="无法解决错误", message=f"删除 {file_path} 时出错: {e}")
                    self.error_deal_result=False
                    self.show_info_UI.destroy()
                    return False
            print("开始复制文件...")
            for filename in os.listdir(src_dir):
                src_path = os.path.join(src_dir, filename)
                dst_path = os.path.join(dst_dir, filename)
                try:
                    if os.path.isfile(src_path):
                        shutil.copy2(src_path, dst_path)
                        current_file_path=os.path.join(dst_dir, filename)
                        try:
                            os.chmod(current_file_path, 0o775)
                        except:
                            tkinter.messagebox.showerror(
                                title="权限错误", message="无法更改权限")
                            self.error_deal_result=False
                            self.show_info_UI.destroy()
                            return False
                        print(f"复制文件: {filename}")
                    elif os.path.isdir(src_path):
                        shutil.copytree(src_path, dst_path)
                        current_file_path=os.path.join(dst_dir, filename)
                        try:
                            os.chmod(current_file_path, 0o775)
                        except:
                            tkinter.messagebox.showerror(
                                title="权限错误", message="无法更改权限")
                            self.error_deal_result=False
                            self.show_info_UI.destroy()
                            return False
                        print(f"复制目录: {filename}")
                except Exception as e:
                    tkinter.messagebox.showerror(
                        title="无法解决错误", message=f"复制 {src_path} 时出错: {e}")
                    self.error_deal_result=False
                    self.show_info_UI.destroy()
                    return False
            print(f"成功复制所有文件从 '{src_dir}' 到 '{dst_dir}'")
            self.is_version_same=True
            self.error_deal_result=True
            return True
        except Exception as e:
            tkinter.messagebox.showerror(
                title="无法解决错误", message=f"操作过程中出错: {e}")
            self.error_deal_result=False
            self.show_info_UI.destroy()
            return False
    def version_unsame_func(self, target_folder):
        root = tkinter.Toplevel()
        root.title("修改浏览器驱动")
        root.geometry("400x150")
        file_label = tkinter.Label(root, text="输入文件路径:")
        file_label.pack()
        file_entry = tkinter.Entry(root, width=40)
        file_entry.pack(pady=5)
        def copy_file():
            source_path = file_entry.get().strip()
            if not source_path:
                tkinter.messagebox.showerror("错误", "请输入文件路径！")
                self.error_deal_result=False
                root.destroy()
                self.show_info_UI.destroy()
                return False
            elif not os.path.exists(source_path):
                tkinter.messagebox.showerror("错误", "文件不存在！")
                self.error_deal_result=False
                root.destroy()
                self.show_info_UI.destroy()
                return False
            elif os.path.isdir(source_path):
                tkinter.messagebox.showerror("错误", "不支持复制文件夹！")
                self.error_deal_result=False
                root.destroy()
                self.show_info_UI.destroy()
                return False
            try:
                filename = os.path.basename(source_path)
                destination = os.path.join(target_folder, filename)
                shutil.copy2(source_path, destination)
                os.chmod(destination, 0o775)
                tkinter.messagebox.showinfo("成功", f"文件已复制到:\n{destination}")
                root.destroy()
                self.error_deal_result=True
                root.destroy()
                self.show_info_UI.destroy()
                return True
            except Exception as e:
                tkinter.messagebox.showerror("错误", f"复制失败: {str(e)}")
                self.error_deal_result=False
                root.destroy()
                self.show_info_UI.destroy()
                return False
        copy_btn = tkinter.Button(root, text="复制文件", command=copy_file, width=15)
        copy_btn.pack(pady=10)
