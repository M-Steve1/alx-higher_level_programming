#!/usr/bin/python3
j = 1
for i in "abcdefghijklmnopqrstuvwxyz"[::-1]:
    if j % 2 == 0:
        i = i.upper()
    print("{}".format(i), end="")
    j += 1
