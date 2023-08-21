#!/usr/bin/env python
## source: https://nitratine.net/blog/post/simulate-keypresses-in-python/
from pynput.keyboard import Controller
import time
import argparse
from getpass import getpass as gtpw

def emulateKeyPress(writeStr, wait=5):
    for t in range(wait, -1, -1):
        print(f'Typing passed-string to the active window in {t} seconds', end='\r')
        time.sleep(1)
    print('')
    kb = Controller()
    kb.type(writeStr)

if __name__=='__main__':
    try:    
        parser = argparse.ArgumentParser(description='Keypress emulator')
        parser.add_argument('--kbstr', '-s', help='string to emulate keypress on')
        parser.add_argument('--wait', '-w', type=int, help='wait time before keypress emulation begins')
        args = parser.parse_args()
        emulateKeyPress(args.kbstr or gtpw('String to emulate > '), args.wait or 5)
    except KeyboardInterrupt:
        print('bye!')