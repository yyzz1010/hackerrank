def swap_case(s):
    x = ''
    word_list = []
    for word in s:
        if word == word.upper():
            word_list.append(word.lower())
        else: 
            word_list.append(word.upper())
    return x.join(word_list)
