#!/bin/python3
from itertools import groupby
n = int(input())
binary = '{0:b}'.format(n)
groups = groupby(binary)
result = [(label, sum(1 for _ in group)) for label, group in groups]
ans = 0
for x in result:
    if x[0] == '1':
        if x[1] > ans:
            ans = x[1]
print(ans)
