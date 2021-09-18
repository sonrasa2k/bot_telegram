from telethon import TelegramClient,events,sync
import telethon.sync
from telethon.errors import SessionPasswordNeededError
import tkinter as tk
import threading
from tkinter import ttk
from tkinter import filedialog
import asyncio
from get_api import GetApi
from tkinter.messagebox import showerror
import os
# api_id = 6159807
# api_hash = "2fe6bf2795a213854e63c7ac42ba6585"
# phone = "+84947425294"
# client = TelegramClient(phone,
#                                 api_id, api_hash,
#                                 # You may want to use proxy to connect to Telegram
#                                 # proxy=(socks.SOCKS5, 'PROXYHOST', PORT, 'PROXYUSERNAME', 'PROXYPASSWORD')
#                                 )
# client.connect()

client = None
def chuyen_windows():
    global client
    app.destroy()
    app2 = App()
    print(client)
    app2.mainloop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dir = ""
        self.title('Dowload Media From TeleGram')
        self.geometry('680x430')
        self.create_header_frame()

    def monitor(self, thread):
        if thread.is_alive():
            # check the thread every 100ms
            self.after(100, lambda: self.monitor(thread))
        else:
            return 0

    def create_header_frame(self):
        self.header = ttk.Frame(self)
        # configure the grid
        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=10)
        self.header.columnconfigure(2, weight=1)
        # label
        self.label = ttk.Label(self.header, text='Username của User/Channel/Group:')
        self.label.grid(column=0, row=0, sticky=tk.W)
        self.label2 = ttk.Label(self.header, text='Chọn Nơi Lưu Media:')
        self.label2.grid(column=0, row=1, sticky=tk.W)

        #buton choose dir
        self.file_button = ttk.Button(self.header, text='Chọn Thư Mục',command = self.get_dir)
        self.file_button.grid(row = 1,column=1)
        #entry
        self.url_var = tk.StringVar()
        self.url_entry = ttk.Entry(self.header,
                                   textvariable=self.url_var,
                                   width=60)
        self.url_entry.grid(column=1, row=0, sticky=tk.EW)
        #file

        self.download_button = ttk.Button(self.header, text='Tải Media')
        self.download_button['command'] = self.dowload_media
        self.download_button.grid(column=2, row=0, sticky=tk.E)
        self.header.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)
    def get_dir(self):
        self.dir = filedialog.askdirectory()
    def callback(self, current, total):
        text = 'Downloaded', current, 'out of', total,'bytes: {:.2%}'.format(current / total)
        print(text)
        self.bodyss = ttk.Frame(self)
        self.thong_baoss = ttk.Label(self.bodyss,text=text)
        self.thong_baoss.grid(column=0, row=0, sticky=tk.W)
        self.header.grid(column=0, row=3, sticky=tk.NSEW, padx=10, pady=10)
    async def dowload(self,username):
        async with client:
            async for message in client.iter_messages(username):
                if message.media:
                    await client.download_media(message, file=self.dir,progress_callback=self.callback)

    def dowload_media(self):
        if self.dir == "":
            self.dir = "media/"
        username = self.url_var.get()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.dowload(username))

