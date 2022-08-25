#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    Last_digit = number % 10
else:
    Last_digit = ((number * -1) % 10) * -1
output = ("Last digit of {} is {}".format(number, Last_digit))
if Last_digit > 5:
    print(output + " and is greater than 5")
elif Last_digit == 0:
    print(output + " and is 0")
else:
    print(output + " and is less than 6 and not 0")
