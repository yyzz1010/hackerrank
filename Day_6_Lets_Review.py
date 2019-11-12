n = int(input())
for _ in range(n):
    text = input()
    print(text[::2] + ' ' + text[1::2])
