#!/bin/python

import sys

opts = "<int a> <int b>"


def main(a, b):
    while a != b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
    print(a)


if len(sys.argv) < 2 or sys.argv[1] == '-h':
    print("Usage: {} {}".format(sys.argv[0], opts))
    exit(1)

main(int(sys.argv[1]), int(sys.argv[2]))
