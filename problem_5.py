"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from __future__ import annotations

from sys import argv


def primes_less_than(n: int) -> list[int]:
    primes = list()
    for i in range(2, n + 1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    return primes


lim = int(argv[1])
primes = primes_less_than(lim)

powers = [0 for _ in primes]

for i, prime in enumerate(primes):
    e = 1
    p = prime
    while p * prime < lim:
        p *= prime
        e += 1
    powers[i] = e

num = 1

for b, e in zip(primes, powers):
    num *= b ** e

print(num)
