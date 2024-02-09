#!/usr/bin/python3
"""
class of student
"""


class student:
    """represntation of a student"""
    def __init__(self, first_name, last_name, age):
        """initalization of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary description as a json"""
        return self.__dict__
