#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(A):
    noofswaps = 0
    for i in range(len(A)):
        while A[i] != i + 1:
            temp = A[i]
            A[i] = A[A[i] - 1]
            A[temp - 1] = temp
            noofswaps += 1
    return noofswaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
