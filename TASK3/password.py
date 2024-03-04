import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class FancyPasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Fancy Password Generator")
        self.master.geometry("400x300")
       
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.master, text="Fancy Password Generator \N By Cyberwave", font=("Helvetica", 16))
        title_label.pack(pady=10)

        self.length_var = tk.IntVar(value=12)
        length_label = tk.Label(self.master, text="Password Length:")
        length_label.pack()
        length_entry = tk.Entry(self.master, textvariable=self.length_var)
        length_entry.pack()

        self.complexity_var = tk.StringVar(value="Medium")
        complexity_label = tk.Label(self.master, text="Password Complexity:")
        complexity_label.pack()
        complexity_combobox = tk.OptionMenu(self.master, self.complexity_var, "Low", "Medium", "High")
        complexity_combobox.pack()

        generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=10)

        self.password_var = tk.StringVar()
        password_label = tk.Label(self.master, text="Generated Password:")
        password_label.pack()
        password_entry = tk.Entry(self.master, textvariable=self.password_var, state="readonly")
        password_entry.pack()

        copy_button = tk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.pack(pady=10)

    def generate_password(self):
        length = self.length_var.get()
        complexity = self.complexity_var.get()

        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        pyperclip.copy(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")

root = tk.Tk()
app = FancyPasswordGenerator(root)
root.mainloop()