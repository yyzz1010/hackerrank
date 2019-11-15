n = int(input())
phone_dict = {}
for _ in range(n):
    name, phone = input().split(' ')
    phone_dict[name] = phone

while True:
    try:
        query = input()
        if query not in phone_dict:
            print('Not found')
        else:
            print(query + '=' + phone_dict[query])
    except EOFError:
        break
