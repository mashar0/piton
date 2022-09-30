# ini adalah script latihan saya saat belajar python dasar 

import random
from sys import platform
import sys
import os
import datetime as dt
from time import sleep
import subprocess as sp
import calendar


# ========================================================================================

def clear():
    if platform == "linux" or platform == "linux2":
        sp.call("clear", shell=True)
    elif platform == "win32":
        sp.call('cls', shell=True)

# ========================================================================================

def banner():
    banner = '''
    ===============================================
    | Script Latihan | Ctrl-c Untuk Exit          |
    ===============================================
    | [1]  Menampilkan kalender                   |
    | [2]  Menampilkan Perkalian                  |
    | [3]  Halaman Login                          |
    | [4]  Program Irit Boros                     |
    | [5]  Timer Workout                          |
    | [6]  Penghitung Umur                        |
    | [7]  Menu Belanja                           |
    ===============================================
    '''
    print(banner)
# ========================================================================================

def start():
    clear()
    
    banner()
    try:
        pilih = int(input("Input\n > "))
    except ValueError:
        clear()
        input('Masukin Inputan Yang Bener Bro / Sist ')
        start()
    except KeyboardInterrupt:
        clear()
        banner()
        print("Script Berakhir")
        exit()
    if pilih == 1:
        kalender()
    elif pilih == 2:
        perkalian()
    elif pilih == 3:
        halaman_login()
    elif pilih == 4:
        irit_boros()
    elif pilih == 5:
        prog_tim()
    elif pilih == 6:
        umur()
    elif pilih == 7:
        struk_belanja()
    else:
        start()

# ========================================================================================

def kalender():
    clear()
    try:
        tahun = int(input("Tahun : "))
    except ValueError:
        clear()
        input("Masukin Tahun Bro / Sist ")
        kalender()
    try:
        bulan = int(input("Bulan : "))
    except ValueError:
        clear()
        input('Masukin Bulan Bro / Sist ')
        kalender()
    try:
        clear()
        print(calendar.month(tahun, bulan),"\n")
        input("Tekan Enter Untuk Melanjutkan ")
        start()
    except IndexError:
        clear()
        input("Bulannya Jangan Lebih Dari 12 Bro / Sist\nKarna Bulan Cuma Ada 12 ")
        kalender()
# ========================================================================================

def perkalian():
    clear()
    try:
        input_perkalian = int(input("Perkalian    : "))
        input_line = int(input("Berapa Baris : "))
        clear()
        header = f"""
        ====================
            Perkalian {input_perkalian}q
        ====================
        """
        print(header)
        for ulang in range(1, input_line+1):
            print(f"• {ulang} x {input_perkalian} = {input_perkalian*ulang}")
        input("\nTekan Enter Untuk Melanjutkan ")
        start()
    except ValueError:
        clear()
        input("Masukin Inputan Yang Bener Bro / Sist")
        perkalian()

# ========================================================================================

def halaman_login():
    try:
        clear()
        username = ['adi','Adi','iki','Uko','Iki','uko']
        password = ['Hhhh','ukoggewe','ikiKu','haerudin']
        token_auth = ['ksfdbjdjdjkbvjmdbl','gggaming','pythonituseru']
        in_username = str(input("Username : "))
        in_password = str(input("Password : "))
        token_auths = str(input("Token    : "))
        if in_username in username and in_password in password and token_auths in token_auth:
            clear()
            print("Login Sukses")
            input("\nTekan Enter Untuk Melanjutkan ")
            start()
        elif in_username not in username and in_password in password and token_auths in token_auth: 
            clear()
            print("Username Salah")
            input("\nTekan Enter Untuk Melanjutkan ")
            halaman_login()
        elif in_username in username and in_password not in password and token_auths in token_auth:
            clear()
            print("Password Salah")
            input("\nTekan Enter Untuk Melanjutkan ")
            halaman_login()
        elif in_username in username and in_password in password and token_auths not in token_auth:
            clear()
            print("Token Auth Salah")
            input("\nTekan Enter Untuk Melanjutkan ")
            halaman_login()
        else:
            clear()
            print("Inputan Yang Anda Masukan Salah")
            input("\nTekan Enter Untuk Melanjutkan ")
            halaman_login()
    except KeyboardInterrupt:
        clear()
        input("Eits Anda Tidak Bisa Keluar Pake ctrl c\nUdah Login Dulu Aja ")
        halaman_login()

# ========================================================================================

