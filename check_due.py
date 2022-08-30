#! /usr/bin/python3
import sys
user = sys.argv[1]
if((user!="santhosh")and(user!="uday")and(user!="anoop")):
        print("[*] Incorrect username, registered usernames are 'anoop', 'uday', 'santhosh'.")
        sys.exit()
with open("../"+user+"/"+user+"due.txt", "r") as f:
    due = f.read()

if int(due)<=0:
    print("No due!")
else:
    print(f"Due: ₹{str(due)}/-")

to_pay = int(due) + 30
print(f"Pay ₹{str(to_pay)} tommorrow.")