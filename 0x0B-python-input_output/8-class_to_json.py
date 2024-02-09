#!/usr/bin/python3
"""
a function that returns the dict description with simple data structure
"""


def class_to_json(obj):
    """return the dictionary description"""
    return obj.__dict__