def irit_boros():
    try:
        clear()
        nama = input("Nama           : ")
        jatahming = int(input("Jatah Mingguan : "))
        jatahhari = jatahming//7
        jatahboros = jatahming//4
        habis = int(input("Habis Hari Ini : "))
        if habis in range(jatahhari, jatahboros):
            Boros = 'Normal'
        elif habis >= jatahboros:
            Boros = "Boros"
        elif habis <= jatahhari:
            Boros = "Irit"
        sign = f'''
===================================================
    Keterangan :
    BOROS  = PENGGUNAAN DI ATAS {jatahboros:,}
    NORMAL = PENGGUNAAN RENTANG {jatahhari:,} - {jatahboros:,}|
    IRIT   = PENGGUNAAN DI BAWAH {jatahhari:,}
===================================================
    Nama           : {nama}
    Uang Mingguan  : {jatahming:,}
    Jatah Per Hari : {jatahhari:,}
    Habis Hari Ini : {habis:,}
    Boros / Tidak  : {Boros}
===================================================
        '''
        clear()
        print(sign)
        input("\nTekan Enter Untuk Melanjutkan ")
        start()
    except ValueError:
        clear()
        input('Masukin Inputan Yang Bener Bro / Sist ')
        irit_boros()


# ========================================================================================

def prog_tim():
    def timer_work():
        try:
            clear()
            work = int(input("Work (Secs) : "))
            rest = int(input("Rest (Secs) : "))
            sett = int(input("Set         : "))
            works = work + 1
            rests = rest + 1
            total_waktu = ((work+rest) * sett)
            if total_waktu >= 3600:
                jam = total_waktu // 60 // 60
                menit = total_waktu // 60 % 60
                detik = total_waktu % 60
            else:
                jam = 0
                menit = total_waktu // 60 % 60
                detik = total_waktu % 60
            clear()
            print(f"Total Waktu : {jam} Jam {menit} Menit {detik} Detik")
            input("\nTekan Enter Untuk Melanjutkan ")
            clear()
            for a in range(1, sett+1):
                clear()
                print(f"Memasuki Set {a}")
                sleep(0.3)
                print(".")
                sleep(0.3)
                print(". .")
                sleep(0.3)
                print(". . .")
                sleep(0.3)
                for s in range(1, work+1):
                    clear()
                    print(f"Total Waktu : {jam} Jam {menit} Menit {detik} Detik")
                    print(f"Total Set   : {sett} Set")
                    print(f"Set : {a} | Work {work} Detik")
                    works -= 1
                    print(f"\nWork {works} Detik\t | Ctrl + C Untuk Keluar")
                    sleep(1)
                works = work + 1
                clear()
                print("Rest")
                sleep(0.3)
                print(".")
                sleep(0.3)
                print(". .")
                sleep(0.3)
                print(". . .")
                sleep(0.3)
                for d in range(1, rest+1):
                    clear()
                    print(f"Total Waktu : {jam} Jam {menit} Menit {detik} Detik")
                    print(f"Total Set   : {sett} Set")
                    print(f"Set : {a} | Rest {rest} Detik")
                    rests -= 1
                    print(f"\nRest {rests} Detik\t | Ctrl + C Untuk Keluar")
                    sleep(1)
                rests = rest + 1
            print("\nTimer Selesai")
            input("\nTekan Enter Untuk Melanjutkan ")
            start()
        except ValueError:
            clear()
            input("Masukin Inputan Yang Bener Bro / Sist ")
            timer_work()
        except KeyboardInterrupt:
            clear()
            input("Menghentikan Proses\nEnter Untuk Melanjutkan ")
            start()
    timer_work()

# ========================================================================================

def umur():
    clear()
    saat_ini = dt.date.today()
    banner_umur = f'''
    -----------------------------
        Saat Ini : {saat_ini}
        Hari     : {saat_ini:%A}
    -----------------------------
    '''
    print(banner_umur)
    print("\nMasukan Tanggal Lahir Anda")
    try:
        tanggal_lahir = int(input("Tanggal : "))
        bulan_lahir = int(input("Bulan   : "))
        tahun_lahir = int(input("Tahun   : "))
        clear()
        print(banner_umur)
        hari_lahir = dt.date(tahun_lahir, bulan_lahir, tanggal_lahir)
        umur_hari = saat_ini - hari_lahir
        umur_tahun = umur_hari.days // 365
        umur_bulan = (umur_hari.days % 365) // 30
        bulan_lahir = hari_lahir.month
        tanggalna_lahir = hari_lahir.day
        print(f"Kamu Lahir Pada    : {hari_lahir}")
        print(f"Di Hari            : {hari_lahir:%A}")
        print(f"Umur Kamu Saat Ini : {umur_tahun} Tahun {umur_bulan} Bulan\n")
        input("Tekan Enter Untuk Melanjutkan ")
        start()
    except ValueError:
        clear()
        input("Masukin Inputan Yang Bener Bro / Sist ")
        umur()
