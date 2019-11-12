arr = list(map(int, input().rstrip().split()))
sum_list = []
for i in arr:
    l = arr.copy()
    l.remove(i)
    sum_list.append(sum(l))
print(min(sum_list), max(sum_list))
