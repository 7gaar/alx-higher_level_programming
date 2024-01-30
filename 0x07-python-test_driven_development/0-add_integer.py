#!/usr/bin/python3
"""
This is the "0-add_integer" module.
This is a function that returns the sum of 2 integers.
Return: an integer from the addition.
"""


def add_integer(a, b=98):
    """Return an int as result of the addition of a and b.
    Raises:
        TypeError: If either a or b is not an int or float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    result = a + b
    return int(result)
