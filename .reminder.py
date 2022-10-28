import os

reminder = [
["Bila kau tak mau merasakan lelahnya belajar,\nmaka kau akan menanggung pahitnya kebodohan\n","Imam Syafi'i"],
["Ilmu itu seperti air.\nJika ia tidak bergerak,\nmaka ia akan menjadi keruh lalu membusuk.\n","Imam Syafi'i"],
["Aku tidak memiliki kecenderungan\n(kecintaan) terhadap dunia.\nKeberadaanku di dalam dunia seperti\nseorang musafir yang berteduh di bawah pohon,\nkemudian pergi dan meninggalkan pohon tersebut.\n","HR. Tirmidzi"]
        ]

try:
  import colorama
except:
  os.system("python3 -m pip install colorama")
  os.system("clear")

from colorama import Fore, Style
from random import randrange
banner = f"""{Fore.LIGHTCYAN_EX}#=============================================#{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}|{Style.RESET_ALL} Welcome to termux:                          {Fore.LIGHTCYAN_EX}|{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}|{Style.RESET_ALL}                                             {Fore.LIGHTCYAN_EX}|{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}|{Style.RESET_ALL} • Github: github.com/adprm123               {Fore.LIGHTCYAN_EX}|{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}|{Style.RESET_ALL}                                             {Fore.LIGHTCYAN_EX}|{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}#=============================================#{Style.RESET_ALL}
"""
print(banner)
reminder_saat_ini = reminder[randrange(len(reminder))]
print(f"\u26A0 {Fore.RED}Reminder Saat Ini{Style.RESET_ALL} \u26A0")
print("")
print(f"{Fore.YELLOW}{reminder_saat_ini[0]}{Style.RESET_ALL}")
print(f"( {Fore.GREEN}{reminder_saat_ini[1]}{Style.RESET_ALL} )")
print("")
