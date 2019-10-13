text = input()
for s, x in zip(text, range(len(text))):
    if not s.isalnum():
        continue
    try: 
        if text[x] == text[x+1]:
            ans = text[x]
            break
    except IndexError:
        break

try:
    print(ans)
except NameError: 
    print(-1)
