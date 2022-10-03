#coding=utf-8
import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools');time.sleep(1)
else:
    print('033[1;31mSorry System not support this tools');sys.exit()
    
banner=("""\033[1;37m     ______   _______   ______  __      __   ______   __    __ 
 /      \ |       \ |      \|  \    /  \ /      \ |  \  |  \
|  $$$$$$\| $$$$$$$\ \$$$$$$ \$$\  /  $$|  $$$$$$\| $$\ | $$
| $$__| $$| $$__| $$  | $$    \$$\/  $$ | $$__| $$| $$$\| $$
| $$    $$| $$    $$  | $$     \$$  $$  | $$    $$| $$$$\ $$
| $$$$$$$$| $$$$$$$\  | $$      \$$$$   | $$$$$$$$| $$\$$ $$
| $$  | $$| $$  | $$ _| $$_     | $$    | $$  | $$| $$ \$$$$
| $$  | $$| $$  | $$|   $$ \    | $$    | $$  | $$| $$  \$$$
 \$$   \$$ \$$   \$$ \$$$$$$     \$$     \$$   \$$ \$$   \$$
                                                            
                                                            
                                                            
[+]═════════════════════════════════════════
[+] Author    :  ARIYAN
[+] Github    : ariyan-king
[+] Facebook  : Ariyan Islam Nil
[+] Tool Type : Premium
[+] Version   : 1.0.0
[+] this massage for haters : \033[1;31mjust feel me 🔥
\033[1;37m[+]═════════════════════════════════════════""")

def main():
    if path.isfile("dz.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/ARIYAN110/Data/main/dz.so -o dz.so")
    system('clear')
    print(banner)
    print('[1] Version : 1.3.4 (new)\n[2] Version : 1.3.3 (old)\n[3] Version : 1.3.2 (old)\n[4] Random Cloning (new)\n\033[1;37m[+]═════════════════════════════════════════')
    vs=input('[•] Choice : ')
    if vs in ['1','01']:
        if path.isfile("ARIYAN.so"):
            import ARIYAN
        else:
            system("curl -L https://raw.githubusercontent.com/ARIYAN110/Data/main/ARIYANG.so -o ARIYANG.so")
            import ARIYANG
    elif vs in ['2','02']:
        if path.isfile("ARIYAN64.so"):
            import ARIYAN
        else:
            system("curl -L https://raw.githubusercontent.com/ARIYAN110/Data/main/ARIYAN64.so -o ARIYAN64.so")
            import ARIYAN64
    elif vs in ['3','03']:
        if path.isfile("ARIYAN.so"):
            import ARIYAN64
        else:
            system("curl -L https://raw.githubusercontent.com/ARIYAN110/Data/main/ARIYAN.so -o ARIYAN.so")
            import ARIYAN
    elif vs in ['4','04']:
        if path.isfile("Rndm.so"):
            import Rndm
        else:
            system("curl -L https://raw.githubusercontent.com/ARIYAN110/Data/main/Rndm.so -o Rndm.so")
            import Rndm
    else:
        if path.isfile("ARIYAN.so"):
            import ARIYAN
        else:
            system("curl -L https://raw.githubusercontent.com/ARIYAN110/Data/main/ARIYANG.so -o ARIYANG.so")
            import ARIYAN
main()
