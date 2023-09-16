'''
Author: Hassaan Ahmed
Date: August 10, 2023
Github: https://github.com/hassaanahmed04/

'''
import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

# Connect to the SQLite database
conn = sqlite3.connect("Database/AccountSystem.db")
cursor = conn.cursor()


with open("./Database/user_email.txt", "r") as file:
    user_email = file.read().strip()
# Create the main Tkinter window
root = tk.Tk()
root.title("Previous Images")

# Create a Treeview widget to display data
treeview = ttk.Treeview(root, columns=("Filename", "Timestamp"), show="headings")
treeview.heading("Filename", text="Filename")
treeview.heading("Timestamp", text="Timestamp")
treeview.pack()

# Fetch data from the database and populate the Treeview
def populate_treeview(query=user_email):
    treeview.delete(*treeview.get_children())
    if query=="admin":
        query=None
    
    if query:
        cursor.execute("SELECT filename, timestamp FROM screenshots WHERE filename LIKE ?", ('%' + query + '%',))
    else:
        cursor.execute("SELECT filename, timestamp FROM screenshots")
    rows = cursor.fetchall()
    for row in rows:
        treeview.insert("", "end", values=row)

populate_treeview()

# Function to open the image when a row in the Treeview is clicked
def open_image(event):
    selected_item = treeview.selection()[0]
    filename = treeview.item(selected_item, "values")[0]
    image = Image.open(filename)
    image.show()

# Bind the open_image function to the Treeview's double click event
treeview.bind("<Double-1>", open_image)

# Function to delete a selected item
def delete_item():
    selected_item = treeview.selection()[0]
    filename = treeview.item(selected_item, "values")[0]

    # Display a confirmation message box
    confirmation = messagebox.askyesno("Delete Item", f"Are you sure you want to delete '{filename}'?")
    if confirmation:
        cursor.execute("DELETE FROM screenshots WHERE filename = ?", (filename,))
        conn.commit()
        populate_treeview()

# Create a delete button
delete_button = tk.Button(root, text="Delete", command=delete_item)
delete_button.pack()

# Function to search for screenshots by filename
# def search_screenshots():
#     search_query = search_entry.get()
#     populate_treeview(query=search_query)

# Create a search entry and button
# search_entry = tk.Entry(root)
# search_entry.pack()
# search_button = tk.Button(root, text="Search", command=search_screenshots)
# search_button.pack()

# Function to close the database and the Tkinter window
def close_window():
    conn.close()
    root.destroy()

# Create a button to close the window
close_button = tk.Button(root, text="Close", command=close_window)
close_button.pack()

# Start the Tkinter event loop
root.mainloop()
