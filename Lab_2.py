###################################################################
# Functions
###################################################################


# Get user to input number between 1 and 100
def PromptForInteger():
    num = int(input("Please enter an integer (1 to 100):"))

    while num < 1 or num > 100:
        num = int(input("Your response must be from 1 to 100, try again: ",
                        "Your response must be from 0 to 8, try again: "))

    return num


# Gather specific user input
def PromptForInteger(minimum, maximum, initMessage, errorMessage):
    num = int(input(str(initMessage)))

    while num < int(minimum) or num > int(maximum):
        if (num < int(minimum) or num > int(maximum)):
            num = int(input(str(errorMessage)))

    return num


# Add contact to a dictionary
def AddNewContact(userContacts):
    name = input("Please enter the name of your friend: ")
    num = PromptForInteger(1000000, 9999999, "What is your friend's 7-digit phone number? ",
                           "That's not 7 digits, try again: ")

    userContacts[name] = num


# Add a dictionary to a dictionary
def AddNewFullContact(userContacts):
    name = input("Please enter the name of your friend: ")
    number = PromptForInteger(1000000, 9999999, "What is your friend's 7-digit phone number? ",
                           "That's not 7 digits, try again: ")
    email = input("What is your friend's email address? ")
    age = PromptForInteger(0, 125, "What is your friend's age? ", "That's not a real age, try again: ")

    holderDict = {'number': number, 'email': email, 'age': age}

    userContacts[name] = holderDict

###################################################################
# Main
###################################################################


exercise = -1
while exercise != 0:
    exercise = PromptForInteger(0, 8, "Which exercise would you like to test (1-8, 0 to exit)? ", "Your response must be from 0 to 8, try again: ")

    #####################################################
    # Exercise 1: Prompt for Integer
    #####################################################
    if exercise == 1:
        print("Running exercise " + str(exercise))
        print(PromptForInteger(1, 100, "Please enter an integer (1 to 100): ",
                               "Your response must be from 1 to 100, try again: "))

    #####################################################
    # Exercise 2: Custom Range
    #####################################################
    elif exercise == 2:
        print("Running exercise " + str(exercise))
        Num = PromptForInteger(-50, 50, "Please enter an integer (-50 to 50): ",
                               "Your response must be from -50 to 50, try again: ")
        print(str(Num))
        Num = PromptForInteger(98, 106, "Please enter your temperature (98 to 106): ",
                               "You must be dead, try again (98 to 106): ")
        print(str(Num))
        Num = PromptForInteger(-25, -1, "Please enter the deduction from your account (-25 to -1): ",
                               "Your response must be from -25 to -1, try again: ")
        print(str(Num))
        Num = PromptForInteger(1, 10, "Please enter a menu selection (1 to 10): ",
                               "You must choose 1 to 10, try again: ")
        print(str(Num))

    #####################################################
    # Exercise 3: Modifying the Exercise Loop
    #####################################################
    elif exercise == 3:
        print("Running exercise " + str(exercise))

    #####################################################
    # Exercise 4: Simple Lists
    #####################################################
    elif exercise == 4:
        print("Running exercise " + str(exercise))
        myList = ["Wallet", "Phone", "Keys"]
        print(myList)
        myList.sort()
        print(myList)
        print(myList[0])
        print(myList[1:])
        print(myList[-1])
        print(myList.index("Keys"))
        myList.append("Tablet")
        print(myList)
        myList.insert(1, "Glasses")
        print(myList)
        myList.remove("Phone")
        print(myList)
        myList.reverse()
        print(myList)

    #####################################################
    # Exercise 5: Display List Elements on Demand and Copying Lists
    #####################################################
    elif exercise == 5:
        print("Running exercise " + str(exercise))
        myList = ["Stan", "Cartman", "Butters", "Kyle", "Kenny"]

        for index, element in enumerate(myList, 0):
            print(index, element)

        Num = PromptForInteger(0, len(myList) - 1, "Choose a name from the list by number: ",
                               "You must choose one of the above numbers, try again: ")
        print("You chose name " + myList[Num])

        newList = myList.copy()
        print(newList)
        myList.remove("Cartman")
        print(myList)
        print(newList)
        newList.remove("Kenny")
        print(myList)
        print(newList)

    #####################################################
    # Exercise 6: Summation
    #####################################################
    elif exercise == 6:
        print("Running exercise " + str(exercise))

        myList = []
        counter = 0

        while counter < 10:
            myList.append(PromptForInteger(1, 100, "Please enter an integer (1 to 100): ",
                                           "Your response must be from 1 to 100, try again: "))
            counter += 1

        print(myList)
        print(sum(myList))

    #####################################################
    # Exercise 7: Simple Dictionary
    #####################################################
    elif exercise == 7:
        print("Running exercise " + str(exercise))
        Dict = {}
        counter = 0

        while counter < 5:
            AddNewContact(Dict)
            counter += 1

        import pprint

        pprint.pprint(Dict)
        print(Dict.keys())
        print(Dict.values())

        finder = input("Whose number do you want?")
        print(Dict.get(finder))

    #####################################################
    # Exercise 8: Nested Dictionaries
    #####################################################
    elif exercise == 8:
        print("Running exercise " + str(exercise))
        Dict = {}
        counter = 0

        while counter < 5:
            AddNewFullContact(Dict)
            counter += 1

        import pprint

        pprint.pprint(Dict)
        print(Dict.keys())
        print(Dict.values())

        finder = input("Whose number do you want?")
        Dictx = Dict.get(finder)
        pprint.pprint(Dictx)
        print(Dictx['email'])



    #####################################################
    # Invalid choice
    #####################################################
    elif exercise == 0:
        exit
