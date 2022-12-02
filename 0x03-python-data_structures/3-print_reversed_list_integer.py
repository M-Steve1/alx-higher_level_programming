#!/usr/bin/pythno3


def print_reversed_list_integer(my_list=[]):
    strlen = len(my_list) - 1
    while strlen > -1:
        print("{}".format(my_list[strlen]))
        strlen -= 1
