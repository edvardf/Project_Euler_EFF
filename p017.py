"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters, 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""


def int_to_words(n):
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    i = 0
    word = list()
    while i < len(str(n)):
        if n == 1000:
            word.append("one thousand")
            break
        elif i == 2:
            if int(str(n)[-2:len(str(n))]) != 0:
                word.append("and")
            word.append("hundred")
            word.append(digits[int(str(n)[-3])])
        elif i == 0:
            num = int(str(n)[-2:len(str(n))])
            if num < 10:
                if n % 100 != 0:
                    word.append(digits[num])
            elif 9 < num < 20:
                word.append(teens[num-10])
            else:
                if num % 10 == 0:
                    word.append(tens[(num//10)-2])
                else:
                    word.append(digits[int(str(num)[1])])
                    word.append(tens[num//10-2])
        i += 1
    word = reversed(word)
    word = " ".join(w for w in word)
    return word


sum_of_letters = 0
for i in range(1000):
    i += 1
    sum_of_letters += len(int_to_words(i).replace(" ", ""))

print(sum_of_letters)
