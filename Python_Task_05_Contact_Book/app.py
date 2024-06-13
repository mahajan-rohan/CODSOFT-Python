from tkinter import *
from tkinter import  messagebox
import os,json

def view_contact_list():
    view_contact_window = Toplevel(window)
    view_contact_window.title("View Contact List")
    view_contact_window.config(bg="#D0EFB1")
    window_width = 500
    window_height = 500  
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    view_contact_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    view_contact_window.minsize(420, 430)
    view_contact_window.attributes('-topmost', True)
    icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
    view_contact_window.iconbitmap(icon_path)

    contact_list = Listbox(view_contact_window, font=("Segoe UI SemiBold",16),height=10, selectmode=NONE,bg="#D0EFB1")
    contact_list.pack(fill=BOTH, expand=True, padx=10, pady=10)

    try:
        filepath = os.path.join(os.path.dirname(__file__), "contacts.json")
        with open(filepath, "r") as f:
            data = json.load(f)
            for contacts in data:
                contact_list.insert(0, contacts["name"]+" : "+contacts["number"])
    except FileNotFoundError:
        pass

    close_button = Button(view_contact_window, text="Close", font=("Segoe UI Semibold", 16), bg="#E58F65", command=view_contact_window.destroy)
    close_button.pack(side=RIGHT,padx=10, pady=5)

def update_contact():
    update_contact_window = Toplevel(window)
    update_contact_window.title("Update Contact")
    update_contact_window.config(bg="#D0EFB1")
    window_width = 500
    window_height = 500  
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    update_contact_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    update_contact_window.minsize(420, 430)
    update_contact_window.attributes('-topmost', True)
    icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
    update_contact_window.iconbitmap(icon_path)

    label = Label(update_contact_window, text="Update Contact", font=("Segoe UI SemiBold", 18), bg="#D0EFB1")
    label.pack(pady=20)

    def clear_placeholder(event):
        widget = event.widget
        if widget.get() in ["Enter Contact Name", "Enter Contact Number", "Enter New Contact Number"]:
            widget.delete(0, END)

    def restore_placeholder(event):
        widget = event.widget
        if widget.get() == "":
            if widget == update_contact_window.contact_name_inp:
                widget.insert(0, "Enter Contact Name")
            elif widget == update_contact_window.contact_number_inp:
                widget.insert(0, "Enter Contact Number")
            elif widget == update_contact_window.new_contact_name_inp:
                widget.insert(0, "Enter New Contact Number")

    def find_contact():
        contact_name = update_contact_window.contact_name_inp.get()

        if contact_name == "" or contact_name == "Enter Contact Name":
            messagebox.showinfo("Input Error", "Please enter a contact name to update.", parent=update_contact_window)
            return

        filepath = os.path.join(os.path.dirname(__file__), "contacts.json")

        if os.path.exists(filepath):
            try:
                with open(filepath, "r") as f:
                    contacts = json.load(f)
            except json.JSONDecodeError:
                messagebox.showinfo("Error", "The contacts file is empty or corrupted.", parent=update_contact_window)
                return

            contact_found = False
            for contact in contacts:
                if contact["name"] == contact_name:
                    contact_found = True
                    display_label.config(text=f"Contact Name: {contact['name']}\nContact Number: {contact['number']}")
                    break

            if not contact_found:
                messagebox.showinfo("Error", "Contact not found.", parent=update_contact_window)
        else:
            messagebox.showinfo("Error", "The contacts file does not exist.", parent=update_contact_window)

    def update_contact_info():
        new_contact_number = update_contact_window.new_contact_name_inp.get()
        contact_name = update_contact_window.contact_name_inp.get()

        if new_contact_number == "" or new_contact_number == "Enter New Contact Number":
            messagebox.showinfo("Input Error", "Please enter a new contact number.", parent=update_contact_window)
            return

        filepath = os.path.join(os.path.dirname(__file__), "contacts.json")

        if os.path.exists(filepath):
            try:
                with open(filepath, "r") as f:
                    contacts = json.load(f)
            except json.JSONDecodeError:
                messagebox.showinfo("Error", "The contacts file is empty or corrupted.", parent=update_contact_window)
                return

            for contact in contacts:
                if contact["name"] == contact_name:
                    contact["number"] = new_contact_number
                    with open(filepath, "w") as f:
                        json.dump(contacts, f, indent=4)
                    messagebox.showinfo("Success", "Contact updated successfully!", parent=update_contact_window)
                    return

            messagebox.showinfo("Error", "Contact not found.", parent=update_contact_window)
        else:
            messagebox.showinfo("Error", "The contacts file does not exist.", parent=update_contact_window)

    update_contact_window.contact_name_inp = Entry(update_contact_window, font=("Segoe UI Semibold", 16), width=30,bg="#7EB2DD")
    update_contact_window.contact_name_inp.pack(pady=10)
    update_contact_window.contact_name_inp.insert(0, "Enter Contact Name")
    update_contact_window.contact_name_inp.bind("<FocusIn>", clear_placeholder)
    update_contact_window.contact_name_inp.bind("<FocusOut>", restore_placeholder)

    search_button = Button(update_contact_window, text="Search Contact", font=("Segoe UI Semibold", 16),bg="#E58F65", command=find_contact)
    search_button.pack(side=TOP, padx=25, pady=10)

    display_label = Label(update_contact_window, text="", font=("Segoe UI Semibold", 18), pady=20, bg="#D0EFB1")
    display_label.pack(pady=5)

    update_contact_window.new_contact_name_inp = Entry(update_contact_window, font=("Segoe UI Semibold", 16), width=30,bg="#7EB2DD")
    update_contact_window.new_contact_name_inp.pack(pady=10)
    update_contact_window.new_contact_name_inp.insert(0, "Enter New Contact Number")
    update_contact_window.new_contact_name_inp.bind("<FocusIn>", clear_placeholder)
    update_contact_window.new_contact_name_inp.bind("<FocusOut>", restore_placeholder)

    update_button = Button(update_contact_window, text="Update Contact", font=("Segoe UI Semibold", 16),bg="#E58F65", command=update_contact_info)
    update_button.pack(side=TOP, padx=25, pady=10)

    close_button = Button(update_contact_window, text="Close", font=("Segoe UI Semibold", 16),bg="#E58F65", command=update_contact_window.destroy)
    close_button.pack(side=RIGHT, padx=50, pady=10)


