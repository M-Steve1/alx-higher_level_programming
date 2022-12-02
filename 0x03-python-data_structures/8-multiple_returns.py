#!/usr/bin/python3


def multiple_returns(sentence):
    size = len(sentence)
    if size == 0:
        return None
    else:
        firstchar = sentence[0]
        return size, firstchar
