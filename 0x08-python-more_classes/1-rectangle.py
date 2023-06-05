#!/usr/bin/python3
"""
A Rectangle class
"""


class Rectangle:
    """
    A rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Intializing a new Rectangle
        Args:
            width(int): The width of the new Rectangle
            height(int): The height of the new Rectngle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get or set the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of width of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self,value):
        """
        Sets the value of height of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
