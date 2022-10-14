# ini adalah script belajar modul tkinter
# jendela login dengan python tkinter

from tkinter import *
from tkinter import messagebox, ttk

kenalan = """
Hallo Bro ,
Selamat Datang Di Python Tk Interface ,

github : https://github.com/adprm123
"""

user = ['adi','riko','adi permadi']
pasw = ['haerudin','indra','riko mashar']

def jendela_login():     
    start = messagebox.askyesno(message="Copyright by ?")
    if start == True:
        pass
    else:
        exit()
        
    window = Tk()
    window.geometry("300x220")
    window.resizable(False, False)
    window.title("Login")
    window.configure(bg="white")

    USERNAME = StringVar()
    PASSWORD = StringVar()

    def pp():
        if USERNAME.get() in user and PASSWORD.get() in pasw:
            messagebox.showinfo(message="Login Sukses")
            window.destroy()
            selamat_datang = Tk()
            selamat_datang.geometry("300x200")
            selamat_datang.resizable(False, False)
            selamat_datang.title("Selamat Datang")
            
            ucapan = Label(selamat_datang, text=kenalan)
            ucapan.pack(padx=10, pady=10, fill='x')


            selamat_datang.mainloop()
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