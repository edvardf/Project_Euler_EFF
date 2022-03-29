"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = []
for i in range(10**6):
    c = len(digits)
    p = 0
    for d in digits:
        c -= 1
        p += d*10**c
    perms.append(p)
    print(p)
#print(perms[-1])
