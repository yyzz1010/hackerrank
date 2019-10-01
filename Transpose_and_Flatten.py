import numpy as np

n, m = list(map(int, input().split()))
arr_list = []
for x in range(n):
    arr_list.append(list(map(int, input().split())))
print(np.array(arr_list).transpose())
print(np.array(arr_list).flatten())
