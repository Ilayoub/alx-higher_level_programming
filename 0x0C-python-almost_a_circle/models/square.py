#!/usr/bin/python3
"""The program defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square

        Args:
            size (int): The new square’s size 
            x (int): The x coordinate of the new square
            y (int): The y coordinate of the new square
            id (int): The new square’s identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets/sets the square’s size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square

        Args:
            *args (ints): New attribute values.
                - The first argument represents id attribute
                - The second argument represents size attribute
                - The third argument represents x attribute
                - The forth argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the square’s dictionary representation"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns the square’s print() and str() representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
