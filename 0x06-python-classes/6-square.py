#!/usr/bin/python3
"""Printing the value of the square"""


class Square:
    """instantiate, retrieve, set and printing in a sqaure class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get size"""
        return self.__size

    @property
    def position(self):
        """get position"""
        return self.__position

    @size.setter
    def size(self, value):
        """set size"""
        if (type(value) is not int):
            return TypeError("size must be an integer")
        elif (value < 0):
            return ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """set position"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((type(value[0]) is not int) or (type(value[1]) is not int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
