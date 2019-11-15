n = int(input())
arr = list(map(int, input().rstrip().split()))
for x in arr[::-1]:
    print(x, end=' ')
