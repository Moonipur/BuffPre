#!/bin/python3

import os
from datetime import datetime


pKa_path = '../lib/lib_pKa'
pKb_path = '../lib/lib_pKb'

time_stamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

head_file = '''---------------------------------------------------------------------------------------------
                                  Buffer Preparation
---------------------------------------------------------------------------------------------\n'''


def acid(pKa, HA):
    print(head_file)
    lib = []
    pH = pKa - 1
    round = 1
    while pH <= pKa + 1:
        A = HA * pow(10, (pH - pKa))
        if A <= HA:
            print('{}) Acid concentration (M): {:.4f}'.format(round, HA) + ' | ' + 'Conjugate base concentration (M): {:.4f}'.format(A) + ' | ' + 'pH = {:.4f}'.format(pH))
            lib.append('{}) Acid concentration (M): {:.4f}'.format(round, HA) + ' | ' + 'Conjugate base concentration (M): {:.4f}'.format(A) + ' | ' + 'pH = {:.4f}'.format(pH))
            

        else:
            A = 1
            HA -= 0.2
            HA = A / pow(10, (pH - pKa))
            print('{}) Acid concentration (M): {:.4f}'.format(round, HA) + ' | ' + 'Conjugate base concentration (M): {:.4f}'.format(A) + ' | ' + 'pH = {:.4f}'.format(pH))
            lib.append('{}) Acid concentration (M): {:.4f}'.format(round, HA) + ' | ' + 'Conjugate base concentration (M): {:.4f}'.format(A) + ' | ' + 'pH = {:.4f}'.format(pH))
        
        pH += 0.2
        round += 1
    return lib



def saveout(lib, name):
    path = "{}/{}.txt".format(str(os.getcwd()), name)
    line = ["{}\n".format(i) for i in lib]
    with open(path,'w') as out:
        out.write(head_file)
        out.writelines(line)
        out.close()
    print("** Your file ({}.txt) already saved".format(name))
        
def Buff_type(bt):
    BT = {
        '01.1': 2.15,
        '01.2': 7.20,
        '02.1': 2.35,
        '02.2': 9.78,
        '03': 4.76,
        '04': 4.76,
        '05': 6.10,
        '06': 6.50,
        '07.1': 6.35,
        '07.2': 10.33,
        '08': 6.59,
        '09': 6.78,
        '10': 6.76,
        '11': 6.90,
        '12': 6.95,
        '13': 6.80,
        '14': 7.09,
        '15': 7.20,
        '16': 7.40,
        '17': 7.48,
        '18': 7.60,
        '19': 7.60,
        '20': 7.60,
        '21': 8.06,
        '22': 7.80,
        '23': 7.80,
        '24': 7.80,
        '25': 8.00,
        '26': 8.05,
        '27': 8.20,
        '28': 8.26,
        '29': 8.30,
        '30': 8.40,
        '31': 8.80,
        '32': 8.90,
        '33': 9.00,
        '34': 9.23,
        '35': 9.49,
        '36': 9.60,
        '37': 9.70,
        '38': 10.40,
        '39': 10.70
    }
    return(BT[bt])

def descript():
    with open(pKa_path,'r') as pKa_read:
        print(pKa_read.read())

def pKa(bt, function):
    pKa = Buff_type(bt)
    HA = 1
    lib = acid(pKa, HA)
    if function == True:
        save(lib)
    else:
        return lib

def save(lib):
    while True:
        print('---------------------------------------------------------------------------')
        print("Press 's' for save to text file (.txt) in current directory")
        print("Press 'q' for quit")
        s = input("Your choose: ")
        if s == 's':
            name = str(input("What is your file name: "))
            saveout(lib, name)
            break
        elif s == 'q':
            break
        else:
            print('ERROR: unrecognized arguments: {}'.format(s))

def Buffer():
    descript()
    while True:
        print("** Press 'q' for quit\n   Press 'o' for pKa description")
        bt = str(input('Your buffer type: '))
        if bt == 'q':
            break
        elif bt == 'o':
            descript()
        else:
            pKa(bt, True)
            

