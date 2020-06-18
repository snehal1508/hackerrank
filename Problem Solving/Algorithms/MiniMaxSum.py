#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    li = sorted(arr)
    min_ = sum([li[i] for i in range(4)])
    max_ = sum([li[i] for i in range(1,5)])
    print(min_, max_)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
