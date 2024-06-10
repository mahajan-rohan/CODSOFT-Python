from tkinter import *
from tkinter import messagebox
import random
import os

user_counter = 0
computer_counter = 0
turns = 0

def onclick(user_choice):
    global user_counter, computer_counter, turns

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_counter += 1
    else:
        result = "Computer wins!"
        computer_counter += 1

    turns += 1
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")
    score_label.config(text=f"Score - You: {user_counter}  Computer: {computer_counter}")

    if turns == 3:
        if user_counter > computer_counter:
            final_result = "Congratulations! You won the game!"
            messagebox.showinfo("Results","Congratulations! You won the game!")
        elif user_counter < computer_counter:
            final_result = "Sorry! The computer won the game!"
            messagebox.showinfo("Results","Sorry! The computer won the game!")
        else:
            final_result = "It's a tie game!"
            messagebox.showinfo("Results","It's a tie game!")
        
        result_label.config(text=f"{result_label.cget('text')}\n\n{final_result}")
        resetGame()

def resetGame():
    global user_counter, computer_counter, turns
    user_counter = 0
    computer_counter = 0
    turns = 0
    result_label.config(text="")
    score_label.config(text=f"Score - You: {user_counter}  Computer: {computer_counter}")

window = Tk()
window.title("Rock-Paper-Scissors")
window_width = 400
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
window.resizable(0,0)
icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
window.iconbitmap(icon_path)
window.configure(bg="#FDFFFF")

result_label = Label(window, text="", font=("Segoe UI Semibold", 18), pady=20,bg="white")
result_label.pack()

score_label = Label(window, text="Score - You: 0  Computer: 0", font=("Segoe UI Semibold", 12),bg="white")
score_label.pack()

btn_rock = Button(window, text="Rock", width=15, height=1, command=lambda: onclick("Rock"),font=("Segoe UI Semibold", 18),bg="#B10F2E",fg="white")
btn_rock.pack(pady=10)

btn_paper = Button(window, text="Paper", width=15, height=1, command=lambda: onclick("Paper"),font=("Segoe UI Semibold", 18),bg="#570000",fg="white")
btn_paper.pack(pady=10)

btn_scissors = Button(window, text="Scissors", width=15, height=1, command=lambda: onclick("Scissors"),font=("Segoe UI Semibold", 18),bg="#DE7C5A",fg="white")
btn_scissors.pack(pady=10)

window.mainloop()