def search_contact():
    search_contact_window = Toplevel(window)
    search_contact_window.title("Search Contact")
    search_contact_window.config(bg="#D0EFB1")
    window_width = 500
    window_height = 500  
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    search_contact_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    search_contact_window.minsize(420, 430)
    search_contact_window.attributes('-topmost', True)
    icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
    search_contact_window.iconbitmap(icon_path)

    label = Label(search_contact_window, text="Search Contact", font=("Segoe UI SemiBold", 18), bg="#D0EFB1")
    label.pack(pady=20)

    def clear_placeholder(event):
        widget = event.widget
        if widget.get() == "Enter Contact Name" or widget.get() == "Enter Contact Number":
            widget.delete(0, END)

    def restore_placeholder(event):
        widget = event.widget
        if widget.get() == "":
            if widget == search_contact_window.contact_name_inp:
                widget.insert(0, "Enter Contact Name")
            elif widget == search_contact_window.contact_number_inp:
                widget.insert(0, "Enter Contact Number")

    search_contact_window.contact_name_inp = Entry(search_contact_window, font=("Segoe UI Semibold", 16), width=30,bg="#7EB2DD")
    search_contact_window.contact_name_inp.pack(pady=10)
    search_contact_window.contact_name_inp.insert(0, "Enter Contact Name")
    search_contact_window.contact_name_inp.bind("<FocusIn>", clear_placeholder)
    search_contact_window.contact_name_inp.bind("<FocusOut>", restore_placeholder)

    display_label = Label(search_contact_window, text="", font=("Segoe UI Semibold", 18), pady=20, bg="#D0EFB1")
    display_label.pack()
    def find_contact():
        contact_name = search_contact_window.contact_name_inp.get()

        if contact_name == "" or contact_name == "Enter Contact Name":
            messagebox.showinfo("Input Error", "Please enter a contact name to search.", parent=search_contact_window)
            return

        filepath = os.path.join(os.path.dirname(__file__), "contacts.json")

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                contacts = json.load(f)

            contact_found = False
            for contact in contacts:
                if contact["name"] == contact_name:
                    contact_found = True
                    display_label.config(text=f"Contact Name : {contact['name']}\nContact Number : {contact['number']}")
                    break

            if not contact_found:
                messagebox.showinfo("Error", "Contact not found.", parent=search_contact_window)

    search_button = Button(search_contact_window, text="Search Contact", font=("Segoe UI Semibold", 16), bg="#E58F65", command=find_contact)
    search_button.pack(side=LEFT,padx=10, pady=0)

    close_button = Button(search_contact_window, text="Close", font=("Segoe UI Semibold", 16), bg="#E58F65", command=search_contact_window.destroy)
    close_button.pack(side=RIGHT,padx=10, pady=0)


