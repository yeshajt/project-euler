# 05: smallest multiple
# The purpose of this program is to find the smalles positive number that is
# evenly divisible by all of the numbers from 1 to 20

import fractions #to access gcd

def smallest_multiple():
   number = 1
   for i in range(1, 11):
        lcm = i // fractions.gcd(i, number)
        number = number * lcm
   return(number) 

print(smallest_multiple())

    


    
