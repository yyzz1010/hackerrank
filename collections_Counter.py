from collections import Counter

n = int(input())
num_list = list(map(int, input().split(' ')))
freq_dict = dict(Counter(num_list))
m = int(input())
price_list = []
for _ in range(m):
    (size, price) = tuple(map(int, input().split(' ')))
    if size in freq_dict:
        if freq_dict[size] == 0:
            continue
        freq_dict[size] -= 1
        price_list.append(price)
print(sum(price_list))
