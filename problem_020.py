"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def cross_sum(n):
    sum_ = 0
    for i in range(len(str(n))):
        sum_ += int(str(n)[i])
    return sum_


print(cross_sum(factorial(100)))
