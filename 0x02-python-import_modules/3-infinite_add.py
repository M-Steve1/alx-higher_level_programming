#!/usr/bin/python3
import sys


def add_argv():
    argv_len = len(sys.argv)
    i = 1
    result = 0

    if argv_len == 1:
        print(0)
    else:
        while i < argv_len:
            result += int(sys.argv[i])
            i += 1
        print("{}".format(result))


if __name__ == '__main__':
    add_argv()
