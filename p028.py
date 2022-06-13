"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def clockwise_spiral(side_len: int):
    nums = [n for n in range(1, side_len**2 + 1)]
    arms = side_len * 4 - 3
    spiral = [[] for arm in range(arms)]
    arm_len = 1
    for arm in range(arms):
        if (arm - 1) % 3 == 0:
            arm_len += 1
        for i in range(arm_len):
            spiral[arm].append(nums[i])
    return spiral


for row in clockwise_spiral(5):
    print(row)
