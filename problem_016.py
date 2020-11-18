"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

num = str(2 ** 1000)
cross_sum = 0

for i in range(len(num)):
    cross_sum += int(num[i])

print(cross_sum)
