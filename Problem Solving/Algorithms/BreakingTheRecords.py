#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lc = hc =  0
    hs = ls = scores[0]
    for i in scores:
        if i > hs :
            hs = i
            hc+=1
        if i < ls :
            ls = i
            lc +=1
    return [hc, lc]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
