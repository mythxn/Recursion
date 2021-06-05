# using while loop:
def nbDivisors(n):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


# recursive function:
def nbDivisors(n, count=0, i=1):
    if i > n:
        return count
    else:
        if n % i == 0:
            count += 1
        i += 1
        return nbDivisors(n, count, i)
