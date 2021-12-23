def is_primes(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(n):
    ans = []
    for i in range(2, n + 1):
        if is_primes(i):
            ans.append(i)
    return ans


print(get_primes(1000))
assert [2, 3, 5, 7, 11] == sorted(get_primes(11))
