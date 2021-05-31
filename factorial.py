# n! = n * (n - 1) * (n - 2) ... 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
