#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
        l1 = len(note)
        l2 = len(magazine)
        magazine.sort()
        note.sort()
        i = 0
        j = 0
        count = 0
        while i<l1 and j<l2:
                if note[i] == magazine[j]:
                        count += 1
                        i += 1
                j += 1
        if count == l1:
                print ('Yes')
        else:
                print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
