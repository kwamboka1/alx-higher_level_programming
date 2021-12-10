#!/usr/bin/python3
"""class Square: It defines a square by its size"""


class Square:
        """ Method to initialize the square object
        """
    def area(self):
        """ Method that returns the square area of the object
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
