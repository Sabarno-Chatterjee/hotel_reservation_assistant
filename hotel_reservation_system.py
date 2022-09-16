#Take in the name, marital status, gender and greet according to wedding status.

name = input("Please enter your full name.\n").title().strip()
first, last = name.split(" ")

gender = input("Please enter \"M\" for male and \"F\" for female.\n " )
gender = gender.capitalize()
if gender != "M" or gender != "F":
    print("Invalid input")
    gender = input("Please enter \"M\" for male and \"F\" for female, again.\n")
    gender = gender.capitalize()

wed = input("Please enter \"Y\" if you are married and \"N\" if you are not married.\n")
wed = wed.capitalize()
if wed != "Y" or wed != "N":
    print("Invalid input")
    wed = input("Please enter \"Y\" if you are married and \"N\" if you are not married, again.\n")
    wed = wed.capitalize()

print(wed)
if gender == "F":
    if wed == "Y":
        print(f"Hello Mrs {last}, welcome to our hotel. Would you like a family room?")
    elif wed == "N":
        print(f"Hello Miss {first}, welcome to our hotel. Would you like a single room?")
elif gender == "M":
    print(f"Hello Mr. {last}, welcome to our hotel. Which room would you like?")


