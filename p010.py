"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import *

num = 0
primes = [2]
i = 3

while i < 2e6:
    for p in primes:
        if i % p == 0:
            break
        elif p > floor(sqrt(i)):
            primes.append(i)
            break
    i += 2

for p in primes:
    num += p

print(num)
