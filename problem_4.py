"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

p = 0

for i in range(999, 99, -1):
    if i * i < p:
        break
    for j in range(i, 99, -1):
        buf = num = i * j
        r_num = 0

        while buf != 0:
            r_num *= 10
            r_num += buf % 10
            buf //= 10

        if r_num == num and num > p:
            p = num
            break

print(p)