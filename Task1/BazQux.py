for i in range(1, 101):
    print(i, end=' ')

print()

for i in range(1, 101):
    if i % 15 == 0:
        print('BazQux', end=' ')
    elif i % 3 == 0:
        print('Baz', end=' ')
    elif i % 5 == 0:
        print('Qux', end=' ')
    else:
        print(i, end=' ')
