# memoization: 0(m^(n)) -> 0(mn)
# top-down approach


def fib(n, lookup={0: 0, 1: 1}):
    if n in lookup:
        return lookup[n]
    else:
        lookup[n] = fib(n - 1) + fib(n - 2)

    return lookup[n]
