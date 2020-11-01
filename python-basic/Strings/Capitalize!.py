#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name = list(s)
    final=''
    for i in range(len(name)):
        if(name[i]==' '):
            final = final+name[i]
        elif(i==0 or name[i-1]==' '):
            final = final+name[i].upper()
        else:
            final = final+name[i]

        
    return final
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
