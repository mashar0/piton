import sys
from sys import platform
from time import sleep 
import os
try:
    from tkinter import *
    from tkinter import filedialog
except ModuleNotFoundError:
    os.system('clear')
    print("Modul Tkinter Belum Di Install")
    print("Untuk Cara Installnya Silakan Cari Di Google")
    print("Setiap OS Berbeda Cara Installnya")


lokasi_file = filedialog.askopenfilename(title="Open File Yang Akan Di Baca")

with open(lokasi_file, mode="r") as file:
    isi_data = file.read()
    os.system('clear')
    print("Isi Data Nya adalah : \n")
    for i in isi_data:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.01)
 
print("")
