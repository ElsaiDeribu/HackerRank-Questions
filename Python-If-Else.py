#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 or (not n % 2 and 6 <= n <= 20):
        print("Weird") 
    
    elif not n % 2 and( 2 <= n <= 5 or 20 < n ):
        print("Not Weird")
        
