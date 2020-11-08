"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes = [2]
i = primes[-1] + 1

while len(primes) < 10001:
    is_p = True
    for p in primes:
        if i % p == 0: 
            is_p = False
            break
    if is_p:
        primes.append(i)
    i += 2

print(primes[-1])
