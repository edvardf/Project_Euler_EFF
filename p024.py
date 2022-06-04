"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from calendar import c
from math import factorial


def n_perm(n, e_l):
    perms = factorial(len(e_l))
    d = e_l.copy()
    p = []
    for i in range(len(e_l)):
        perms /= len(e_l)-i
        if n >= perms:
            break
    for i in range(len(d)):
        p.append(d[int(n//perms)])
        d.pop(int(n//perms))
        n -= perms*(n//perms)
        if len(d) == 0:
            break
        perms /= len(d)
    return p


ans = n_perm(1e6-1, [0,1,2,3,4,5,6,7,8,9])
x=0
c = len(ans)-1
for _ in n_perm(1e6-1, [0,1,2,3,4,5,6,7,8,9]):
    x += 10**c*_
    c -= 1
print(x, ans)
