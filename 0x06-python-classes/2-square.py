#!/usr/bin/python3
"""Square class with int private instance attribute"""


class Square:
    """Checking if the attribute size is int and above 0"""

    def __init__(self, size=0):
        if(type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
