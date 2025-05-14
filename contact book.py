import tkinter as tk
from tkinter import messagebox
import json
import os

CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and Phone are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    refresh_list()
    clear_entries()

# Search contact
def search_contact():
    query = search_entry.get().lower()
    result = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    refresh_list(result)

# Update selected contact
def update_contact():
    global selected_index
    if selected_index is None:
        messagebox.showwarning("No selection", "Please select a contact to update.")
        return
    contacts[selected_index] = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }
    save_contacts(contacts)
    refresh_list()
    clear_entries()

# Delete selected contact
def delete_contact():
    global selected_index
    if selected_index is None:
        messagebox.showwarning("No selection", "Please select a contact to delete.")
        return
    contacts.pop(selected_index)
    save_contacts(contacts)
    refresh_list()
    clear_entries()

# Refresh contact list display
def refresh_list(display_contacts=None):
    contact_list.delete(0, tk.END)
    display_contacts = display_contacts if display_contacts is not None else contacts
    for idx, contact in enumerate(display_contacts):
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Clear entry fields
def clear_entries():
    global selected_index
    selected_index = None
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Load selected contact
def on_select(event):
    global selected_index
    if not contact_list.curselection():
        return
    selected_index = contact_list.curselection()[0]
    contact = contacts[selected_index]
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

    name_entry.insert(0, contact['name'])
    phone_entry.insert(0, contact['phone'])
    email_entry.insert(0, contact['email'])
    address_entry.insert(0, contact['address'])

# Main UI
root = tk.Tk()
root.title("Contact Book")

contacts = load_contacts()
selected_index = None

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Phone").grid(row=1, column=0)
tk.Label(root, text="Email").grid(row=2, column=0)
tk.Label(root, text="Address").grid(row=3, column=0)

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1)

tk.Button(root, text="Add", command=add_contact).grid(row=0, column=2)
tk.Button(root, text="Update", command=update_contact).grid(row=1, column=2)
tk.Button(root, text="Delete", command=delete_contact).grid(row=2, column=2)

search_entry = tk.Entry(root)
search_entry.grid(row=4, column=0)
tk.Button(root, text="Search", command=search_contact).grid(row=4, column=1)

contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=5, column=0, columnspan=3)
contact_list.bind('<<ListboxSelect>>', on_select)

refresh_list()

root.mainloop()
