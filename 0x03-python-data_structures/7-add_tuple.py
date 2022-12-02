#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 1 and len(tuple_b) > 1:
        newtuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
        return newtuple
    elif len(tuple_a) == 1:
        newtuple = tuple_a[0] + tuple_b[0], 0 + tuple_b[1]
        return newtuple
    elif len(tuple_b) == 1:
        newtuple = tuple_a[0] + tuple_b[0], tuple_a[1] + 0
        return newtuple
    else:
        newtuple = tuple_a + tuple_b
        return newtuple
