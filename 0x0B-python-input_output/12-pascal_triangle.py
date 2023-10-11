#!/usr/bin/python3
"""The program returns a list of lists of integers
   representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n

    Returns a list of lists of integers representing triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles

100-append_after.py
#!/usr/bin/python3
"""The program defines a function that inserts a text file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing
    a given string in a file

    Args:
        filename (str): The file’s name
        search_string (str): The string to search in within the file
        new_string (str): The string to be inserted
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
