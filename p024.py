"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from math import factorial


def n_perm(n, e_l):
    perms = factorial(len(e_l))
    d = []
    p = []
    if n == 0:
        return e_l
    if n >= perms:
        return "Error, n out of range"
    for i in range(len(e_l)):
        perms /= len(e_l)-i
        if n >= perms:
            for j in range(i, len(e_l)):
                d.append(e_l[j])
            for j in range(i):
                p.append(e_l[j])
            break
    for i in range(len(d)):
        p.append(d[int(n//perms)])
        d.pop(int(n//perms))
        n -= perms*(n//perms)
        if len(d) == 0:
            break
        perms /= len(d)
    return p


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans_l = n_perm(10**6-1, digits)
ans = 0
for i in range(len(ans_l)):
    c = 10 ** (len(ans_l) - i - 1)
    ans += c * ans_l[i]
print(ans)
