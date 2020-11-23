#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total = sum(arr)
    mn = min(arr)
    mx = max(arr)
    print(str(total-mx)+' '+str(total-mn))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
