input1 = list(map(int, input()))
count = 1
list1 = []

for num in range(len(input1)):
    try:
        if input1[num] == input1[num+1]:
            count += 1
        else:
            list1.append((count, input1[num]))
            count = 1
    except IndexError:
        list1.append((count, input1[num]))

for a in list1:
    print(a, end=' ')
