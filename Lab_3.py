# Andrew McGrath
# 02/21/2020
# amcgrat3@uccs.edu
# Script for LAb 3: Regex

###################################################################
# Main
###################################################################

import re

exercise = -1
while exercise != 0:
    exercise = int(input("Which exercise would you like to test (1-8, 0 to exit)? "))

    #####################################################
    # Exercise 1: Validate Simple Zip Codes
    #####################################################
    if exercise == 1:
        zipcode = input("Enter a zip code: \n")

        # Match pattern of 5 digits 0 to 9
        zip = re.search("^([\d]{5})$", zipcode)
        if zip:
            print("Valid")
        else:
            print("Invalid")

    #####################################################
    # Exercise 2: Extended Zip Codes
    #####################################################
    elif exercise == 2:
        zipcode = input("Enter a zip code: \n")

        zip1 = re.search("^([\d]{5})(-[\d]{4})?$", zipcode)

        if zip1:  #
            print("Valid")
        else:
            print("Invalid")

    #####################################################
    # Exercise 3: Numerically Correct Zip Codes
    #####################################################
    elif exercise == 3:
        zipcode = input("Enter a zip code: \n")

        zip1 = re.search("^((([\d][1-9])|([1-9][\d]))[\d]{3}(-[\d]{4})?)$", zipcode)

        if zip1:
            print("Valid")
        else:
            print("Invalid")

    #####################################################
    # Exercise 4: Variable Name Validation
    #####################################################
    elif exercise == 4:
        name = input("Enter a variable name: \n")

        varName = re.search("^([a-zA-Z_][\w]*)$", name)
        if varName:
            print("Valid")
        else:
            print("Invalid")

    #####################################################
    # Exercise 5: Username Validation
    #####################################################
    elif exercise == 5:
        username = input("Enter a username: \n")
        uName = re.search("^([a-zA-Z](([\w]([.]?)))*)$", username)
        if uName:
            print("Valid")
        else:
            print("Invalid")

    #####################################################
    # Exercise 6: Min/Max Length Username Validation
    #####################################################
    elif exercise == 6:
        username = input("Enter a username: \n")
        uName = re.search("^([a-zA-Z](([\w]([.]?)){5,15}))$", username)
        if uName:
            print("Valid")
        else:
            print("Invalid")

    #####################################################
    # Exercise 7: Email Validator
    #####################################################
    elif exercise == 7:
        email = input("Enter a email address: \n")
        mail = re.search("^([a-zA-Z]([\w]|[.][\w])*[@][\w]([\w]|[.][\w])*[.][\w]{2,4})$", email)
        if mail:
            print("Valid")
        else:
            print("Invalid")

    #####################################################
    # Exercise 8: Separate City, State and Zip
    #####################################################
    elif exercise == 8:
        address = input("Enter a city, state and zip: \n")
        matches = re.search("^(?P<City>(([A-Z][a-z]*([.]?)([ ]?)))*), (?P<State>[a-zA-Z]{2}) (?P<Zip>((([0-9][1-9]{4})|([1-9][\d]{4}))(-[\d]{4})?))", address)


        print("City:", matches.group('City'))
        print("State:", matches.group('State'))
        print("Zip:", matches.group('Zip'))

    #####################################################
    # Invalid choice
    #####################################################
    elif exercise == 0:
        exit

    else:
        print("Your response must be from 0 to 8, try again: ")
