#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    a = 0
    b = 1
    for i in range(length):
        sequence.append(a)
        next_num = a + b
        a = b
        b = next_num
    print(sequence)

    