import sys


class Stack:
    def __init__(self, iterable):
        self.data = []
        for elem in iterable:
            self.data.append(elem)

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        del self.data[-1]

    def top(self):
        return self.data[-1]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return ' '.join([str(i) for i in self.data])


exec(sys.stdin.read())
