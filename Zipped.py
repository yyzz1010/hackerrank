from statistics import mean

n, x = map(int, input().split())
score_list = [list(map(float, input().split())) for i in range(x)]
zip_list = list(zip(*score_list))
zip_list = [list(item) for item in zip_list]
for item in zip_list:
    print(round(mean(item), 1))
