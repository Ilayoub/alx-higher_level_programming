#!/usr/bin/python3
"""The program writes a string to a text file(UTF8)
   and returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file

    Args:
        filename (str): The file’s name to be written
        text (str): The text to be written to the file
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
