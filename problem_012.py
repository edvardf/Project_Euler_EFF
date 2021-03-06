"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

i = 2
factors = 0
while factors < 500:
    factors = 0
    tri_num = 0
    j = 1
    for num in range(i):
        tri_num += num
    while j * j <= tri_num:
        if tri_num % j == 0:
            factors += 1
            if tri_num // j != j:
                factors += 1
        j += 1
    i += 1

print("The triangle number", tri_num, "has", factors, "factors.")
