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


firstType = secondType = thirdType = others = 0

f = open('input.txt')

for line in f.readlines():
    split_line = intelligent_split(line)
    others += 1
    responce = int(split_line[5])
    if responce == 200:
        firstType += 1
    elif 300 <= responce <= 309:
        secondType += 1
    else:
        thirdType += 1

print(firstType, secondType, thirdType, others, sep='\n')
