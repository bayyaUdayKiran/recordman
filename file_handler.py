class Handler:
    def write(self, user, due, today, amount):
        with open("../"+user+"/"+user+"log.txt", "a") as f:
            status = f"Paid: {amount}"
            f.write(f"On {today}: {status},\t\t\t Pay: ₹{due+30}, tommorow\n")

    
    def read(self, user):
        with open("../"+user+"/"+user+"due.txt", "r") as f:
            returnable = f.read()
            return int(returnable)

            