#!/usr/bin/python3
import hidden_4


def print_hidden():
    file_info = dir(hidden_4)
    for file_name in file_info:
        if file_name[:2] != "__":
            print(file_name)


if __name__ == "__main__":
    print_hidden()
