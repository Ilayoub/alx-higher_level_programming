#!/usr/bin/python3

if __name__ == "__main__":
    """The program prints all the names defined by the compiled hidden_4.pyc"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
