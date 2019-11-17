#!/bin/python3
import os

# Complete the factorial function below.
def factorial(n):
    num_list = [x for x in range(1,n+1)]
    ans = 1
    for y in num_list:
        ans *= y
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
