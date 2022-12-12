import os
from __init__ import *

def source(input_output):
    conf =  open(input_output[0], 'r')
    con = conf.readlines()
    return con

def hist(con, reset):
    if con[reset][7] == 'Y':
        empty()
    elif con[reset][7] == 'N':
        pass
    else:
        pass

def buff(con, pK, save, pi):
    pk = con[pK]
    PK = pk[pk.find('[')+len('['):pk.rfind(']')]
    lib = pKa(PK, False)
    if con[save][6] == 'Y':
        name = con[pi[1] + 3]
        file = name[name.find('[')+len('['):name.rfind(']')]
        saveout(lib, file)
    elif con[save][6] == 'N':
        pass


def Confi(input_output):
    pi = []

    conf =  open(input_output[0], 'r')
    for l_no, line in enumerate(conf):
        if '#hist' in line:
            History(re=False)
            pi.append(l_no)
        elif '#buffer' in line:
            pi.append(l_no)
        elif '#dilute' in line:
            pi.append(l_no)
        elif '#Molar' in line:
            pi.append(l_no)
        else:
            pass
    
    
    reset = pi[0] + 1
    hist(source(input_output), reset)
    pKa, save = pi[1] + 1, pi[1] + 2
    buff(source(input_output), pKa, save, pi)


    



    # with open(input_output[1], 'w') as out:
    #     out.writelines()
    #     out.close()
        

