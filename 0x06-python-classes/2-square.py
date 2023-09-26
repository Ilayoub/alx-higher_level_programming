#!/usr/bin/python3
"""The program defines a square(based on 1-square.py)"""


class Square:
    """The program represents a square"""

    def __init__(self, size=0):
        """The program initializes a new Square

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
