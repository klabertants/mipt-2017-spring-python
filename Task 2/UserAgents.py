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


def l():
    return lambda x: x[1]


systems = [['Macintosh', 0, 'OS X'], ['Ubuntu', 0, 'Ubuntu'],
           ['Windows', 0, 'Windows'], ['Unknown', 0, 'Unknown']]

f = open('input.txt')

for line in f.readlines():
    split_line = intelligent_split(line)
    current_agent = split_line[8]
    recognized = False
    for index, obj in enumerate(systems):
        if obj[0] == 'Unknown':
            continue
        if obj[0] in current_agent:
            systems[index][1] += 1
            recognized = True
    if not recognized:
        systems[3][1] += 1

sorted_systems = sorted(systems, key=lambda x: x[1])

for ind, count, os_name in sorted_systems:
    print(os_name + ": " + str(count))
