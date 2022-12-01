#!/usr/bin/python3
import sys


def count_argv():
    argv_len = len(sys.argv)
    i = 1

    if argv_len == 1:
        print("{} arguments.".format(0))
    elif argv_len == 2:
        print("{} argument:".format(argv_len - 1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argv_len - 1))
        while i < argv_len:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1


if __name__ == '__main__':
    count_argv()
