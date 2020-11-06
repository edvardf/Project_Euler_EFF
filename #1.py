"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples(m):
    a = 0
    for x in range(1, 1000):
        if x % m == 0:
            a += x
    return a


print(sum_multiples(3), "+", sum_multiples(5), "-", sum_multiples(15), "=")
print("Ans = ", sum_multiples(3) + sum_multiples(5) - sum_multiples(15))
