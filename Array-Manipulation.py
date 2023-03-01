#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    
    arr = [0] * (n + 1)
    
    
    for i in range(len(queries)):
        arr[queries[i][0] - 1] += queries[i][2] 
        arr[queries[i][1]] -= queries[i][2] 
    
        
        
    curr = 0
    largest = 0
    
    
    for i in range(len(arr)):
        curr += arr[i]
        largest = max(curr, largest)
        
    return largest
        
        
        
        
        
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
