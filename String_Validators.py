if __name__ == '__main__':
    s = input()
    boolean_list = []
    for word in s:
        if word.isalnum():
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    print(any(boolean_list))

    boolean_list = []
    for word in s:
        if word.isalpha():
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    print(any(boolean_list))

    boolean_list = []
    for word in s:
        if word.isdigit():
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    print(any(boolean_list))

    boolean_list = []
    for word in s:
        if word.islower():
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    print(any(boolean_list))

    boolean_list = []
    for word in s:
        if word.isupper():
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    print(any(boolean_list))
