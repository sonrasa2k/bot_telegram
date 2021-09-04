from telethon import TelegramClient,events, sync
import tkinter as tk
from threading import Thread
from tkinter import ttk
from tkinter import filedialog
import asyncio
api_id = 4397380
api_hash = "c714283ab4be5fccaa9e1db1956c904a"
phone = "+84838273502"
client = TelegramClient('+84838273502',
                                api_id, api_hash,
                                # You may want to use proxy to connect to Telegram
                                # proxy=(socks.SOCKS5, 'PROXYHOST', PORT, 'PROXYUSERNAME', 'PROXYPASSWORD')
                                )
client.start()
class BackgroundDowload(Thread):
    def __init__(self,username,path_save):
        super().__init__()
        self.username = username
        self.path_save = path_save

    def callback(self,current, total):
        print('Downloaded', current, 'out of', total,
              'bytes: {:.2%}'.format(current / total))
    async def dowloadss(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        async for message in client.iter_messages(self.username):
            await client.download_media(message,file = self.path_save,progress_callback=self.callback)
    def run(self):
        asyncio.run(self.dowloadss())
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
        self.progress = ttk.Progressbar(self.header,orient=tk.HORIZONTAL, length=100, mode='indeterminate')
        self.progress['value'] = int(current/total)
        self.header.update_idletasks()
    def dowload_media(self):
        if self.dir == "":
            self.dir = "media/"
        username = self.url_var.get()
        print(username)
        if username:
            self.download_button['state'] = tk.DISABLED
            download_thread = BackgroundDowload(username,self.dir)
            download_thread.start()
            self.monitor(download_thread)

if __name__ == "__main__":
    app = App()
    app.mainloop()










# api_id = 4397380
# api_hash= "c714283ab4be5fccaa9e1db1956c904a"
# phone = "+84838273502"
# # #logging.basicConfig(level=logging.DEBUG)
# #
# #
# #
# #
# #
# client = TelegramClient('+84838273502',
#     api_id, api_hash,
#     # You may want to use proxy to connect to Telegram
#     #proxy=(socks.SOCKS5, 'PROXYHOST', PORT, 'PROXYUSERNAME', 'PROXYPASSWORD')
# )
# client.start()
# def callback(current, total):
#     print('Downloaded', current, 'out of', total,
#           'bytes: {:.2%}'.format(current / total))
# for message in client.iter_messages('son_dz2k_bot'):
#     client.download_media(message,progress_callback=callback)