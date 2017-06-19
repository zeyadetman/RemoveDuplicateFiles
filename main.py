import os
import hashlib
import sys
files = []

def hashing(Filepath):
    with open(Filepath, 'rb') as f:
        HashedFile = hashlib.sha256(f.read()).hexdigest()
        return HashedFile

PFfiles = {}

filePath = input()
PFofFile = hashing(filePath)

default_path = input()

for item in os.listdir(default_path):
    Npath = default_path+'/'+item
    files.append(Npath)

for item in files:
    if os.path.isfile(item) is True:
        if item != filePath:
            PFfiles[item] = hashing(item)

for path,PF in PFfiles.items():
    if PFofFile == PF:
        print ("We found this "+ path)
        print ("\nWanna Remove ? [Y|n]")
        choice = input()
        print (choice)
        if choice[0] == 'y' or choice[0] == 'Y':
            os.remove(path)
            print ("Removed!")
        elif choice[0] == 'n' or choice[0] == 'N':
            print ("OK, it's your hard capacity!")
