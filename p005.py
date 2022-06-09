from math import floor, sqrt


def primes(max: int):
    primes = []
    for n in range(2, max + 1):
        isPrime = True
        for p in primes:
            if p > floor(sqrt(n)):
                break
            if n % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(n)
    return primes


def min_divisible(max: int):
    prim = primes(max)
    ans = 1
    for p in prim:
        power = 1
        while p**power < max:
            power += 1
        power -= 1
        ans *= p**power
    return ans


i = 20
print(len(str(min_divisible(i))) / i)
