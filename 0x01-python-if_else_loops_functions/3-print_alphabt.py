#!/usr/bin/python3

"""The function prints the ASCII alphabet in lowercase"""

for n in range(97, 123):
    if n != 101 and n != 113:
        print("{}".format(chr(n)), end="")
