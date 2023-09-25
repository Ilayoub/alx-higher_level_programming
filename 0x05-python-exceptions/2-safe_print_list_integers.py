#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """The program prints the first x elements of a list and only integers

    Args:
        my_list (list): The list from where to print elements
        x (int): The number of elements of my_list to be printed

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
