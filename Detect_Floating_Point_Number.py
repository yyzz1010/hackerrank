import re

x = int(input())
for _ in range(x):
    print(bool(re.match('(\-*|\+*)\d*\.\d+$', str(input()))))
