def leibnic(n):
    if n == 1:
        return 4
    else:
        if n % 2 == 0:
            return leibnic(n - 1) - 4 / (2 * n - 1)
        else:
            return leibnic(n - 1) + 4 / (2 * n - 1)

print(leibnic(10))
