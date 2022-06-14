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
    arm_count = side_len * 2 - 1
    arms = [[] for arm in range(arm_count)]
    arm_len = 0
    for arm in range(arm_count):
        if arm % 2 == 0:
            c = 1 + arm_len * (arm_len + 1)
            arm_len += 1
        else:
            c = 1 + arm_len**2
        for i in range(arm_len):
            arms[arm].append(i + c)
    spiral = [[0 for n in range(side_len)] for row in range(side_len)]
    row_index = side_len // 2
    if side_len % 2 == 0:
        row_index -= 1
    column_index = row_index
    for i in range(arm_count):
        direction = i % 4
        for n in arms[i]:
            spiral[row_index][column_index] = n
            if direction == 0:  # right
                column_index += 1
            if direction == 1:  # down
                row_index += 1
            if direction == 2:  # left
                column_index -= 1
            if direction == 3:  # up
                row_index -= 1
    return spiral


def square_matrix_diag_sum(sqaure_matrix):
    ans = -1
    for i in range(len(sqaure_matrix)):
        ans += sqaure_matrix[i][i] + sqaure_matrix[-(i + 1)][i]
    if len(sqaure_matrix) % 2 == 0:
        ans += 1
    return ans


print(square_matrix_diag_sum(clockwise_spiral(1001)))
