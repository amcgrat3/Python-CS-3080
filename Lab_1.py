# Create variables
a = 248
b = 27
filler = "*"

# Do some arithmetic
print(str(a + b))
print(str(a - b))
print(str(a * b))
print(str(a / b))
print(str(a // b))
print(str(a % b))
print(str(a ** b))
print(filler * 67)

# User Input Time
name = input("Please enter your name:")
print("Hello, " + name)
print(filler * 42)

a, b = input("Enter two large numerical values:").split()
a = int(a)  # We treat these as integers for a while
b = int(b)  # So store them as such to save casts
print("Adding " + str(a) + " + " + str(b) + " = " + str(a + b))
print(filler * 59)

# Boolean Logic
aIsGreater = False
if a > b:
    print(str(a) + " is greater than " + str(b))
    aIsGreater = True
else:
    print(str(a) + " is not greater than " + str(b))

if (a % 2) == 0:
    print(str(a) + " is even")
else:
    print(str(a) + " is not even")

if aIsGreater:
    if a % b == 0:
        print(str(b) + " is a factor of " + str(a))
    else:
        print(str(b) + " is not a factor of " + str(a))
else:
    if b % a == 0:
        print(str(a) + " is a factor of " + str(b))
    else:
        print(str(a) + " is not a factor of " + str(b))
print(filler * 26)

# Repeated Actions
c = input("Enter a small numerical values not equal to 1:")
c = int(c)
factorCounter = 0

for x in range(c, b + 1, c):
    print((str(x)), end=" ")
print()
for x in range(b, c - 1, -c):
    print((str(x)), end=" ")
print()
for x in range(1, a + 1, 1):
    if a == x:
        print((str(x)), end=" ")
    elif a % x == 0:
        print((str(x)), end=", ")
        factorCounter += 1
print()
if factorCounter == 1:
    print(str(a) + " is a prime number")
else:
    print(str(a) + " is not a prime number")
