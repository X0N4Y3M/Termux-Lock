import os
import time
import sys

os.system('clear')
os.system('figlet -f small UNISTALLING | lolcat')
print('[+] System Unistalling...')
time.sleep(4)
os.system('rm $PREFIX/bin/window && cd $PREFIX/share/Termux-Lock && rm main.py setup.py unistall-lock ')
print('DONE')
time.sleep(5)
