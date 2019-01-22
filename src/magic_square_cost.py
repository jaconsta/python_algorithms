#!/bin/python3

import math
import os
import random
import re
import sys

def is_even(n):
    return n%2 == 0

def in_verticals (a, b):
    return bool(a==1) ^ bool(b==1)

def unfold_square (s):
    unfolded = []
    for index_x, x in enumerate(s):
        for index_y, y in enumerate(x):
            if not (index_x == index_y == 1):
                unfolded.append(y)
    return unfolded

def rotate_vector (v):
    steps = (-3, 3, 0, -2, 4, 1, -1, 5, 2)
    v.insert(4, 5)
    rotated = list(range(9))
    for step, val in zip(steps, v):
        rotated[step] = val
    rotated.pop(4)
    return rotated

# Ideal magig square
# 2 9 4    4 3 8    4 9 2
# 7 5 3    9 5 1    3 5 7
# 6 1 8    2 7 6    8 1 6
open_magic_square = [ 2, 9, 4, 7, 3, 6, 1, 8 ]
open_magic_square_inv = [ 4, 9, 2, 3, 7, 8, 1, 6 ]
# Complete the formingMagicSquare function below.
def formingMagicSquare(s):

    unf_s = unfold_square(s)
    min_cost = 99999
    for i in range(4):
        partial_cost = sum([abs(a-b) for a,b in zip(unf_s, open_magic_square)])
        print(partial_cost)
        if partial_cost < min_cost:
            min_cost = partial_cost
        unf_s = rotate_vector(unf_s)

    for i in range(4):
        partial_cost = sum([abs(a-b) for a,b in zip(unf_s, open_magic_square_inv)])
        print(partial_cost)
        if partial_cost < min_cost:
            min_cost = partial_cost
        unf_s = rotate_vector(unf_s)
    min_cost += abs(5 - s[1][1])

    return min_cost

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = [
      [5, 9, 2],
      [3, 5, 7],
      [8, 1, 5]
    ]

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print('************************')
    print(result)
    print('************************')

    # s2 = [
    #     [2, 2, 7],
    #     [8, 6, 4],
    #     [1, 2, 9]
    #     ]
    #
    # result2 = formingMagicSquare(s2)
    # print('************************')
    # print(result2)
    # print('************************')
    #
    #
    # s3 = [
    #     [9, 9, 9],
    #     [9, 9, 9],
    #     [9, 9, 9]
    #     ]
    #
    # result3 = formingMagicSquare(s3)
    # print('************************')
    # print(result3)
    # print('************************')
    #
    # s4 = [
    #     [5, 5, 5],
    #     [5, 5, 5],
    #     [5, 5, 5]
    #     ]
    #
    # result4 = formingMagicSquare(s4)
    # print('************************')
    # print(result4)
    # print('************************')

    # fptr.write(str(result) + '\n')

    # fptr.close()