class APP2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dir = ""
        self.title('Dowload Media From TeleGram')
        self.geometry('680x430')
        self.create_header_frame()
    def get_apied(self):
        try:
            code = self.code.get()
            self.api_data = self.apied.get_api(self.random_hash,code)
        except:
            showerror(title='Error',
                      message='Có thể code của bạn sai hoặc sai số điện thoại!')
        with open(self.api_data["phone"]+".txt","w+") as f:
            f.write(self.api_data["phone"]+"\n")
            f.write(self.api_data["api_id"] + "\n")
            f.write(self.api_data["api_hash"])
            f.close()
        self.footer = ttk.Frame(self)
        self.thong_tin = ttk.Label(self.footer, text="Thông Tin API Telegram của Bạn: ")
        self.thong_tin.grid(column=1, row=0, sticky=tk.EW)

        self.label_sdt = ttk.Label(self.footer,text = "Số Điện Thoại: "+str(self.api_data["phone"]))
        self.label_sdt.grid(column=0, row=1, sticky=tk.EW)

        self.api_id = ttk.Label(self.footer, text="Api_id của bạn: " + str(self.api_data["api_id"]))
        self.api_id.grid(column=0, row=2, sticky=tk.EW)

        self.label_api_hash = ttk.Label(self.footer,text = "Api_hash của bạn: "+str(self.api_data["api_hash"]))
        self.label_api_hash.grid(column=0, row=3, sticky=tk.EW)

        self.button_get_media = ttk.Button(self.footer,text = "Đăng Nhập API")
        self.button_get_media["command"] = self.login_apis
        self.button_get_media.grid(column=1, row=4, sticky=tk.EW)
        self.footer.grid(column=0, row=2, sticky=tk.NSEW, padx=10, pady=10)
    def login_api_new(self):
        global client
        code = self.code_apis.get()
        self.client.sign_in(self.api_data["phone"],code=code)
        client = self.client
        self.footer3 = ttk.Frame(self)
        self.label_complete = ttk.Label(self.footer3,text="Bạn đã login api thành công ! Click vào Nút Phía Dưới để dùng phần mềm!")
        self.label_complete.grid(column=0, row=0, sticky=tk.EW)
        self.button_login_apis_new = ttk.Button(self.footer3,text="Sử Dụng Phần Mềm")
        self.button_login_apis_new["command"] = chuyen_windows
        self.button_login_apis_new.grid(column=0, row=1, sticky=tk.EW)
        self.footer3.grid(column=0, row=3, sticky=tk.NSEW, padx=10, pady=10)
    def login_apis(self):
        global client
        self.client = TelegramClient(self.api_data["phone"],self.api_data["api_id"],self.api_data["api_hash"])
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.api_data["phone"])
            self.footer2 = ttk.Frame(self)
            self.label_code = ttk.Label(self.footer2, text="Nhập Mã Code Trên APP Telegram Để Login API:")
            self.label_code.grid(column=0, row=0, sticky=tk.EW)
            self.code_apis = tk.StringVar()
            self.code_apis = tk.Entry(self.footer2,
                                      textvariable=self.code_apis,
                                      width=60)
            self.code_apis.grid(column=1, row=0, sticky=tk.EW)
            self.button_login_apis = ttk.Button(self.footer2, text="Đăng Nhập")
            self.button_login_apis["command"] = self.login_api_new
            self.button_login_apis.grid(column=2, row=0, sticky=tk.E)
            self.footer2.grid(column=0, row=3, sticky=tk.NSEW, padx=10, pady=10)
            return False
        client = self.client
        self.footer3 = ttk.Frame(self)
        self.label_complete = ttk.Label(self.footer3,
                                        text="Bạn đã login api thành công ! Click vào Nút Phía Dưới để dùng phần mềm!")
        self.label_complete.grid(column=0, row=0, sticky=tk.EW)
        self.button_login_apis_new = ttk.Button(self.footer3, text="Sử Dụng Phần Mềm")
        self.button_login_apis_new["command"] = chuyen_windows
        self.button_login_apis_new.grid(column=0, row=1, sticky=tk.EW)
        self.footer3.grid(column=0, row=3, sticky=tk.NSEW, padx=10, pady=10)
    def get_code(self):
        global client
        phone = self.url_var.get()
        list_sessioned = os.listdir()
        name_sessioned = phone+".txt"
        if name_sessioned in list_sessioned:
            with open(name_sessioned,"r") as f:
                data_sessioned = f.readlines()

            self.client = TelegramClient(phone,data_sessioned[1].strip(),data_sessioned[2].strip())
            self.client.connect()
            client = self.client
            self.footer3 = ttk.Frame(self)
            self.label_complete = ttk.Label(self.footer3,
                                            text="Bạn đã login api thành công ! Click vào Nút Phía Dưới để dùng phần mềm!")
            self.label_complete.grid(column=0, row=0, sticky=tk.EW)
            self.button_login_apis_new = ttk.Button(self.footer3, text="Sử Dụng Phần Mềm")
            self.button_login_apis_new["command"] = chuyen_windows
            self.button_login_apis_new.grid(column=0, row=1, sticky=tk.EW)
            self.footer3.grid(column=0, row=3, sticky=tk.NSEW, padx=10, pady=10)
            return True
        self.apied = GetApi(phone)
        try:
            self.random_hash = self.apied.get_random_hash()
        except:
            showerror(title='Error',
                      message='Bạn đã bị khóa api vì login quá nhiều lần!')
            return False
        self.body = ttk.Frame(self)
        self.label1 = ttk.Label(self.body,text = "Nhập Code Để Lấy API: ")
        self.label1.grid(column=0, row=0, sticky=tk.EW)
        self.code = tk.StringVar()
        self.code = ttk.Entry(self.body,
                                   textvariable=self.code,
                                       width=60)
        self.code.grid(column=1, row=0, sticky=tk.EW)
        self.download_login = ttk.Button(self.body, text='Lấy API')
        self.download_login['command'] = self.get_apied
        self.download_login.grid(column=2, row=0, sticky=tk.E)
        self.body.grid(column=0, row=1, sticky=tk.NSEW, padx=10, pady=10)
    def create_header_frame(self):
        self.header = ttk.Frame(self)
        # configure the grid
        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=10)
        self.header.columnconfigure(2, weight=1)
        self.label = ttk.Label(self.header,text = "Nhap So Dien Thoai Telegram cua ban: ")
        self.label.grid(column=0, row=0, sticky=tk.W)
        self.url_var = tk.StringVar()
        self.url_entry = ttk.Entry(self.header,
                                   textvariable=self.url_var,
                                   width=60)
        self.url_entry.grid(column=1, row=0, sticky=tk.EW)
        self.download_button = ttk.Button(self.header, text='Đăng Nhập API')
        self.download_button['command'] = self.get_code
        self.download_button.grid(column=2, row=0, sticky=tk.E)
        self.header.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)

app = APP2()
app.mainloop()
