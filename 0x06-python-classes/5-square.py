#!/usr/bin/python3
"""Printing the value of the square"""


class Square:
    """instantiate, retrieve, set and printing in a sqaure class"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            return TypeError("size must be an integer")
        elif (value < 0):
            return ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            print("#" * self.__size)
