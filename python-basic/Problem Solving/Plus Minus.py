#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=neg=zero = 0
    n = len(arr)
    for i in range(n):
        if(arr[i])==0:
            zero+=1
        elif(arr[i]>0):
            pos+=1
        else:
            neg+=1
    zero = zero/n
    pos = pos/n
    neg = neg/n
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(zero))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
