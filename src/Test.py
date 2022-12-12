from __init__ import *
import os

path_conf = '../lib/confic.txt'

path_out = os.getcwd()

tail = '''---------------------------------------------------------------------------------------------
** Confic file test already finished\n'''

def Test():
    conf()
    inp_out = [path_conf, path_out]
    Confi(inp_out)
    print(tail)

