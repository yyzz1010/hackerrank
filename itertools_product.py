from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = product(a, b)
for i in x:
    print(i, end=' ')
