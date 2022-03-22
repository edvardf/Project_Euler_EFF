"""
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


names = []

with open("p022_names.txt", "r") as fp:
    contents = fp.read()
    for name in contents.split(','):
        names.append(name.strip('"'))
    names.sort()

sum_ = 0

for i in range(len(names)):
    name = names[i]
    x = 0
    for j in range(len(name)):
        x += ord(name[j])-64
    sum_ += x * (i+1)

print(sum_)
