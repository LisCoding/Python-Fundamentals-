# condtionals staments
def bankBalance(amount):
    balance = 1000
    if (amount < balance):
        print("Your balance is less than " + str(balance))
    elif (amount == balance):
        print("Total Balance is " + str(balance))
    else:
        print("you are Total balance is greater than  " + str(balance))

bankBalance(1500)
bankBalance(1000)
bankBalance(500)


#using "A if C else B" stament
def lifeChoices():
    x = "learn"
    y = "learn"
    print "Study hard, Play hard" if x == "live" else "Take a break"
    print "Study hard, Play hard" if y == "learn" else "Take a break"


lifeChoices()
