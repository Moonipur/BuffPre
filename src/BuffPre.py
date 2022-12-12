#!/bin/python3
import os
import sys
from __init__ import *
from datetime import datetime

help_description = '''Usage: BuffPre [options] -h

Optional argruments:
    -b, --buffer    Buffer preparation (efault acid; base)
    -d, --dilute    Dilution of solution
    -m, --Molar     Calculate Molar of solution
    -r, --recovery  Calculate the percentage of recovery

File config: BuffPre -i <path> -o <path>
    -i <path>       Input config file path
    -o <path>       Your output directory path (default current directory)
    --conf          Display confic file pattern

Library & Test:
    -l, --library   Display pKa library
    -t, --test      Test example confic file

History:
    --hist          Display all command and output (Showed dates)

Other:
    -h, --help      Show this help message and exit
    -v, --version   The lastest version of BuffPre
    
Author's email:
    moo_sutthittha@hotmail.com

The lastest version:
    BuffPre v0.0.1    

** Please contact us if you have any questions or problems with the program.'''

version = 'BuffPre v0.0.1'

report = '** Plese check with HELP command:\n   BuffPre --help or BuffPre -h'

current_dir = os.getcwd()

time_stamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def Check_dir(path):
    isExist = os.path.isfile(path)
    PATH = []
    if isExist:
        print('Your input PATH is: {}'.format(path))
        PATH.append(path)
        if len(sys.argv) >= 4:
            if sys.argv[3] == '-o':
                if len(sys.argv) == 5:
                    outExist = os.path.isdir(sys.argv[4])
                    if outExist:
                        print('Your output PATH is: {}/Out_BuffPre.txt'.format(os.path.dirname(sys.argv[4])))
                        PATH.append('{}/Out_BuffPre.txt'.format(os.path.dirname(sys.argv[4])))
                    else:
                        print('ERROR: your output PATH does NOT exist')
                else:
                    print('Your output PATH is: {}/Out_BuffPre.txt'.format(current_dir))
                    PATH.append('{}/Out_BuffPre.txt'.format(current_dir))
            else:
                print('Your output PATH is: {}/Out_BuffPre.txt'.format(current_dir))
                PATH.append('{}/Out_BuffPre.txt'.format(current_dir))
        else:
            print('Your output PATH is: {}/Out_BuffPre.txt'.format(current_dir))
            PATH.append('{}/Out_BuffPre.txt'.format(current_dir))
    else:
        print('ERROR: your input PATH does NOT exist')

    return PATH


#History
hist = []
for i in range(len(sys.argv)):
    ar = sys.argv[i]
    hist.append(ar)

HIST(hist[1:])


#Check Argumants
if len(sys.argv) != 1:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print(help_description)
    elif sys.argv[1] == '-v' or sys.argv[1] == '--version':
        print(version)
    elif sys.argv[1] == '--hist':
        History(re=True)
    elif sys.argv[1] == '--conf':
        conf()
    elif sys.argv[1] == '-b' or sys.argv[1] == '--buffer':
        Buffer()
    elif sys.argv[1] == '-d' or sys.argv[1] == '--dilute':
        Dilute()
    elif sys.argv[1] == '-m' or sys.argv[1] == '--Molar':
        Molar()
    elif sys.argv[1] == '-r' or sys.argv[1] == '--recovery':
        Recovery()
    elif sys.argv[1] == '-i':
        if len(sys.argv) >= 3:
            if str(sys.argv[2])[-4:] == ".txt":
                inp_out = Check_dir(sys.argv[2])
                Confi(inp_out)
            else:
                print('ERROR: your input file is NOT text')
        else:
            print('ERROR: you did NOT provide an input path.')
    elif sys.argv[1] == '-l' or sys.argv[1] == '--library':
        buff()
    elif sys.argv[1] == '-t' or sys.argv[1] == '--test':
        Test()
    else:
        print('ERROR: unrecognized arguments: {}'.format(sys.argv[1]))
        print(report)
elif len(sys.argv) == 1:
    print(report)


