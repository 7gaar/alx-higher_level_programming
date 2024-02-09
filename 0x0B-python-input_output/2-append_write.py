#!/usr/bin/python3
"""
a function that appends a string at the end of a file
"""


def append_write(filename="", text=""):
    """ appending text to file"""
    with open(filename, "a", encoding="utf-8") as f:
        numchar = f.write(text)
        return numchar
