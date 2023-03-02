#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
     
    last = arr[-1]
    
    ptr = n - 1
    
    while ptr > 0 and arr[ptr - 1] > last:
        arr[ptr] = arr[ptr - 1]
        print(*arr)
        ptr -= 1
        
    arr[ptr] = last
    print(*arr)
    
        
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
