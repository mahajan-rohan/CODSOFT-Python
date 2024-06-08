
from tkinter import *
from tkinter import filedialog, messagebox
import os

first_num = second_num = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')
    history_label.config(text='')

def get_operator(op):
    global first_num, operator

    if result_label['text']:
        first_num = int(result_label['text'])
        operator = op
        history_label.config(text=f"{first_num} {operator}")
        result_label.config(text='')

def get_ans():
    global first_num, operator, second_num

    if result_label['text']:
        second_num = int(result_label['text'])
        
        if operator == '+':
            result = first_num + second_num
        elif operator == '-':
            result = first_num - second_num
        elif operator == '*':
            result = first_num * second_num
        elif operator == '/':
            if second_num == 0:
                result_label.config(text="Error")
                return
            else:
                result = round(first_num / second_num, 2)
        
        result_label.config(text=str(result))
        history_label.config(text=f"{first_num} {operator} {second_num} = {result}")

window = Tk()
window.title("Calculator App")
window.configure(bg="black")

window_width = 360
window_height = 480
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
window.resizable(0, 0)
window.minsize(360, 480)
icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
window.iconbitmap(icon_path)

history_label = Label(window, text='', bg="black", fg="white")
history_label.grid(row=0, column=0, columnspan=4, pady=(20, 5), sticky='w')
history_label.config(font=("verdana", 12))

result_label = Label(window, text='', bg="black", fg="white")
result_label.grid(row=1, column=0, columnspan=4, pady=(5, 25), sticky='w')
result_label.config(font=("verdana", 30, "bold"))

button_config = {
    'font': ("Helvetica Neue", 20),
    'width': 5,
    'height': 2,
    'relief': FLAT,
    'bd': 0
}

digit_color = "#333333"
operator_color = "#FF9500"
function_color = "#A5A5A5"
text_color = "white"

btn7 = Button(window, text="7", bg=digit_color, fg=text_color, command=lambda: get_digit(7), **button_config)
btn7.grid(row=2, column=0, padx=2, pady=2)

btn8 = Button(window, text="8", bg=digit_color, fg=text_color, command=lambda: get_digit(8), **button_config)
btn8.grid(row=2, column=1, padx=2, pady=2)

btn9 = Button(window, text="9", bg=digit_color, fg=text_color, command=lambda: get_digit(9), **button_config)
btn9.grid(row=2, column=2, padx=2, pady=2)

btn4 = Button(window, text="4", bg=digit_color, fg=text_color, command=lambda: get_digit(4), **button_config)
btn4.grid(row=3, column=0, padx=2, pady=2)

btn5 = Button(window, text="5", bg=digit_color, fg=text_color, command=lambda: get_digit(5), **button_config)
btn5.grid(row=3, column=1, padx=2, pady=2)

btn6 = Button(window, text="6", bg=digit_color, fg=text_color, command=lambda: get_digit(6), **button_config)
btn6.grid(row=3, column=2, padx=2, pady=2)

btn1 = Button(window, text="1", bg=digit_color, fg=text_color, command=lambda: get_digit(1), **button_config)
btn1.grid(row=4, column=0, padx=2, pady=2)

btn2 = Button(window, text="2", bg=digit_color, fg=text_color, command=lambda: get_digit(2), **button_config)
btn2.grid(row=4, column=1, padx=2, pady=2)

btn3 = Button(window, text="3", bg=digit_color, fg=text_color, command=lambda: get_digit(3), **button_config)
btn3.grid(row=4, column=2, padx=2, pady=2)

btn0 = Button(window, text="0", bg=digit_color, fg=text_color, command=lambda: get_digit(0), **button_config)
btn0.grid(row=5, column=1, padx=2, pady=2)

btn_add = Button(window, text="+", bg=operator_color, fg=text_color, command=lambda: get_operator('+'), **button_config)
btn_add.grid(row=2, column=3, padx=2, pady=2)

btn_sub = Button(window, text="-", bg=operator_color, fg=text_color, command=lambda: get_operator('-'), **button_config)
btn_sub.grid(row=3, column=3, padx=2, pady=2)

btn_multi = Button(window, text="*", bg=operator_color, fg=text_color, command=lambda: get_operator('*'), **button_config)
btn_multi.grid(row=4, column=3, padx=2, pady=2)

btn_div = Button(window, text="/", bg=operator_color, fg=text_color, command=lambda: get_operator('/'), **button_config)
btn_div.grid(row=5, column=3, padx=2, pady=2)

btn_clr = Button(window, text="C", bg=function_color, fg="black", command=clear, **button_config)
btn_clr.grid(row=5, column=0, padx=2, pady=2)

btn_ans = Button(window, text="=", bg=operator_color, fg="black", command=get_ans, **button_config)
btn_ans.grid(row=5, column=2, padx=2, pady=2)

window.mainloop()