# ========================================================================================

def struk_belanja():
    try:
        from prettytable import PrettyTable
    except ModuleNotFoundError:
        clear()
        install = input("Modul pretty belum Terinstall\nApa Kamu Mau Menginstallnya y/n --> ")
        if install == "y" or install == "Y":
            os.system("pip install prettytable")
        elif install == "n" or install == "N":
            exit()
    list_harga = []
    list_belanja = {}
    def tabel():

        t = PrettyTable(["No","Menu","Harga"])
        t.add_row([1, "Bala-bala", "1.000"])
        t.add_row([2, "Cireng", "1.000"])
        t.add_row([3, "Gehu", "1.000"])
        t.add_row([4, "Makaroni", "1.000"])
        t.add_row([5, "Cimol", "1.000"])
        t.add_row([6, "Cireng isi", "1.000"])
        t.add_row([7, "Otak-otak", "1.000"])
        t.add_row([8, "Batagor", "1.000"])
        t.add_row([9, "Bihun", "1.000"])
        t.add_row([10, "Comro", "1.000"])
        t.add_row([11, "Jumlahkan Pembelian",""])
        print(t)

    def startken_mang_otong():
        no_bal = 0
        no_cir = 0
        no_geh = 0
        no_mak = 0
        no_cim = 0
        no_ciris = 0
        no_otak = 0
        no_bata = 0
        no_bihun = 0
        no_comro = 0
        while True:
            cek_batas = len(list_belanja)
            clear()
            totalnya = 0
            for total in range(len(list_harga)):
                totalnya += list_harga[total]
            print("Selamat datang di warung mang Otong\n")
            print(f"Kamu Membeli :\t\tTotal : Rp. {totalnya:,}")
            if cek_batas != 0:
                print("="*35)
            for list_beli in list_belanja:
                print("- " + list_belanja.get(list_beli))
            if cek_batas != 0:
                print("="*35)
            tabel()
            try:
                pilih = int(input("Silakan Pilih No Menu : \n> "))
            except ValueError:
                clear()
                input("Masukin Inputan Yang Bener Bro / Sist ")
                continue
            if pilih == 1:
                no_bal += 1
                list_harga.append(1000)
                list_belanja.update({"bala":f"Bala-bala {no_bal}"})
            elif pilih == 2:
                no_cir += 1
                list_harga.append(1000)
                list_belanja.update({"cir":f"Cireng {no_cir}"})
            elif pilih == 3:
                no_geh += 1
                list_harga.append(1000)
                list_belanja.update({"geh":f"Gehu {no_geh}"})
            elif pilih == 4:
                no_mak += 1
                list_harga.append(1000)
                list_belanja.update({"mak":f"Makaroni {no_mak}"})
            elif pilih == 5:
                no_cim += 1
                list_harga.append(1000)
                list_belanja.update({"cim":f"Cimol {no_cim}"})
            elif pilih == 6:
                no_ciris += 1
                list_harga.append(1000)
                list_belanja.update({"ciris":f"Cireng Isi {no_ciris}"})
            elif pilih == 7:
                no_otak += 1
                list_harga.append(1000)
                list_belanja.update({"otak":f"Otak-otak {no_otak}"})
            elif pilih == 8:
                no_bata += 1
                list_harga.append(1000)
                list_belanja.update({"bata":f"Batagor {no_bata}"})
            elif pilih == 9:
                no_bihun += 1
                list_harga.append(1000)
                list_belanja.update({"bihun":f"Bihun {no_bihun}"})
            elif pilih == 10:
                no_comro += 1
                list_harga.append(1000)
                list_belanja.update({"comro":f"Comro {no_comro}"})
            elif pilih == 11:
                if totalnya == 0:
                    clear()
                    input("Kamu Membeli Apapun , Kamu Tidak Perlu Membayar ")
                    start()
                else:
                    clear()
                    input(f"Total Yang Harus Kamu Bayar Adalah {totalnya:,} ")
                    clear()
                    namamu = str(input("Namamu Siapa\nNama : "))
                    clear()
                    sapa_dia = f'''
Hai {namamu} , Terima Kasih Sudah Belanja Di Warung Mang Otong ,
Total Yang Harus Kamu Bayar Adalah : {totalnya:,}

Tekan Enter Untuk Melanjutkan '''
                    clear()
                    for sapalah in sapa_dia:
                        sys.stdout.write(sapalah)
                        sys.stdout.flush()
                        sleep(random.random()*0.0001)
                    input()
                    clear()
                    input(f'Memberikan {totalnya:,} Kepada Penjual ')
                    input("Ok ")
                    start()
    startken_mang_otong()

start()
