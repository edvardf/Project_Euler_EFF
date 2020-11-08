"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from sys import argv

num = int(argv[1])
sum_sq = sum(i * i for i in range(1, num + 1))
sq_sum = sum(i for i in range(1, num + 1)) ** 2

print(sq_sum - sum_sq)
