import tkinter as tk
from tkinter import ttk,messagebox
from ttkbootstrap import Style
import json,os

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do-List App by Rohan Mahajan")

        window_width = 500
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.minsize(420,430)
        style = Style(theme="flatly")
        style.configure("Custon.TEntry",foreground="gray")
        icon_path = "D:\\Coding_Playground\\Python_Projects\\To-Do-List\\icon.png" 
        self.icon_image = tk.PhotoImage(file=icon_path)
        self.iconphoto(False, self.icon_image)

        self.task_input = ttk.Entry(self, font =(
            "TkDefaultFont",16),width=40, style="Custon.TEntry")
        self.task_input.pack(pady=10)

        self.task_input.insert(0,"Enter task...")

        self.task_input.bind("<FocusIn>",self.clear_placeholder)
        self.task_input.bind("<FocusOut>",self.restore_placeholder)

        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        self.task_list = tk.Listbox(self, font=(
            "TkDefaultFont",16),height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Button(self, text="Done", style="success.TButton", command=self.task_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)

        ttk.Button(self, text="View Stats", style="info.TButton", command=self.view_statistics).pack(side=tk.BOTTOM, pady=10)

        self.load_tasks()

    def view_statistics(self):
        done_count=0;
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count+=1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted Tasks: {done_count} ")

    def add_task(self):
        task = self.task_input.get()
        if task == "" or task == "Enter task...":
            messagebox.showinfo("Input Error", "Please enter a task to add.")
        else:
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="red")
            self.task_input.delete(0, tk.END)
            self.save_tasks()


    def task_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()

    def delete_task(self):
        if self.task_list.size() == 0:
            messagebox.showinfo("Task List Empty", "The task list is empty.")
        else:
            task_index = self.task_list.curselection()
            if not task_index:
                messagebox.showinfo("No Task Selected", "Please select a task to delete.")
            else:
                self.task_list.delete(task_index)
                self.save_tasks()

    
    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter task...":
            self.task_input.delete(0, tk.END)
            self.task_input.configure(style="TEntry")

    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0,"Enter task...")
            self.task_input.configure(style="Custom.TEntry")

    def load_tasks(self):
        try:
            filepath = os.path.join(os.path.dirname(__file__), "tasks.json")
            with open(filepath, "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert(tk.END, task["text"])
                    self.task_list.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass

    def save_tasks(self):
        data = []
        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        filepath = os.path.join(os.path.dirname(__file__), "tasks.json")
        with open(filepath, "w") as f:
            json.dump(data, f)


if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()


