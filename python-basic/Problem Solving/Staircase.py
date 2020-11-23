#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    
    temp = 1
    for i in range(n):
        a = ''
        for j in range(n-temp):
            a = a+' '
        for k in range(temp):
            a = a+'#'
        temp+=1
        print(a)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
