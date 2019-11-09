n = int(input())
space = n-1
while True:
    print(' '*(space) + '#'*(n - space))
    space -= 1
    if space < 0:
        break
