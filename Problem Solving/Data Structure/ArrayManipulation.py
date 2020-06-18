#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    my_array = [0] * (n+1)
    count = 0
    temp = 0
    for first,last,value in queries:
        
        my_array[first-1] += value
        my_array[last] -= value
    
    for item in my_array:
        count += item
        if count > temp:
            temp = count
       
    return temp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
