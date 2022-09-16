#Take in the name, marital status, gender and greet according to wedding status.
def name():
    n = input("Please enter your full name.\n").title().strip()
    first, last = n.split(" ")

def gender():
    g = input("Please enter \"M\" for male and \"F\" for female.\n ")
    g = g.capitalize()

gender()
print(g)
'''
#Invalid error corrected one
name = input("Please enter your full name.\n").title().strip()
first, last = name.split(" ")
gender = input("Please enter \"M\" for male and \"F\" for female.\n" )
gender = gender.capitalize()
if gender == "M" or gender == "F":
    wed = input("Please enter \"Y\" if you are married and \"N\" if you are not married.\n")
    wed = wed.capitalize()
    if wed == "Y" or wed == "N":
        if gender == "F":
            if wed == "Y":
                print(f"Hello Mrs {last}, welcome to our hotel. Would you like a family room?")
            elif wed == "N":
                print(f"Hello Miss {first}, welcome to our hotel. Would you like a single room?")
        elif gender == "M":
            print(f"Hello Mr. {last}, welcome to our hotel. Which room would you like?")
    else:
        print("Invalid input")        

else:    
    print("Invalid input")
    
    

total = 999+235+2315+692+125436+1154554421
#using arguments to insert comma after 3digits
print(f"{total:,}")

'''

