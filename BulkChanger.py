import os 
from sys import platform 

cwd = os.getcwd()+"/"
list = os.listdir (cwd)
def BulkChange ():
    for number , filename in enumerate(os.listdir(cwd)):
        if filename == "BulkChanger.py":
            continue 
        source = cwd + filename 
        destionation = str(number) + "-" + filename
        destionation = cwd + destionation 
        os.rename (source , destionation)

BulkChange ()
