#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    
    
    def helper(dig, multiplier):
        
        if len(dig) == 1:
            return dig
            
        sumOfDigits = 0
        
        # the iteration below takes k * len(n) time which is too much
        for digit in dig:
            sumOfDigits += int(digit)
        
        sumOfDigits *= multiplier
            
        sumOfDigits = str(sumOfDigits)
        
        return helper(sumOfDigits, 1)
    
        
    return helper(n, k)
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
