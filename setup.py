import os.path
from getpass import getpass
import time

os.system('clear')
os.system('figlet -small SETUP INSTALLING | lolcat')
print('[+] System installing...')
os.system('chmod +x *')
time.sleep(5)
os.system('cd && mv Termux-Lock $PREFIX/share && cd $PREFIX/share/Termux-Lock')
os.system('mv window $PREFIX/bin && mv unistall-lock $PREFIX/bin')
os.system('window')
