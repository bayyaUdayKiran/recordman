#! /usr/bin/python3
import sys
import datetime
import file_handler as fh
import os

MIN_PAY = 30


if __name__ == "__main__":
    handler = fh.Handler()

    #Handle username input..
    user = sys.argv[1]
    if((user!="santhosh")and(user!="uday")and(user!="anoop")):
        print("[*] Incorrect username, registered usernames are 'anoop', 'uday', 'santhosh'.")
        sys.exit()

    #Handle paid amount input..
    amount = sys.argv[2]
    try:
        amount = int(amount)
    except ValueError:
        print("[*] Paid amount should be an integer.")
        sys.exit()
    if amount<0:
        print("[*] Negative amount isn't accepted!")
        sys.exit()

    #Update user's balance..
    with open("../"+user+"/"+user+"amount.txt", "r") as f:
        data = f.read()
    with open("../"+user+"/"+user+"amount.txt", "w") as f:
        upd_data = int(data) + amount
        f.write(str(upd_data))

    #Driver code..
    due = MIN_PAY + handler.read(user)

    if amount == due:
        due_amount = 0
    elif amount < due:
        due_amount = due-amount
    else:
        advance = amount - due
        due_amount = -advance

    handler.write(user, due_amount, datetime.date.today(), amount)
    with open("../"+user+"/"+user+"due.txt", "w") as f:
        f.write(str(due_amount))

    with open("../"+user+"/"+user+"amount.txt", "r") as f:
        tot_amount = f.read()
    filename = "../"+user+"/"+user+"log.txt"
    print(f"[+] To check your payment statement view, {os.path.abspath(filename)}")
    print(f"[+] Till now, you've paid ₹{tot_amount}")
    print(f"[+] You've to pay ₹{due_amount+MIN_PAY} tommorrow")

    




    
