#!/usr/bin/python3
"""
a function that writes an object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """object to a text file using JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        text = json.dumps(my_obj)
        f.write(text)
