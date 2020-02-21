# Andrew McGrath
# 02/21/2020
# amcgrat3@uccs.edu
# Script for HW 2: Working with dictionaries and drawing shapes

###########################################################################
# Input/Output Functions
###########################################################################


def menu():
    menuItem = 1
    print("*" * 30)
    print("%d - Draw a Rectangle" % menuItem)
    menuItem += 1
    print("%d - Draw a Right Triangle" % menuItem)
    menuItem += 1
    print("%d - Draw an Isosceles Triangle" % menuItem)
    menuItem += 1
    print("%d - Draw a Flipped Isosceles Triangle" % menuItem)
    menuItem += 1
    print("%d - Draw a Diamond" % menuItem)
    menuItem += 1
    print("%d - Draw an Hourglass" % menuItem)
    menuItem += 1
    print("%d - Draw a House" % menuItem)
    menuItem += 1
    print("%d - Add a Student" % menuItem)
    menuItem += 1
    print("%d - Print a Student" % menuItem)
    menuItem += 1
    print("%d - Print all Students" % menuItem)
    menuItem += 1
    print("%d - Quit" % menuItem)
    print("*" * 30)
    return promptForInteger(1, menuItem,
                            "Please make a selection between 1 and %d:" % menuItem,
                            "Your response must be number between 1 and %d, try again." % menuItem)


def promptForInteger(minimum, maximum, message, errorMessage):
    num = (input(str(message + "\n")))
    isValid = False

    # Get user input, catching type errors
    while not isValid:
        try:
            num = int(num)
            while num < int(minimum) or num > int(maximum):
                num = (input(str(errorMessage + "\n")))
                num = int(num)

            isValid = True

        except:
            num = (input(str(errorMessage + "\n")))

    return num


###########################################################################
# Draw Functions
###########################################################################


def drawRectangle(width, height):
    for i in range(0, height):
        print("*" * width)


def drawRightTriangle(size):
    for i in range(1, size + 1):
        print("*" * int(i))


def drawIsoTriangle(size, ignoreFirst=False):
    for i in range(0, size):
        if not ignoreFirst:
            print(' ' * (size - i - 1), end="")
            print('*' * (2 * i + 1))
        else:
            ignoreFirst = False


# Use optional parameters for special cases like diamonds
def drawFlippedIsoTriangle(size, ignoreFirst=False):
    # Reverse the loop
    # We learned in class range generates a list, so we can simply reverse it
    for i in reversed(range(0, size)):
        if not ignoreFirst:
            print(' ' * (size - i - 1), end="")
            print('*' * (2 * i + 1))
        else:
            ignoreFirst = False


###########################################################################
# Handling Functions
###########################################################################
def handleRectangle():
    print("Drawing Rectangle")
    width = promptForInteger(1, 20, "What is the width of your rectangle (1 to 20)?",
                             "Your width must be between 1 and 20, try again.")
    height = promptForInteger(1, 20, "What is the height of your rectangle (1 to 20)?",
                              "Your height must be between 1 and 20, try again.")
    drawRectangle(width, height)


def handleRightTriangle():
    print("Drawing Right Triangle")
    size = promptForInteger(1, 20, "What is the size of your right triangle (1 to 20)?",
                            "Your size must be between 1 and 20, try again.")
    drawRightTriangle(size)


def handleIsoTriangle():
    print("Drawing Isosceles Triangle")
    size = promptForInteger(1, 20, "What is the size of your isosceles triangle (1 to 20)?",
                            "Your size must be between 1 and 20, try again.")
    drawIsoTriangle(size)


def handleFlippedIsoTriangle():
    print("Drawing Flipped Isosceles Triangle")
    size = promptForInteger(1, 20, "What is the size of your flipped isosceles triangle (1 to 20)?",
                            "Your size must be between 1 and 20, try again.")
    drawFlippedIsoTriangle(size)


def handleDiamond():
    print("Drawing Diamond")
    size = promptForInteger(1, 20, "What is the size of your diamond (1 to 20)?",
                            "Your size must be between 1 and 20, try again.")
    drawIsoTriangle(size)
    drawFlippedIsoTriangle(size, True)


def handleHourGlass():
    print("Drawing Hourglass")
    size = promptForInteger(1, 20, "What is the size of your hourglass (1 to 20)?",
                            "Your size must be between 1 and 20, try again.")
    drawFlippedIsoTriangle(size)
    drawIsoTriangle(size, True)


def handleHouse():
    print("Drawing House")
    size = promptForInteger(1, 20, "What is the size of your house (1 to 20)?",
                            "Your size must be between 1 and 20, try again.")
    drawIsoTriangle(size)
    drawRectangle(2 * size - 1, size - 1)


def handleAddStudent(studentDict):
    print("Adding a Student")
    name = input("What is the student's name?" + "\n")

    # Get number of grades
    gradeCount = promptForInteger(1, 10, "How many grades does %s have between 1 and 10?" % name,
                                  "You must enter a number between 1 and 10, try again.")

    gradeList = []
    counter = 0

    # Fill a list with the student's grades
    while counter < gradeCount:
        gradeList.append(promptForInteger(0, 100, "Enter the student's grade between 0 and 100?",
                                          "A grade must be between 0 and 100, try again."))
        counter += 1

    studentDict[name] = gradeList


def printStudent(studentDict):
    print("Print a Student")
    name = input("What is the student's name?" + "\n")

    if name in studentDict:
        print("%s's grades: " % name)
        print("  ", end="")
        print(studentDict[name])
        print("  Average: ", end="")
        print(sum(studentDict[name]) / len(studentDict[name]))

    else:
        print("%s does not exist." % name)


def printAllStudents(studentDict):
    print("Printing all Students")

    for student in sorted(studentDict.keys()):
        print("%s's grades: " % student)
        print("  ", end="")
        print(studentDict[student])
        print("  Average: ", end="")
        print(sum(studentDict[student]) / len(studentDict[student]))

###########################################################################
# Main
###########################################################################


response = 0
studentDict = {}
while response != 11:
    response = menu()

    if response == 1:  # Draw Rectangle
        handleRectangle()
    elif response == 2:  # Draw Right Triangle
        handleRightTriangle()
    elif response == 3:  # Draw Isosceles Triangle
        handleIsoTriangle()
    elif response == 4:  # Draw Flipped Isosceles Triangle
        handleFlippedIsoTriangle()
    elif response == 5:  # Draw Diamond
        handleDiamond()
    elif response == 6:  # Draw Hourglass
        handleHourGlass()
    elif response == 7:  # Draw House
        handleHouse()
    elif response == 8:  # Add a student
        handleAddStudent(studentDict)
    elif response == 9:  # Print a student
        printStudent(studentDict)
    elif response == 10:  # Print all students
        printAllStudents(studentDict)
    elif response == 11:  # Quit
        print("Quitting!")
        exit