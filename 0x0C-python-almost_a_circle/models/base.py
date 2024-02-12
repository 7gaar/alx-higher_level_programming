#!/usr/bin/python3
"""
class Base
"""
import json


class Base:
    """ a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base.
        Args:
            id : the identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string represntation.
        Args:
            list_dictionaries : is a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the json string representation,
        Args:
            json_string : a JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string represntation of list_objs.
        Args:
            list_objs : is a list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_f:
            if list_objs is None:
                json_f.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                json_f.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes.
        Args:
            **dictionary (dict): value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return the list of instances.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
