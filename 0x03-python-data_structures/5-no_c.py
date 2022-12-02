#!/usr/bin/python3


def no_c(my_string):
    newstr = ""
    for char in my_string:
        if "C" != char and "c" != char:
            newstr += char
    return newstr
