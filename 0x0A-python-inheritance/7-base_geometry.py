#!/usr/bin/python3
""" Class that defines the attributes of Geometric Shapes """


class BaseGeometry:
    """ A Method that defines the area of a geomtric shape"""

    def area(self):

        raise Exception("area() is not implemented")

    """ Method that recieves the value property

        Árgs:
            name: name of the object
            value: value of the property

    """
    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
