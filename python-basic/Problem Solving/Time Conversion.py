#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    h = int(s[0:2])
    l = s[2:8]
    pick = s[8:10]
    if(pick == 'AM'):
        if(h==12):
            f = '00'
            return(f+l)
        else:
            return(s[0:8])
    else:
        if(h==12):
            return(s[0:8])
        else:
            h = 12+h
            f = str(h)
            return(f+l)
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
