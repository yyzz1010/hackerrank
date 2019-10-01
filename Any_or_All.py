N = int(input())
num_list = list(map(int, input().split()))
if N == 1:
    print(False)
else:
    print(all([0<x<100 for x in num_list]))
