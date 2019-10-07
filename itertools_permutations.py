from itertools import permutations
a, b = input().split()
a = ''.join(sorted(a))
b = int(b)
for x in list(permutations(a, b)): 
    print(''.join(x))
