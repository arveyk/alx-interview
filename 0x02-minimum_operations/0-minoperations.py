#!/usr/bin/python3
""" Module for Minimum operations function
"""

def isPrime(n):
    """Function to determine if a number is prime
    Args:
        n: number to be evaluated
    Returns: True is so, False otherwise
    """
    if n == 2 or n == 3:
        print('{}prime')
        return True
    if n < 2 or n % 2 == 0:
        print('{} not prime')
        return False
    if n < 9:
        print('{} prime')
        return True
    if n % 3 == 0:
        print('{} Not prime')
        return False
    r = int (n ** 0.5)

    f = 5
    while f <= r:
        print('\t', f)
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
        return True

def main():
    if isPrime(504):
        print("is Prime")

main()
