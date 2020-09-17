# 03: largest prime factor
# The purpose of this program

# import everything!
import math

def largest_prime(num):
    # num is even
    while (num % 2 == 0):
        large_prime = 2
        num /= 1
    # num is odd
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while (num % i == 0):
            large_prime = i
            num = num / i
    # prime num > 2
    if num > 2:
        large_prime = num
    return int(large_prime)

#run function
print(largest_prime(600851475143))
