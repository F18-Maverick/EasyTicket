import os
import re
import json
import shutil
import webbrowser
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, filedialog
class AddUnknownBrowserDriverWindow:
    def __init__(self, temp_dir):
        self.temp_dir = temp_dir
        self.window = tk.Toplevel()
        self.window.title("添加未知的驱动和浏览器类型")
        self.window.geometry("600x500")
        self.window.resizable(True, True)
        self.browser_type_var = tk.StringVar()
        self.browser_path_var = tk.StringVar()
        self.driver_path_var = tk.StringVar()
        self.supported_browsers = [
            'chrome', 'firefox', 'edge', 'safari', 'opera',
            'ie', 'chromium', 'brave', 'android', 'ios',
            'phantomjs', 'htmlunit', 'chrome-headless', 'firefox-headless'
        ]
        self.create_widgets()
        self.window.grab_set()
    def create_widgets(self):
        main_frame = tk.Frame(self.window, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        browser_frame = tk.Frame(main_frame)
        browser_frame.pack(fill=tk.X, pady=(0, 15))
        browser_label = tk.Label(
            browser_frame,
            text="添加未知的浏览器类型(具体请参阅selenium官方文档的支持浏览器类型)",
            font=('Arial', 10, 'bold')
        )
        browser_label.pack(anchor=tk.W, pady=(0, 5))
        browser_label.config(fg="blue", cursor="hand2")
        browser_label.bind("<Button-1>", lambda e: self.open_selenium_docs())
        self.browser_entry = tk.Entry(
            browser_frame,
            textvariable=self.browser_type_var,
            font=('Arial', 11),
            width=50
        )
        self.browser_entry.pack(fill=tk.X, ipady=5)
        browser_path_frame = tk.Frame(main_frame)
        browser_path_frame.pack(fill=tk.X, pady=(0, 15))
        browser_path_label = tk.Label(
            browser_path_frame,
            text="输入浏览器路径",
            font=('Arial', 10, 'bold')
        )
        browser_path_label.pack(anchor=tk.W, pady=(0, 5))
        browser_path_input_frame = tk.Frame(browser_path_frame)
        browser_path_input_frame.pack(fill=tk.X)
        self.browser_path_entry = tk.Entry(
            browser_path_input_frame,
            textvariable=self.browser_path_var,
            font=('Arial', 11)
        )
        self.browser_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        browser_path_browse_button = tk.Button(
            browser_path_input_frame,
            text="浏览...",
            command=self.browse_browser_path,
            font=('Arial', 10)
        )
        browser_path_browse_button.pack(side=tk.RIGHT, padx=(10, 0))
        driver_frame = tk.Frame(main_frame)
        driver_frame.pack(fill=tk.X, pady=(0, 15))
        driver_label = tk.Label(
            driver_frame,
            text="添加未知的浏览器对应驱动",
            font=('Arial', 10, 'bold')
        )
        driver_label.pack(anchor=tk.W, pady=(0, 5))
        driver_input_frame = tk.Frame(driver_frame)
        driver_input_frame.pack(fill=tk.X)
        self.driver_entry = tk.Entry(
            driver_input_frame,
            textvariable=self.driver_path_var,
            font=('Arial', 11)
        )
        self.driver_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        browse_button = tk.Button(
            driver_input_frame,
            text="浏览...",
            command=self.browse_driver_file,
            font=('Arial', 10)
        )
        browse_button.pack(side=tk.RIGHT, padx=(10, 0))
        info_frame = tk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=(0, 20))
        info_label = tk.Label(
            info_frame,
            text="支持的浏览器类型示例: " + ", ".join(self.supported_browsers[:5]) + "...",
            font=('Arial', 9),
            fg="gray"
        )
        info_label.pack(anchor=tk.W)
        button_frame = tk.Frame(main_frame)
        button_frame.pack(side=tk.BOTTOM, pady=(20, 0))
        confirm_button = tk.Button(
            button_frame,
            text="确定",
            command=self.on_confirm,
            font=('Arial', 11, 'bold'),
            bg="#4CAF50",
            fg="white",
            padx=30,
            pady=10
        )
        confirm_button.pack()
        self.window.bind('<Return>', lambda event: self.on_confirm())
    def browse_driver_file(self):
        file_path = filedialog.askopenfilename(
            title="选择浏览器驱动文件",
            filetypes=[
                ("可执行文件", "*.exe"),
                ("所有文件", "*.*")
            ]
        )
        if file_path:
            self.driver_path_var.set(file_path)
    def browse_browser_path(self):
        file_path = filedialog.askopenfilename(
            title="选择浏览器可执行文件",
            filetypes=[
                ("可执行文件", "*.exe"),
                ("应用程序", "*.app"),
                ("所有文件", "*.*")
            ]
        )
        if file_path:
            self.browser_path_var.set(file_path)
    def open_selenium_docs(self):
        url = "https://www.selenium.dev/documentation/webdriver/browsers/"
        messagebox.showinfo(
            "Selenium文档",
            "请访问: https://www.selenium.dev/documentation/webdriver/browsers/\n"
            "查看支持的浏览器类型。"
        )
        webbrowser.open_new(url=url)
    def validate_browser_type(self, browser_type):
        if not browser_type or not browser_type.strip():
            return False, "浏览器类型不能为空"
        browser_type = browser_type.strip().lower()
        if not re.match(r'^[a-z0-9_-]+$', browser_type):
            return False, "浏览器类型只能包含字母、数字、连字符和下划线"
        if len(browser_type) < 2 or len(browser_type) > 50:
            return False, "浏览器类型长度应在2-50个字符之间"
        if browser_type in self.supported_browsers:
            return True, f"注意：'{browser_type}'已经是Selenium官方支持的浏览器类型"
        return True, "浏览器类型验证通过"
    def validate_browser_path(self, browser_path):
        if not browser_path or not browser_path.strip():
            return False, "浏览器路径不能为空"
        browser_path = browser_path.strip()
        if not os.path.exists(browser_path):
            return False, "指定的浏览器路径不存在"
        if os.path.isfile(browser_path):
            _, ext = os.path.splitext(browser_path)
            allowed_extensions = ['.exe', '.app', '.bin', '']
            if ext.lower() not in allowed_extensions:
                return False, "浏览器路径应为可执行文件"
        return True, "浏览器路径验证通过"
    def validate_driver_path(self, driver_path):
        if not driver_path or not driver_path.strip():
            return False, "驱动路径不能为空"
        driver_path = driver_path.strip()
        if not os.path.isfile(driver_path):
            return False, "指定的驱动文件不存在"
        file_size = os.path.getsize(driver_path)
        if file_size == 0:
            return False, "驱动文件为空文件"
        _, ext = os.path.splitext(driver_path)
        allowed_extensions = ['.exe', '.bin', '']
        if ext.lower() not in allowed_extensions:
            return False, "驱动文件应为可执行文件（如.exe）"
        return True, "驱动文件验证通过"
    def copy_driver_file(self, source_path):
        try:
            driver_dir = Path.cwd() / "driver"
            driver_dir.mkdir(exist_ok=True)
            file_name = os.path.basename(source_path)
            target_path = driver_dir / file_name
            if target_path.exists():
                response = messagebox.askyesno(
                    "文件已存在",
                    f"文件 '{file_name}' 已存在，是否覆盖？"
                )
                if not response:
                    return None
            shutil.copy2(source_path, target_path)
            return str(target_path)
        except Exception as e:
            messagebox.showerror("复制错误", f"复制文件时出错: {str(e)}")
            return None
    def save_to_log(self, browser_type, browser_path, original_driver_path):
        try:
            log_file = Path(self.temp_dir) / "data_socket_unknown_browser_driver_info.log"
            data = {
                "browser_type": browser_type.strip(),
                "browser_path": browser_path.strip() if browser_path else "",
                "driver_path": original_driver_path,
            }
            if log_file.exists():
                with open(log_file, 'r', encoding='utf-8') as f:
                    try:
                        existing_data = json.load(f)
                        if not isinstance(existing_data, list):
                            existing_data = [existing_data]
                    except json.JSONDecodeError:
                        existing_data = []
            else:
                existing_data = []
            existing_data.append(data)
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            messagebox.showerror("保存错误", f"保存到日志文件时出错: {str(e)}")
            return False
    def on_confirm(self):
        browser_type = self.browser_type_var.get()
        browser_path = self.browser_path_var.get()
        driver_path = self.driver_path_var.get()
        is_valid_browser, browser_msg = self.validate_browser_type(browser_type)
        if not is_valid_browser:
            messagebox.showerror("验证失败", browser_msg)
            self.browser_entry.focus_set()
            return
        is_valid_browser_path, browser_path_msg = self.validate_browser_path(browser_path)
        if not is_valid_browser_path:
            messagebox.showerror("验证失败", browser_path_msg)
            self.browser_path_entry.focus_set()
            return
        is_valid_driver, driver_msg = self.validate_driver_path(driver_path)
        if not is_valid_driver:
            messagebox.showerror("验证失败", driver_msg)
            self.driver_entry.focus_set()
            return
        if "注意" in browser_msg:
            response = messagebox.askyesno("警告", f"{browser_msg}\n\n是否继续添加？")
            if not response:
                return
        copied_path = self.copy_driver_file(driver_path)
        if not copied_path:
            return
        if self.save_to_log(browser_type, browser_path, driver_path):
            messagebox.showinfo(
                "成功",
                f"浏览器类型 '{browser_type}' 和驱动已成功添加！\n"
                f"驱动文件已复制到: {copied_path}"
            )
            self.window.destroy()
        else:
            messagebox.showerror("错误", "保存信息失败")
