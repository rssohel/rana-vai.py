import socket, threading, time, os
from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_logo():
    clear()
    print(Fore.GREEN + r"""
             ______  ______  __   __  ______    __   __  _ 
            |  __  ||  __  ||  \ |  ||  __  |  |  \ |  |(_)
            | |__| || |__| ||   \|  || |__| |  |   \|  | _ 
            |  _  / |  __  ||  . `  ||  __  |  |  . `  || |
            | | \ \ | |  | ||  |\   || |  | |  |  |\   || |
            |_|  \_\|_|  |_||__| \__||_|  |_|  |__| \__||_| 
    """)
    print(Fore.RED + "    [!] NETWORK STATUS CHECK MODE ACTIVE [!]")
    print(Fore.WHITE + "    ----------------------------------------")

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

target = input(Fore.GREEN + "    PROMPT > Target IP/URL: " + Fore.WHITE)

if target:
    print(Fore.YELLOW + "\n    Checking server status...\n")
    time.sleep(1)
    threading.Thread(target=check_host, args=(target, 80)).start()
