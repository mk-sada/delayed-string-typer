#!/usr/bin/env python
#cython: language_level=3
## source: https://nitratine.net/blog/post/simulate-keypresses-in-python/
from pynput.keyboard import Controller, Key
import time
import argparse
from getpass import getpass as gtpw

def emulateKeyPress(writeStr, wait=5, perchar=False):
    kb = Controller()
    for t in range(wait, -1, -1):
        print(f'Typing passed-string to the active window in {t} seconds', end='\r')
        time.sleep(1)
    if perchar:
        for c in writeStr:
            if c.isupper():
                with kb.pressed(Key.shift):
                    kb.tap(c.lower())
            else:
                kb.type(c)
    else:
        kb.type(writeStr)
    print('')

if __name__=='__main__':
    try:    
        parser = argparse.ArgumentParser(description='Keypress emulator')
        parser.add_argument('--kbstr', '-s', help='string to emulate keypress on')
        parser.add_argument('--wait', '-w', type=int, help='wait time before keypress emulation begins')
        parser.add_argument('--perchar', '-p', action='store_true', help='emulate characters one at a time, capital letters are done with shift')
        args = parser.parse_args()
        emulateKeyPress(args.kbstr or gtpw('String to emulate > '), args.wait or 5, args.perchar)
    except KeyboardInterrupt:
        print('bye!')