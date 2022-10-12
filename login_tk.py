# ini adalah script belajar modul tkinter

import tkinter as tk 
from tkinter import ttk, messagebox

def jendela_login():
    window = tk.Tk()
    window.geometry("300x220")
    window.title("Login")
    window.configure(bg="white")

    USERNAME = tk.StringVar()
    PASSWORD = tk.StringVar()
    def pp():
        print(USERNAME.get())
        print(PASSWORD.get())

    frame = ttk.Frame(window)
    frame.pack(padx=10, pady=10, expand=True, ipadx=100)

    label_username = ttk.Label(frame, text="Username")
    label_username.pack(padx=10, pady=7,  expand=True, fill='x')
    input_username = ttk.Entry(frame, textvariable=USERNAME)
    input_username.pack(padx=10, pady=5, expand=True, fill='x')

    label_pasword = ttk.Label(frame, text="Password")
    label_pasword.pack(padx=10, pady=7, expand=True, fill='x')
    input_password = ttk.Entry(frame, textvariable=PASSWORD)
    input_password.pack(padx=10, pady=5, expand=True, fill='x')

    login = ttk.Button(frame, text="Login", command=pp)
    login.pack(padx=10, pady=10, expand=True)

    window.mainloop()

jendela_login()