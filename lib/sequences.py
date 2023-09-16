#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    if (length == 0):
        print([])
    else:
        print(fibonacci[0:length])
