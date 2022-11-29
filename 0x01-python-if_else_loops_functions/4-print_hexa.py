#!/usr/bin/python3
j = 0
for i in range(99):
    if i > 9 and i <= 15:
        print("{} = 0x{}".format(i, "abcdef"[j]))
        j += 1
    else:
        print("{} = 0x{}".format(i, i))
