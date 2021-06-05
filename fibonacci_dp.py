# time & space complexity - 0(n)
# bottom-up approach (tabulation)


def fib(n):
    fib_arr = [0] * (n + 1)
    fib_arr[0] = 0
    fib_arr[1] = 1

    for i in range(2, len(fib_arr)):
        fib_arr[i] = fib_arr[i - 1] + fib_arr[i - 2]

    return fib_arr[n]
