"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

a = 600851475143
i = 1
while i > 0:
    for x in range(2, a):
        if a % x == 0:
            a = int(a / x)
            print(a)
            break
    if a == 1:
        break
print("done")
