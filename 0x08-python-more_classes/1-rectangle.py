#!/usr/bin/python3
""" define a rectangle class """


class Rectangle:
    """ Represnts  a rectangle """
    def __init__(self, width = 0, height = 0):
        """ Initianzation of a new rectangle
        Arguments:
        width: width of rectangle
        height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            TypeError('width must be an integer')
        if value < 0:
            ValueError('width must be >= 0')
        self.width = value

        @property
        def height(self):
            """return height"""
            return self.__height
        
        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                TypeError('height must be an integer')
            if value < 0:
                ValueError('height must be an integer')
            self.__height = value
