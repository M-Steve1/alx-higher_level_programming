#!/usr/bin/python3
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
def uppercase(str):
    for i in str:
        if i in upper or i in lower:
            print("{}".format(i).capitalize(), end="")
        else:
              print("{}".format(i), end="")
    print()
