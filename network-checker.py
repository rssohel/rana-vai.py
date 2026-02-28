import socket, threading, time, os
from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_logo():
    clear()
    print(Fore.GREEN + r"""
    __  __       _    _                   _              
   |  \/  | __ _| | _| |__   ___  _ __ __| | ___  _ __  
   | |\/| |/ _` | |/ / '_ \ / _ \| '__/ _` |/ _ \| '_ \ 
   | |  | | (_| |   <| | | | (_) | | | (_| | (_) | | | |
   |_|  |_|\__,_|_|\_\_| |_|\___/|_|  \__,_|\___/|_| |_|
    """)
    print(Fore.YELLOW + "[*] Safe Network Checker Tool (Legal Use Only)\n")

def check_host(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip, port))
        print(Fore.GREEN + f"[+] {ip}:{port} is ONLINE")
        s.close()
    except:
        print(Fore.RED + f"[-] {ip}:{port} is OFFLINE")

show_logo()
target = input(Fore.GREEN + "PROMPT > Target IP (Local/Own Server Only): " + Fore.WHITE)

if target:
    print(Fore.YELLOW + "\nChecking server status...\n")
    for port in range(1, 1025):
        threading.Thread(target=check_host, args=(target, port)).start()
