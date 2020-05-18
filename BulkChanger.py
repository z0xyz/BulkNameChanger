import  os
from os import *
from sys import platform 

path = os.getcwd()+"/"
list = os.listdir (path)

def BulkChange ():
    for  number , filename  in  enumerate (list):
        if filename == "BulkChanger.py":
            continue 
        elif os.path.isdir(filename):
            continue
        source = path + filename 
        destionation = str(number) + "-" + filename
        destionation = path + destionation 
        os.rename (source , destionation)

BulkChange ()
