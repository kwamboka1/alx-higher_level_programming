#!/usr/bin/python3
for number in range(0, 90):
        if number % 10 > number / 10:
                if number != 89:
                        print("{:02d}, ".format(number), end='')
                else:
                        print("{:02d}".format(number))
