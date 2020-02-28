# Andrew McGrath
# 02/28/2020
# amcgrat3@uccs.edu
# Script for HW 3: Loading and query csv of Movies

import Shape
import Rectangle
import Triangle

from Shape import *
from Rectangle import *
from Triangle import *

shapes = []


###########################################################################
# Input/Output Functions
###########################################################################
def menu():
    menuItem = 1
    print("*" * 30)
    print("%d - Add a Shape" % menuItem)
    menuItem += 1
    print("%d - Add a Rectangle" % menuItem)
    menuItem += 1
    print("%d - Add a Triangle" % menuItem)
    menuItem += 1
    print("%d - Print all Shapes" % menuItem)
    menuItem += 1
    print("%d - Quit" % menuItem)
    print("*" * 30)
    return promptForInteger(1, menuItem,
                            "Please make a selection between 1 and %d:" % menuItem,
                            "Your response must be number between 1 and %d, try again." % menuItem)


def promptForInteger(minimum, maximum, message, errorMessage):
    value = int(input(message + "\n"))
    while value < minimum or value > maximum:
        value = int(input(message + "\n"))
    return value  # This is stub line to allow the code to run


###########################################################################
# Handling Functions
###########################################################################
def handleShape(shapes):
    print("Add a shape")
    shape = Shape()
    shapes.append(shape)


def handleRectangle(shapes):
    print("Add a rectangle")
    height = promptForInteger(1, 20, "Please enter the height between 1 and 20:",
                              "Your response must be number between 1 and 20:")
    width = promptForInteger(1, 20, "Please enter the width between 1 and 20:",
                             "Your response must be number between 1 and 20:")
    shape = Rectangle(height, width)
    shapes.append(shape)

def handleTriangle(shapes):
    print("Add a triangle")
    base = promptForInteger(1, 20, "Please enter the base between 1 and 20:",
                            "Your response must be number between 1 and 20:")
    shape = Triangle(base)
    shapes.append(shape)


def handlePrint(shapes):
    print("Print all the shapes")
    for shape in shapes:
        shape.Draw()


###########################################################################
# Main
###########################################################################
response = 0
shapes = []

while response != 5:
    response = menu()

    if response == 1:  # Add a Shape
        handleShape(shapes)
    elif response == 2:  # Add a Rectangle
        handleRectangle(shapes)
    elif response == 3:  # Add a Triangle
        handleTriangle(shapes)
    elif response == 4:  # Print all the Shapes
        handlePrint(shapes)
    elif response == 5:  # Quit
        print("Quitting!")
        exit