# Andrew McGrath

# Part 1
studentCount = input("How many students are in the class?")  # Read in number of students
# Store valid student data in arrays
realCount = []
students = []
gpas = []
SUM = 0.0

# Read student information from the user
for x in range(1, int(studentCount) + 1, 1):
    name = input("Enter the name of student:")
    if len(name) > 24:
        print("Name of student cannot exceed 24 characters.")
        continue

    gpa = input("Enter the gpa of student:")
    gpa = float(gpa)  # Convert to floating point value
    if (gpa < 0.0) or (gpa > 4.0):
        print("GPA of student must be between 0.0 and 4.0")
        continue

    # If we made it here the student is valid
    students.append(name)
    gpas.append(gpa)
    realCount.append(x)
    SUM += gpa

# Print the header
if len(realCount) > 0:
    print("Number".ljust(10, ' '), end="")
    print("Name".ljust(24, " "), end="")
    print("GPA".ljust(3, " "))
    print("-" * 37)

    # Print valid student information
    for x in range(0, len(students), 1):
        print(str(realCount[int(x)]).ljust(10, ' '), end="")
        print(str(students[int(x)]).ljust(24, " "), end="")
        print(str(gpas[int(x)]).ljust(3, " "))
    print("Average GPA: " + str(SUM/len(realCount)))

# Part 2
keepGoing = True
while keepGoing:
    amountOfChange = int(input("How much change should the customer get?"))  # Found out I can cast to int initially
    if amountOfChange < 0:
        print("Change must be a positive integer")
        continue
    print("Return the following change:")
    # Zero out coin objects
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    # Requirement to use while loops was a nice hint
    # Loop through each coin amount starting with the biggest to reduce the initial value
    # by largest amount (quarters) to smallest (pennies)
    while amountOfChange >= 25:
        amountOfChange -= 25
        quarters += 1

    if quarters:  # Truthy/falsey values
        print(str(quarters) + " quarters")

    while amountOfChange >= 10:
        amountOfChange -= 10
        dimes += 1

    if dimes:
        print(str(dimes) + " dimes")

    while amountOfChange >= 5:
        amountOfChange -= 5
        nickels += 1

    if nickels:
        print(str(nickels) + " nickels")

    while amountOfChange >= 1:
        amountOfChange -= 1
        pennies += 1

    if pennies:
        print(str(pennies) + " pennies")

    # Sub loop to continue the main loop
    while keepGoing:
        userCont = input("Would you like to make more change? (y/Y/n/N)")
        if (userCont == "Y") or (userCont == "y"):
            print("Let's make some more change!")
            break
        elif (userCont == "N") or (userCont == "n"):
            print("Ok, I'll move along to something else...")
            keepGoing = False
        else:
            print("I did not recognize that response")

# Part 3

offYouGo = False

while not offYouGo:
    print("Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.")
    name = input("What is your name?")
    # Question #1
    if (name != "Sir Lancelot of Camelot") and (name != "Sir Robin of Camelot") and \
            (name != "Sir Galahad of Camelot") and (name != "Arthur, King of the Britons"):
        print("You have been cast into the Gorge of Eternal Peril.  Goodbye.")
        continue

    quest = input("What is your quest?")

    # QUESTion #2
    if quest != "To seek the Holy Grail":
        print("You have been cast into the Gorge of Eternal Peril.  Goodbye.")
        continue

    color = input("What is your favorite color?")

    # Question #3
    if (color != "Blue") and (color != "Yellow"):
        print("You have been cast into the Gorge of Eternal Peril.  Goodbye.")
        continue

    print("Right. Off you go")
    offYouGo = True
    exit()
