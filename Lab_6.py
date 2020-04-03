# Andrew McGrath
# 04/03/2020
# amcgrat3@uccs.edu
# Script for Lab 6, Web Scraping and Time

import requests
import bs4
import time
import datetime

###################################################################
# Main
###################################################################

exercise = -1
while exercise != 0:
    exercise = int(input("Which exercise would you like to test (1-6, 0 to exit)? "))

    #####################################################
    # Exercise 1:
    #####################################################
    if exercise == 1:
        req = requests.get("https://automatetheboringstuff.com/files/rj.txt")  # Get the text file

        # Check the status code of the request
        if req.status_code == requests.codes.ok:
            print("Everything is OK")
        else:
            print("Something bad happened")

        # Print some of the stuff we got from the URL
        print(len(req.text))
        print(req.text[:47])

    #####################################################
    # Exercise 2:
    #####################################################
    elif exercise == 2:
        req = requests.get("https://automatetheboringstuff.com/files/rj.txt")
        req.raise_for_status()  # Checks for 'ok' status

        # Open file to write
        file = open("Lab_6_File.txt", "wb")

        # Put web contents into file
        for chunk in req.iter_content(100000):
            file.write(chunk)

        # Close and reopen the file
        file.close()
        file = open("Lab_6_File.txt", "r")

        content = file.readlines()  # Read lines from file

        # Get lines 50-59
        for line in content[50:60]:
            print(line, end='')

        file.close()

    #####################################################
    # Exercise 3:
    #####################################################
    elif exercise == 3:
        req = requests.get("https://www.futureme.org/")
        req.raise_for_status()  # Checks for 'ok' status

        # bs4 call from pptx
        soup = bs4.BeautifulSoup(req.text, features="html.parser")

        Title = soup.select("title")  # Select by title tag

        print(Title)
        print(Title[0].getText())

    #####################################################
    # Exercise 4:
    #####################################################
    elif exercise == 4:
        req = requests.get("http://hmpg.net/")
        req.raise_for_status()  # Checks for 'ok' status

        # bs4 call from pptx
        soup = bs4.BeautifulSoup(req.text, features="html.parser")

        paragraphs = soup.select("p")  # Select by p tag

        # Print paragraph elements
        for p in paragraphs:
            print("-" * 40)
            print(p)

        # Print paragraph text
        for p in paragraphs:
            print("-" * 40)
            print(p.getText())

    #####################################################
    # Exercise 5:
    #####################################################
    elif exercise == 5:
        req = requests.get("https://www.daylightofdarkness.com/")
        req.raise_for_status()  # Checks for 'ok' status

        # bs4 call from pptx
        soup = bs4.BeautifulSoup(req.text, features="html.parser")

        images = soup.select("img")  # Select by img tag, found by inspect element

        for image in images:
            print(image.attrs['src'])  # src found by inspect element

    #####################################################
    # Exercise 6:
    #####################################################
    elif exercise == 6:
        secondsPastEpoch = int(input("How many seconds since epoch? "))

        # Print the different time values
        print(time.gmtime(secondsPastEpoch))  # Greenwich Mean Time
        print(time.localtime(secondsPastEpoch))  # Local Time
        print(datetime.datetime.fromtimestamp(secondsPastEpoch))  # Default Time
        print(datetime.datetime.fromtimestamp(secondsPastEpoch).year)  # Year
        print(datetime.datetime.fromtimestamp(secondsPastEpoch).month)  # Month
        print(datetime.datetime.fromtimestamp(secondsPastEpoch).hour)  # Day

        # UTC Time is 7 hours ahead of Colorado Time, so just add 7 hours to the time
        print(datetime.datetime.fromtimestamp(secondsPastEpoch) + datetime.timedelta(hours=7))

        # Add 30 days to the time
        print(datetime.datetime.fromtimestamp(secondsPastEpoch) + datetime.timedelta(days=30))

        # Format Output
        print(datetime.datetime.fromtimestamp(secondsPastEpoch).strftime("%B %d, %Y") + " is ", end='')

        # Date for 9/11
        nineEleven = datetime.datetime(2001, 9, 11, 0, 0, 0)
        givenTime = datetime.datetime.fromtimestamp(secondsPastEpoch)

        if givenTime < nineEleven:
            print("before 9/11")
        else:
            print("after 9/11")

    #####################################################
    # Invalid choice
    #####################################################
    elif exercise == 0:
        exit()

else:
    print("Your response must be from 0 to 6, try again: ")
