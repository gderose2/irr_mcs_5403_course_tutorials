#!/usr/bin/env python3

is_prime = True

n = int(input("Enter a positive integer: "))

# 0 and 1 are not prime numbers
if (n == 0 or n == 1):
    is_prime = False

# loop to check if n is prime
for i in range( 2, int(n/2)+1 ):
    if (n % i == 0):
        is_prime = False
        break;

# check if flag is True
if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")


