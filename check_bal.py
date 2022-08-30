#! /usr/bin/python3
import sys

user = sys.argv[1]
if((user!="santhosh")and(user!="uday")and(user!="anoop")):
        print("[*] Incorrect username, registered usernames are 'anoop', 'uday', 'santhosh'.")
        sys.exit()
with open("../"+user+"/"+user+"amount.txt") as f:
    bal = f.read()

print(f"Till now you've paid ₹{bal}/-")