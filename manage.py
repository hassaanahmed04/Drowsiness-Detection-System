import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def load_data():
    try:
        connection = sqlite3.connect("Database/AccountSystem.db")
        cur = connection.cursor()
        cur.execute("SELECT * FROM AccountDB")
        data = cur.fetchall()
        connection.close()
        return data
    except Exception as e:
        messagebox.showerror("Error", "Failed to fetch data from the database")
        return []

def modify_selected():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        values = item["values"]

        modify_window = tk.Toplevel(root)
        modify_window.title("Modify User")

        first_name_label = tk.Label(modify_window, text="First Name:")
        first_name_label.grid(row=0, column=0)
        first_name_entry = tk.Entry(modify_window)
        first_name_entry.grid(row=0, column=1)
        first_name_entry.insert(0, values[1])

        Last_label = tk.Label(modify_window, text="Last Name:")
        Last_label.grid(row=1, column=0)
        Last_entry = tk.Entry(modify_window)
        Last_entry.grid(row=1, column=1)
        Last_entry.insert(0, values[2])

        email_label = tk.Label(modify_window, text="Email:")
        email_label.grid(row=2, column=0)
        email_entry = tk.Entry(modify_window)
        email_entry.grid(row=2, column=1)
        email_entry.insert(0, values[3])

        def save_changes():
            new_first_name = first_name_entry.get()
            new_last = Last_entry.get()
            new_email = email_entry.get()
            if new_first_name and new_email:
                try:
                    connection = sqlite3.connect("Database/AccountSystem.db")
                    cur = connection.cursor()
                    cur.execute("UPDATE AccountDB SET FirstName=?, LastName=?, Email=? WHERE Email=?", (new_first_name, new_last, new_email, values[3]))
                    connection.commit()
                    connection.close()
                    modify_window.destroy()
                    refresh_treeview()
                    messagebox.showinfo("Success", "User information updated successfully")
                except Exception as e:
                    messagebox.showerror("Error", "Failed to update user information")

        save_button = tk.Button(modify_window, text="Save Changes", command=save_changes)
        save_button.grid(row=3, columnspan=2)

def delete_selected():
    selected_item = tree.selection()
    if selected_item:
        confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this user?")
        if confirmed:
            item = tree.item(selected_item)
            values = item["values"]
            try:
                connection = sqlite3.connect("Database/AccountSystem.db")
                cur = connection.cursor()
                cur.execute("DELETE FROM AccountDB WHERE Email=?", (values[3],))
                connection.commit()
                connection.close()
                refresh_treeview()
                messagebox.showinfo("Success", "User deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", "Failed to delete user")

def search_by_email():
    search_email = search_email_entry.get()
    if search_email:
        data = load_data_by_email(search_email)
        refresh_treeview(data)
    else:
        refresh_treeview()

def load_data_by_email(email):
    try:
        connection = sqlite3.connect("Database/AccountSystem.db")
        cur = connection.cursor()
        cur.execute("SELECT * FROM AccountDB WHERE Email=?", (email,))
        data = cur.fetchall()
        connection.close()
        return data
    except Exception as e:
        messagebox.showerror("Error", "Failed to fetch data from the database")
        return []

def refresh_treeview(data=None):
    if data is None:
        data = load_data()
    tree.delete(*tree.get_children())
    for record in data:
        tree.insert("", "end", values=record)

data = load_data()

root = tk.Tk()
root.title("Admin Panel")

tree = ttk.Treeview(root)
tree["columns"] = ("ID", "FirstName", "LastName", "Email")

tree.heading("#1", text="ID")
tree.heading("#2", text="First Name")
tree.heading("#3", text="Last Name")
tree.heading("#4", text="Email")

tree.pack(fill="both", expand=True)

for record in data:
    tree.insert("", "end", values=record)
def show_all_records():
    refresh_treeview()

show_all_button = ttk.Button(root, text="Show All", command=show_all_records)
show_all_button.pack()
modify_button = ttk.Button(root, text="Modify", command=modify_selected)
delete_button = ttk.Button(root, text="Delete", command=delete_selected)
search_email_label = tk.Label(root, text="Search by Email:")
search_email_entry = tk.Entry(root)
search_email_button = ttk.Button(root, text="Search", command=search_by_email)

modify_button.pack()
delete_button.pack()
search_email_label.pack()
search_email_entry.pack()
search_email_button.pack()

root.mainloop()
