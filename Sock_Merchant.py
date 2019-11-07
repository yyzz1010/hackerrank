#!/bin/python3
import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    freq_dict = {}
    for x in ar:
        if x not in freq_dict:
            freq_dict[x] = 1
        else:
            freq_dict[x] += 1
    
    count_list = []
    for k,v in freq_dict.items():
        if freq_dict[k] >= 2:
            count_list.append(v)
    
    return sum([y//2 for y in count_list])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
