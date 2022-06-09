"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
from math import floor


def digits_unit_fraction(max: int):
    frac_list = []
    for d in range(2, max):
        fraction = 1 / d
        power = 1
        prev_num = []
        digits = []
        while True:
            digit = floor(fraction * 10**power)
            power2 = len(prev_num)
            for i in range(len(prev_num)):
                digit -= prev_num[i] * 10**power2
                power2 -= 1
            digits.append(digit)
            prev_num.append(digit)
            power += 1
            if power > 16:
                break
        frac_list.append(digits)
    return frac_list


def reccuring_cycle_len(digits: list):
    l = len(digits)
    for i in range(l):
        for j in range(l):
            if i + j > l:
                break
            cycle = digits[i : i + j]
            k = len(cycle)
            if i + j + k > l:
                break
            if cycle == digits[i + k : i + j + k]:
                return k


for i in digits_unit_fraction(10):
    print(reccuring_cycle_len(i))
