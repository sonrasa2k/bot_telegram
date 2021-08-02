import tkinter as tk
from tkinter import StringVar
#Khai báo màn hình và set up màn hình
window = tk.Tk()
window.title("hello")
window.geometry("500x300")
#Các chức năng

hoten = StringVar()
hoten.set('')
ho_ten = tk.Label(textvariable=hoten)
def get_ten():
    global ho_ten
    ten = nhap_ten.get()
    ho = nhap_ho.get()
    hoten.set(ho + ten)
nhap_ten_label = tk.Label(text="Nhap Ten Cua Ban: ")
nhap_ten = tk.Entry()
nhap_ho_label = tk.Label(text="Nhap Ho Cua Ban: ")
nhap_ho = tk.Entry()

nut = tk.Button(text="Gửi",command=get_ten)

#hiển thị chức năng
nhap_ten_label.pack()
nhap_ten.pack()
nhap_ho_label.pack()
nhap_ho.pack()
nut.pack()
ho_ten.pack()

#Cho màn hình lặp đi lặp lại
window.mainloop()
