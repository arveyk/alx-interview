#!/usr/bin/python3
""" Module for Minimum operations function
"""
from math import floor


def isPrime(n):
    """Function to determine if a number is prime
    Args:
        n: number to be evaluated
    Returns: True is so, False otherwise
    """
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)

    f = 3
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 1
        return True


def minOperations(n):
    """Evaluates the minimum number of times the Character H has to be copied
    to have the give number of H characters
    Args:
        n: the number to evaluate
    Return: the number of operations to carry out
    """
    if n < 1:
        return 0
    i = 2
    prime_fact = []
    sqr_root = floor(n * 0.5)
    while i <= (sqr_root):
        if n / i == 1:
            prime_fact.append(i)
            break
        if isPrime(i) is True:
            if n % i == 0:
                while n % i == 0:
                    prime_fact.append(i)
                    n /= i
        i += 1
    total = 0
    length = len(prime_fact)
    for i in range(length):
        total += prime_fact[i]
    return total
