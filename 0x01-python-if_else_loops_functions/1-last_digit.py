#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
negnumber = number * -1
lastDigit = 0

if number < 0:
    lastDigit = -(negnumber % 10)
else:
    lastDigit = number % 10

message = f"Last digit of {number} is {lastDigit}"

if lastDigit == 0:
    print(f"{message} and is 0")
elif lastDigit < 6:
    print(f"{message} and is less than 6 and not 0")
else:
    print(f"{message} and is greater than 5")
