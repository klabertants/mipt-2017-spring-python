def intelligent_split(sample):
    flag = True
    start_index = 0
    result = []
    for index, char in enumerate(sample):
        if char == ' ' and flag:
            result.append(sample[start_index:index])
            start_index = index + 1
        if char in '"[]':
            flag = not flag
    result.append(sample[start_index:])
    return result


counter = 0

while 1:
    try:
        s_input = intelligent_split(input())
        if '"Go-http-client/1.1"' in s_input:
            counter += 1
    except EOFError:
        break
print(counter)
