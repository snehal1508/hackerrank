#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    sorted_arr = sorted(arr)
    diff = []
    for i in range(len(sorted_arr) - 1):
        diff.append(sorted_arr[i+1] - sorted_arr[i])
    value = min(diff)
    result = []
    for i in range(len(sorted_arr) - 1):
        if (sorted_arr[i+1] - sorted_arr[i]) == value:
            result.append(sorted_arr[i])
            result.append(sorted_arr[i+1])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
