#!/bin/python3

buff_path = '../lib/lib_pKa'

confic_path = '../lib/confic.txt'

def buff():
    with open(buff_path,'r') as buff_read:
        print(buff_read.read())


def conf():
    with open(confic_path,'r') as conf_read:
        print(conf_read.read())