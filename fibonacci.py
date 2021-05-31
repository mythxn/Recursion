# fib(n) = fib(n - 1) + fib(n - 2)
# fib(5) = 0, 1, 1, 2 , 3, [5]


def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