def delete_contact():
    delete_contact_window = Toplevel(window)
    delete_contact_window.title("Delete Contact")
    delete_contact_window.config(bg="#D0EFB1")
    window_width = 500
    window_height = 500  
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    delete_contact_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    delete_contact_window.minsize(420, 430)
    delete_contact_window.attributes('-topmost', True)
    icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
    delete_contact_window.iconbitmap(icon_path)

    label = Label(delete_contact_window, text="Delete Contact", font=("Segoe UI SemiBold", 18), bg="#D0EFB1")
    label.pack(pady=30)

    def clear_placeholder(event):
        widget = event.widget
        if widget.get() == "Enter Contact Name" or widget.get() == "Enter Contact Number":
            widget.delete(0, END)

    def restore_placeholder(event):
        widget = event.widget
        if widget.get() == "":
            if widget == delete_contact_window.contact_name_inp:
                widget.insert(0, "Enter Contact Name")
            elif widget == delete_contact_window.contact_number_inp:
                widget.insert(0, "Enter Contact Number")

    delete_contact_window.contact_name_inp = Entry(delete_contact_window, font=("Segoe UI Semibold", 16), width=30,bg="#7EB2DD")
    delete_contact_window.contact_name_inp.pack(pady=15)
    delete_contact_window.contact_name_inp.insert(0, "Enter Contact Name")
    delete_contact_window.contact_name_inp.bind("<FocusIn>", clear_placeholder)
    delete_contact_window.contact_name_inp.bind("<FocusOut>", restore_placeholder)

    label = Label(delete_contact_window, text="OR", font=("Segoe UI SemiBold", 18), bg="#D0EFB1", width=30)
    label.pack(pady=15)

    delete_contact_window.contact_number_inp = Entry(delete_contact_window, font=("Segoe UI Semibold", 16), width=30,bg="#7EB2DD")
    delete_contact_window.contact_number_inp.pack(pady=15)
    delete_contact_window.contact_number_inp.insert(0, "Enter Contact Number")
    delete_contact_window.contact_number_inp.bind("<FocusIn>", clear_placeholder)
    delete_contact_window.contact_number_inp.bind("<FocusOut>", restore_placeholder)

    def del_contact():
        contact_name = delete_contact_window.contact_name_inp.get()
        contact_number = delete_contact_window.contact_number_inp.get()

        if (contact_name == "" or contact_name == "Enter Contact Name") and (contact_number == "" or contact_number == "Enter Contact Number"):
            messagebox.showinfo("Input Error", "Please enter a contact name or number to delete.", parent=delete_contact_window)
            return

        filepath = os.path.join(os.path.dirname(__file__), "contacts.json")

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                contacts = json.load(f)
        else:
            contacts = []

        updated_contacts = []
        contact_found = False
        for contact in contacts:
            if contact["name"] == contact_name or contact["number"] == contact_number:
                contact_found = True
            else:
                updated_contacts.append(contact)

        with open(filepath, "w") as f:
            json.dump(updated_contacts, f)

        if contact_found:
            messagebox.showinfo("Success", "Contact deleted successfully!", parent=delete_contact_window)
        else:
            messagebox.showinfo("Error", "Contact not found.", parent=delete_contact_window)

        delete_contact_window.destroy()

    delete_button = Button(delete_contact_window, text="Delete Contact", font=("Segoe UI Semibold", 16), bg="#E58F65", command=del_contact)
    delete_button.pack(pady=20)

    close_button = Button(delete_contact_window, text="Close", font=("Segoe UI Semibold", 16), bg="#E58F65", command=delete_contact_window.destroy)
    close_button.pack(pady=20)

