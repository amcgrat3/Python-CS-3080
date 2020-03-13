# Andrew McGrath
# 03/12/2020
# amcgrat3@uccs.edu
# Script for HW4, timing self coded function against built in python functions

from functools import wraps
from time import time


#######################################
# Timing Tools
#######################################

# Decorator to time to function it's attached to
def timeIt(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        start = time()
        # Keep running the passed function
        for num in range(1, 10000):
            func(*args, **kwds)
        end = time()
        name = func.__name__
        runTime = (end - start) * 1000

        # Output function information
        print(str(name).ljust(20, " ") + ":", end="")
        print("{:.3f}".format(runTime).rjust(10, " ") + " ms")
        return runTime

    return wrapper


# Takes in a list of functions and compares the time it takes them to run
def timeCompare(funcList, data):
    name = ""
    timer = 99999  # Completely arbitrary large number
    for func in funcList:
        timing = func(data)
        if timing < timer:
            timer = timing
            name = func.__name__

    print(str(name) + " is the best")

#######################################
# Test String Concatenation versus Join
#######################################


@timeIt
def stringConcatenator(words):
    total = ""
    for word in words:
        total += word + " "
    total = total[:-1]
    return total;


@timeIt
def stringJoiner(words):
    total = " "
    return total.join(words)


# A collection of words that will be used
# to test Concatenation and Joining
words = []
for i in range(100, 300):
    words.append(str(i))

# Use words as the list of words to put together into a single string
timeCompare([stringConcatenator, stringJoiner], words)

# Extra print to space out output
print()


#######################################
# Test String Formatting
#######################################

@timeIt
def stringPercent(words):
    totalString = '%s %s %s %s %s %s %s %s %s %s %s %s %s' % (words[0], words[1], words[2], words[3], words[4], words[5],
                                                             words[6], words[7], words[8], words[9], words[10], words[11]
                                                             , words[12])
    return totalString


@timeIt
def stringFormat(words):
    totalString = '{} {} {} {} {} {} {} {} {} {} {} {} {}'.format(words[0], words[1], words[2], words[3], words[4],
                                                                  words[5],words[6], words[7], words[8], words[9],
                                                                  words[10], words[11], words[12])
    return totalString


@timeIt
def stringF(words):
    totalString = f"{words[0]} {words[1]} {words[2]} {words[3]} {words[4]} {words[5]} {words[6]} {words[7]} {words[8]} " \
                  f"{words[9]} {words[10]} {words[11]} {words[12]}"

    return totalString


# A collection of 13 long strings that will be used to test
# the 3 formatting styles
words = ["Fourscore and seven years ago our fathers brought forth,",
         "on this continent, a new nation, conceived in liberty,",
         "and dedicated to the proposition that all men are created equal. ",
         "Now we are engaged in a great civil war, testing whether that nation,",
         "or any nation so conceived, and so dedicated, can long endure. ",
         "We are met on a great battle-field of that war. ",
         "We have come to dedicate a portion of that field,",
         "as a final resting-place for those who here gave their lives, "
         "that that nation might live. ",
         "It is altogether fitting and proper that we should do this. ",
         "But, in a larger sense, we cannot dedicate, ",
         "we cannot consecrate—we cannot hallow—this ground.",
         "The brave men, living and dead, who struggled here, ",
         "have consecrated it far above our poor power to add or detract. "]

# Use words as the list of words to format
timeCompare([stringPercent, stringFormat, stringF], words)

# Extra print to space out output
print()


#######################################
# Test List Building
#######################################

class ListRangeObject:
    def __init__(self, maxi):
        self.val = 1
        self.max = maxi

    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= max:
            returnNum = self.val
            self.val += 1
            return returnNum
        else:
            raise StopIteration

@timeIt
def listRange(max):
    return sum(range(0, max + 1))


@timeIt
def listComprehension(max):

    return sum([i for i in range(0, max + 1)])


@timeIt
def listIterator(max):
    x = ListRangeObject(max)
    return sum(x)

def Generator(max):
    num = 1
    # Infinite Loop
    while num < max + 1:
        yield num
        num += 1

@timeIt
def listGenerator(max):
    return sum(Generator(max))


@timeIt
def listExpression(max):
    return sum((n for n in range(1, max + 1)))


max = 100

# Use max as the number of items to generate
timeCompare([listRange, listComprehension, listIterator, listGenerator, listExpression], max)

print()
