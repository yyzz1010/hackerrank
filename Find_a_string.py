def count_substring(string, sub_string):
    start = 0
    num = len(sub_string)
    string = list(string)
    word_list = []
    counter = 0
    for _ in string:
        word = ''.join(string[start:num])
        word_list.append(word)
        start += 1
        num += 1
    for x in word_list:
        if x == sub_string:
            counter += 1
    return counter
