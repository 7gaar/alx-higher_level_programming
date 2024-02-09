#!/usr/bin/python3
"""
a function that writes a string to text file.
"""


def write_file(filename="", text=""):
    """return the number of chars"""
    with open(filename, "w", encoding="utf-8") as f:
        numchar = f.write(text)
        return numchar
