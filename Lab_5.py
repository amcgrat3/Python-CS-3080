import re


# Class for cubing numbers
class Cubes:
    def __init__(self):
        self.num = 1
        self.cube = 1

    def __iter__(self):
        return self

    def __next__(self):
        returnNum = self.cube
        self.num += 1
        self.cube = self.num ** 3
        return returnNum


# Class for cubing numbers
class Primes:
    def __init__(self):
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):
        returnNum = self.num

        prime = self.num + 1
        while True:
            # Regex for prime numbers
            matcher = re.match(r'^1?$|^(11+?)\1+$', '1' * prime) == None

            if matcher:
                self.num = prime
                return returnNum
            else:
                prime += 1


# Function to generate odd negative numbers
def genOddNegatives():
    num = -1
    # Infinite Loop
    while True:
        yield num

        num -= 1
        while num % 2 == 0:
            num -= 1


# Function to generate Fib. numbers
def genFibNumbers():
    ret = 1
    a = 0
    b = 0

    # Infinite Loop
    while True:
        yield ret
        b = a
        a = ret
        ret = a + b


# Use nbrValues as the number of values to generate for Exercises 1-5
nbrValues = int(input("What is the number of items you want to generate?\n"))

###############################################################
# Exercise 1 - Cubed Values from a Generator Object
###############################################################
print("%-16s" % "Cubes: ", end=' ')

c = Cubes()

for i in range(nbrValues):
    print(next(c), end=" ")

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 2 - Prime Values from a Generator Object
###############################################################
print("\n%-16s" % "Primes: ", end=' ')

p = Primes()

for i in range(nbrValues):
    print(next(p), end=" ")

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 3 - Odd Negative Values from a Generator Function
###############################################################
print("\n%-16s" % "Odd Negatives: ", end=' ')

gen = genOddNegatives()

for i in range(nbrValues):
    print(next(gen), end=" ")

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 4 - Fibonacci Values from a Generator Function
###############################################################
print("\n%-16s" % "Fibonacci: ", end=' ')

gen = genFibNumbers()

for i in range(nbrValues):
    print(next(gen), end=" ")

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 5 - Triangular Values from a Generator Expression
###############################################################
print("\n%-16s" % "Triangular: ", end=' ')

numList = range(1, nbrValues + 1)
# n * (n + 1) / 2
triangles = (x * (x + 1) / 2 for x in numList)
for i in numList:
    print(int(next(triangles)), end=' ')

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 6 - Making Ice Cream with Decorators
###############################################################
print("\n%-16s" % "Ice Cream: ")


def addBrownie(func):
    def wrapper():
        print("Adding Brownie")
        func()

    return wrapper


def addBanana(func):
    def wrapper():
        print("Adding Banana")
        func()

    return wrapper


def addSyrup(func):
    def wrapper():
        func()
        print("Adding Chocolate Syrup")

    return wrapper


def addNuts(func):
    def wrapper():
        func()
        print("Adding Nuts")

    return wrapper


def addCherry(func):
    def wrapper():
        func()
        print("Adding the Cherry on Top!")

    return wrapper


# DO NOT MODIFY ANYTHING BELOW THIS LINE
def addIceCream():
    print("Adding Ice Cream")


# Add decorators to this call
addIceCream = addCherry(addNuts(addSyrup(addBrownie(addBanana(addIceCream)))))

addIceCream()

###############################################################
# Exercise 7 - Custom Toppings using Decorators and Arguments
###############################################################
print("\n%-16s" % "Custom Toppings: ")


def baseItem(item):
    def add(func):
        def wrapper():
            print(item)
            func()

        return wrapper

    return add


def topItem(item):
    def add(func):
        def wrapper():
            func()
            print(item)

        return wrapper

    return add


@baseItem(item="Adding Brownie")
@baseItem(item="Adding Banana")
@topItem(item="Adding the Cherry on Top!")
@topItem(item="Adding Nuts")
@topItem(item="Adding Chocolate Syrup")
# DO NOT MODIFY ANYTHING BELOW THIS LINE
def addIceCream2():
    print("Adding Ice Cream")


addIceCream2()
