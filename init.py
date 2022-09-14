#! /usr/bin/python3
import os
import sys

LOOP_FLAG = 0
user = sys.argv[1]

os.chdir("..")
try:
    os.mkdir(user)
except FileExistsError:
    print("[*] Program already initialized!")
    LOOP_FLAG = 1

os.chdir(user)
os.system("touch log.txt && touch due.txt && touch amount.txt")
os.system("echo 0 > amount.txt && echo 0 > due.txt")


if LOOP_FLAG == 0:
    print("[+] Sucessfully initialized the program!")