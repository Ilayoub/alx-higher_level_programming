#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """The program executes a function safely

    Args:
        fct: The function to be executed
        args: The arguments for function

    Returns:
        If an error occurs - None
        Otherwise - the result of the call to function
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
