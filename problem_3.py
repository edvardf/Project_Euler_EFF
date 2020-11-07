"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

num = 600851475143
fac = 2

while num > 1:
    if (num % fac == 0):
        num //= fac
    else:
        fac += 1

print(fac)
