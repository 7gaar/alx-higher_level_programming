#!/usr/bin/python3
"""
contains the json string function.
"""

import json


def from_json_string(my_str):
    """return an object"""
    return json.loads(my_str)
