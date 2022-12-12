#!/bin/python3

import os
from __init__ import *


hist_path = '../lib/history'

head_hist = '''---------------------------------------------------------------------------------------------
                                History of the BuffPre
---------------------------------------------------------------------------------------------\n'''

def empty():
    with open(hist_path, 'w') as emp:
        emp.write(head_hist)
        emp.close()
    print('** Your history already reset.')

def reset():
    print(head_hist)
    while True:
        print('What you want to reset your history?')
        empt = input("Your choose [Y/N]:")
        if empt == 'Y':
            empty()
            break
        elif empt == 'N':
            break
        else:
            print('ERROR: unrecognized arguments: {}\n'.format(empt))

def History(re):
    with open(hist_path,'r') as conf_read:
        print(conf_read.read())
    if re == True:
        reset()


    