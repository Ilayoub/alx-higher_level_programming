#!/usr/bin/python3
"""The program defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is exactly an instance of a given class

    Args:
        obj (any): The object to be checked
        a_class (type): The class to match the type of object    Returns:
        If obj is exactly an instance of a_class - True
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
