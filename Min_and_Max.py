n, m = list(map(int, input().split(' ')))

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split(' '))))
#arr = [list(map(int, input().split(' '))) for _ in range(n)]
    
min_list = []
for x in arr:
    min_list.append(min(x))
print(max(min_list))
#print(max([min(x) for x in arr]))
