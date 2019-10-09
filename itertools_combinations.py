from itertools import combinations
import re

s, k = input().split()
for x in range(1, int(k)+1):
    for word in list(combinations(sorted(s),x)):
        print(''.join([x for x in re.findall('\w', str(word))]))
