#! /usr/bin/python3
import os

LOOP_FLAG = 0

os.chdir("..")
try:
    os.mkdir("anoop")
except FileExistsError:
    print("[*] Program already initialized!")
    LOOP_FLAG = 1

os.chdir("anoop")
os.system("touch anooplog.txt && touch anoopdue.txt && touch anoopamount.txt")
os.system("echo 0 > anoopamount.txt && echo 0 > anoopdue.txt")



os.chdir("..")
try:
    os.mkdir("uday")
except FileExistsError:
    if(LOOP_FLAG==0):
        print("[*] Program already initialized!")
        
os.chdir("uday")
os.system("touch udaylog.txt && touch udaydue.txt && touch udayamount.txt")
os.system("echo 0 > udayamount.txt && echo 0 > udaydue.txt")



os.chdir("..")
try:
    os.mkdir("santhosh")
except FileExistsError:
    if(LOOP_FLAG==0):
        print("[*] Program already initialized!")

os.chdir("santhosh")
os.system("touch santhoshlog.txt && touch santhoshdue.txt && touch santhoshamount.txt")
os.system("echo 0 > santhoshamount.txt && echo 0 > santhoshdue.txt")

if LOOP_FLAG == 0:
    print("[+] Sucessfully initialized the program!")