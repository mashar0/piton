from tkinter import *

def window_satu():
    global window_01
    window_01 = Tk()
    window_01.geometry("400x300")
    window_01.title("Window Pertama")

    tombol = Button(text="Beralih Ke Window 2", command=window_dua)
    tombol.pack(padx=10, pady=10)

    window_01.mainloop()

def window_dua():
    global window_02
    window_02 = Tk()
    window_02.geometry("400x300")
    window_02.title("Window Kedua")

    label = Label(window_02, text="Ini Adalah Window Dua")
    label.pack(padx=10, pady=10)

    window_02.mainloop()

window_satu()