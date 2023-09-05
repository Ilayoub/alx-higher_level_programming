#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
mod = number % 10 if numer > 10 else numer % -10
print(
	"Last digit of {:d} is {:d} and is "
	.format(number, digit), end="")
if mod > 5:
    print("greater than 5")
elif mod == 0:
    print("0")
else:
    print("less than 6 and not 0")
