#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    arr=[]
    answerarray=[]
    rows=math.floor(math.sqrt(len(s)))
    cols=math.ceil(math.sqrt(len(s)))
    if rows*cols<len(s):
            rows=cols
    for j in range(rows):
        arr.append(s[cols*j:(cols*j)+cols])
    for x in range(cols):
            string=""
            for y in range(rows):
              if x<len(arr[y]):
                    string+=arr[y][x]
            answerarray.append(string+" ")
    return "".join(answerarray)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
