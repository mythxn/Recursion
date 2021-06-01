def climbing_stairs(n, memo={}):
    # at the last step
    if n == 0:
        return 1
    # crossed last step
    if n < 0:
        return 0

    # memoization
    if n in memo:
        return memo[n]
    else:
        # recursive call
        memo[n] = climbing_stairs(n - 1) + climbing_stairs(n - 2)
        return memo[n]
