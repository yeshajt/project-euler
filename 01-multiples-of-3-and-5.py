# 01: Multiples of 3 + 5
# The purpose of this program is to find the sum of all the multiples of 3 + 5
# under 1000.

def sumcalc(num):
    total = 0
    for i in range(num):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    print(total)

sumcalc(1000)
