import sys


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imaginary - other.imaginary)

    def __mul__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return ComplexNumber(a * c - b * d, a * d + b * c)

    def __truediv__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        if other.imaginary == 0.0:
            return ComplexNumber(a / c, b / c)
        else:
            norm = c ** 2 + d ** 2
            return ComplexNumber((a * c + b * d) / norm,
                                 (b * c - a * d) / norm)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self):
        if self.real == 0.00 and self.imaginary == 0.00:
            return '0.00'
        if self.real == 0.0:
            return "%.2f" % self.imaginary + 'i'
        if self.imaginary == 0.0:
            return "%.2f" % self.real
        if self.imaginary > 0.0:
            return "%.2f" % (self.real) + ' + ' \
                   + "%.2f" % self.imaginary + 'i'
        return "%.2f" % (self.real) + ' - ' \
               + "%.2f" % abs(self.imaginary) + 'i'


print(ComplexNumber(4.33, 4.37) * ComplexNumber(2, 1))

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print(eval(line.strip()))
