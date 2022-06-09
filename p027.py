# https://projecteuler.net/problem=27
# b must be prime and a must be odd
from p005 import primes

quad_list = []
for a in range(-999, 1000, 2):
    for b in primes(1000):
        if a > -b:  # quad-formula must be greater than 0 gives a > -b
            quad_list.append([a, b])
        if a > b:
            quad_list.append([a, -b])

primes_set = set(
    primes(111000)
)  # biggest prime to check -> 100**2 + 100 * 1000 + 1000 = 111000
longest_n = [0, 0]
for pair in quad_list:
    n = 0
    while True:
        quad_formula = n**2 + n * pair[0] + pair[1]
        if quad_formula in primes_set:
            n += 1
        else:
            if n > longest_n[1]:
                longest_n = [pair, n]
            break

print(longest_n)
print(longest_n[0][0] * longest_n[0][1])
