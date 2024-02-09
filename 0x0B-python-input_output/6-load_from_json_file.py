#!/usr/bin/python3
"""
a function that creats an object from json
"""

import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        return json.loads(content)