def add_contact():
    add_contact_window = Toplevel(window)
    add_contact_window.title("Add Contact")
    add_contact_window.config(bg="#D0EFB1")
    window_width = 500
    window_height = 500  
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    add_contact_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    add_contact_window.minsize(420, 430)
    add_contact_window.attributes('-topmost', True)
    icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
    add_contact_window.iconbitmap(icon_path)

    label = Label(add_contact_window, text="Add Contact", font=("Segoe UI SemiBold", 18),bg="#D0EFB1")
    label.pack(pady=30)

    def clear_placeholder(event):
        widget = event.widget
        if widget.get() == "Enter Contact Name" or widget.get() == "Enter Contact Number":
            widget.delete(0, END)

    def restore_placeholder(event):
        widget = event.widget
        if widget.get() == "":
            if widget == add_contact_window.contact_name_inp:
                widget.insert(0, "Enter Contact Name")
            elif widget == add_contact_window.contact_number_inp:
                widget.insert(0, "Enter Contact Number")

    add_contact_window.contact_name_inp = Entry(add_contact_window, font=("Segoe UI Semibold", 16), width=30,bg="#7EB2DD")
    add_contact_window.contact_name_inp.pack(pady=20)
    add_contact_window.contact_name_inp.insert(0, "Enter Contact Name")
    add_contact_window.contact_name_inp.bind("<FocusIn>", clear_placeholder)
    add_contact_window.contact_name_inp.bind("<FocusOut>", restore_placeholder)

    add_contact_window.contact_number_inp = Entry(add_contact_window, font=("Segoe UI Semibold", 16), width=30,bg="#7EB2DD")
    add_contact_window.contact_number_inp.pack(pady=20)
    add_contact_window.contact_number_inp.insert(0, "Enter Contact Number")
    add_contact_window.contact_number_inp.bind("<FocusIn>", clear_placeholder)
    add_contact_window.contact_number_inp.bind("<FocusOut>", restore_placeholder)

    def save_contact():
        contact_name = add_contact_window.contact_name_inp.get()
        contact_number = add_contact_window.contact_number_inp.get()

        if contact_name == "" or contact_name == "Enter Contact Name":
            messagebox.showinfo("Input Error", "Please enter a contact name to add.", parent=add_contact_window)
        elif contact_number == "" or contact_number == "Enter Contact Number":
            messagebox.showinfo("Input Error", "Please enter a contact number to add.", parent=add_contact_window)
        elif len(contact_number) != 10 or not contact_number.isdigit():
            messagebox.showinfo("Input Error", "Please enter a valid 10-digit contact number.", parent=add_contact_window)
        else:
            filepath = os.path.join(os.path.dirname(__file__), "contacts.json")
            if os.path.exists(filepath):
                with open(filepath, "r") as f:
                    contacts = json.load(f)
            else:
                contacts = []

            contacts.append({"name": contact_name, "number": contact_number})
            with open(filepath, "w") as f:
                json.dump(contacts, f)

            messagebox.showinfo("Success", "Contact added successfully!", parent=add_contact_window)
            add_contact_window.destroy()

    add_button = Button(add_contact_window, text="Add Contact", font=("Segoe UI Semibold", 16),bg="#E58F65", command=save_contact)
    add_button.pack(pady=30)

    close_button = Button(add_contact_window, text="Close", font=("Segoe UI Semibold", 16),bg="#E58F65", command=add_contact_window.destroy)
    close_button.pack(pady=30)


if __name__ == "__main__":
    window = Tk()
    window.title("Contact Book")

    window_width = 500
    window_height = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    window.minsize(420, 430)
    window.config(bg="#D0EFB1")

    icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
    window.iconbitmap(icon_path)

    title = Label(window, text="Rohan's Contact Book", font=("Segoe UI Semibold", 18, "bold"), fg="black", bg="#D0EFB1")
    title.pack(pady=25)

    btn_add = Button(window, text="Add to Contact", font=("Segoe UI Semibold", 14), command=add_contact,bg="#AB92BF")
    btn_add.pack(pady=5)

    btn_add = Button(window, text="View Contact List", font=("Segoe UI Semibold", 14), command=view_contact_list,bg="#AB92BF")
    btn_add.pack(pady=5)

    btn_add = Button(window, text="Search Contact", font=("Segoe UI Semibold", 14), command=search_contact,bg="#AB92BF")
    btn_add.pack(pady=5)

    btn_add = Button(window, text="Update Contact", font=("Segoe UI Semibold", 14), command=update_contact,bg="#AB92BF")
    btn_add.pack(pady=5)

    btn_add = Button(window, text="Delete Contact", font=("Segoe UI Semibold", 14), command=delete_contact,bg="#AB92BF")
    btn_add.pack(pady=5)

    btn_add = Button(window, text="Close", font=("Segoe UI Semibold", 14), command=window.destroy,bg="#AB92BF")
    btn_add.pack(pady=5)

    window.mainloop()