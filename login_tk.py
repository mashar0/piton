# ini adalah script belajar modul tkinter

from tkinter import *
from tkinter import messagebox, ttk

user = ['adi','riko']
pasw = ['haerudin','indra']

def jendela_login():     
    start = messagebox.askyesno(message="Copyright by ?")
    if start == True:
        pass
    else:
        exit()
        
    window = Tk()
    window.geometry("300x220")
    window.title("Login")
    window.configure(bg="white")

    USERNAME = StringVar()
    PASSWORD = StringVar()

    def pp():
        if USERNAME.get() in user and PASSWORD.get() in pasw:
            messagebox.showinfo(message="Login Sukses")
            exit()
        elif USERNAME.get() not in user and PASSWORD.get() in pasw:
            messagebox.showinfo(message="Username Salah")
        elif USERNAME.get() in user and PASSWORD.get() not in pasw:
            messagebox.showinfo(message="Password Salah")
        else:
            messagebox.showinfo(message="Username dan Password Salah")
        
        

    frame = Frame(window)
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