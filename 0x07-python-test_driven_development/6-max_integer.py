#!/usr/bin/python3
"""The program finds the module of the max integer in a list
"""


def max_integer(list=[]):
    """The program to find and return the max integer in a list of integers
        If the list is empty, the function should return None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
