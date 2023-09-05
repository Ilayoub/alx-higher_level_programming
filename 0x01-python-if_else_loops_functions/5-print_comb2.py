#!/usr/bin/python3

"""The function prints numbers from 0 to 99 in ascending order"""


for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
