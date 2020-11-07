"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples(a, b, stop):
    sum_ = 0
    for x in range(1, stop):
        if x % a == 0 or x % b == 0:
            sum_ += x
    return sum_


print(sum_multiples(3, 5, 1000))
