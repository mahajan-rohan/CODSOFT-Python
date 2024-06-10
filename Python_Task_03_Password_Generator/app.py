from tkinter import *
import pyperclip 
import os
import string
import random

def copyPass():
    password=password_field.get()
    pyperclip.copy(password)

def genPass():
    small_alpha=string.ascii_lowercase
    caps_alpha=string.ascii_uppercase
    num=string.digits
    spec_char = string.punctuation
    all=small_alpha+caps_alpha+num+spec_char
    len=int(len_num.get())

    password=random.sample(all,len)
    password_field.insert(0,password)

window = Tk()
window_width = 400
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
window.resizable(0,0)
window.configure(bg="#F9F5E3")
window.title("Password Generator by Rohan Mahajan")
icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
window.iconbitmap(icon_path)

title_label = Label(window, text="Password Generator", font=("Segoe UI Semibold", 18, "bold"), fg="black",bg="#F9F5E3")
title_label.pack(pady=10)
length_label = Label(window, text="Select Length of Password", font=("Segoe UI Semibold", 14, "bold"), fg="black",bg="#F9F5E3")
length_label.pack(pady=10)

len_num = Spinbox(window,from_=6,to=36,width=5,font=("Segoe UI Semibold", 14, "bold"), fg="black",bg="#CCF5AC")
len_num.pack(pady=10)

gen_button = Button(window, text="Generate Password", fg="white", font=("Segoe UI Semibold", 12),command=genPass,bg="#6B7FD7")
gen_button.pack(pady=5, padx=10)

password_field=Entry(window,width=25,bd=2,font=("Segoe UI Semibold", 14, "bold"), fg="black",bg="#CCF5AC")
password_field.pack(pady=5, padx=10)

copy_button = Button(window, text="Copy Password", fg="black", font=("Segoe UI Semibold", 12),command=copyPass,bg="#DE6B48")
copy_button.pack(pady=5, padx=10)

window.mainloop()