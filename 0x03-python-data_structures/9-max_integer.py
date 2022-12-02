#!/usr/bin/python3


def max_integer(my_list=[]):
    size = len(my_list)
    temp = 0

    if size == 0:
        return None
    else:
        for i in my_list:
            if i > temp:
                temp = i

    return temp
