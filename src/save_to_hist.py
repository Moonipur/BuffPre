import os
from __init__ import *
from datetime import datetime

time_now = '[{}]'.format(datetime.now().strftime("%b-%d-%Y %H:%M:%S"))
path_hist = "../lib/history"

def HIST(data):
    d = ' '.join(data)
    with open(path_hist ,'a') as hist:
        hist.write(time_now + '\t')
        hist.writelines('BuffPre '+ d + '\n')
        hist.close()