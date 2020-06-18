#!/bin/python3

import os
import sys
from datetime import *
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    t_splt = s.split(':')
    if t_splt[2][2:] == 'PM' and t_splt[0] != '12':
        t_splt[0] = str(12+ int(t_splt[0]))
    elif int(t_splt[0])==12 and t_splt[2][2:] == 'AM':
        t_splt[0] = '00'
    t_splt[2] = t_splt[2][:2]
    return ':'.join(t_splt)
    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
