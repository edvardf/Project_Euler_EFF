"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known
that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from math import floor, sqrt


def ab_nums(stop):
    nums = []
    for n in range(1, stop+1):
        sum_d = -n
        for d in range(1, floor(sqrt(n))+1):
            if d*d == n:
                sum_d -= d
            if n % d == 0:
                sum_d += d + n/d
        if n < sum_d:
            nums.append(n)
    return nums


ab = ab_nums(28123)
s = 0