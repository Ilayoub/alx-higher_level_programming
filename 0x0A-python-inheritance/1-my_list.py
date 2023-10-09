#!/usr/bin/python3
"""The program defines an inherited MyList from list"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Prints a list in ascending sort"""
        print(sorted(self))
