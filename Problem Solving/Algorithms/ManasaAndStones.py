#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    l_itr=n-1
    h_itr=0
    l=[]
    no=0
    while(n):
        no=l_itr*a + h_itr*b
        if no not in l:
            l.append(no)
        no=0
        l_itr-=1
        h_itr+=1
        n-=1
    if a>b:
        l.reverse()

    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
