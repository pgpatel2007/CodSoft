import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4.")
            return

        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        all_chars = letters + digits + symbols

        password = [
            random.choice(letters),
            random.choice(digits),
            random.choice(symbols)
        ]
        password += random.choices(all_chars, k=length - 3)
        random.shuffle(password)

        final_password = ''.join(password)
        result_label.config(text=final_password)

        # Copy to clipboard
        root.clipboard_clear()
        root.clipboard_append(final_password)

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# UI Components
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="#000080")
result_label.pack(pady=10)

tk.Label(root, text="(Password is copied to clipboard)", font=("Arial", 10, "italic")).pack()

# Start GUI loop
root.mainloop()
