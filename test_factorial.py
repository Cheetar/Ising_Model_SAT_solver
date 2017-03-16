from math import factorial


def bin_coef(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

s = sum([bin_coef(8, k) for k in range(0, 6)])

print s
