#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


""" Class that defines a Square from Rectangle class """
class Square(Rectangle):

    """ Method that initializes a Square """
    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    """ Method that returns a string with the area """
    def area(self):

        return super().area()
