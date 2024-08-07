#!/usr/bin/python3
""" IsWinner file
"""


def isWinner(x, nums):
    """ Determine the winner in this game
    Args:
        x: number of rounds to play
        nums: array of numbers to choose
    Returns:
        Winner; Ben or Maria or None"""
    Maria = 0
    Ben = 0
    if x == 0 or type(nums) != list:
        return None
    if len(nums) == 0:
        return None

    rounds = 0
    primeGame = []
    while rounds < x:
        primeGame = ErastosPrime(nums[rounds])
        if len(primeGame) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
        rounds += 1
    if Maria > Ben:
        return 'Maria'
    if Maria < Ben:
        return 'Ben'
    return None


def ErastosPrime(num):
    """ Function to generate primes from 2 to given number
    Args:
        num: the number given
    Returns:
        List of primes
    """
    list_prime = []
    for elem in range(num + 1):
        primes = [True for i in range(num + 1)]
        p = 2
        while (p * p <= num):
            if (primes[p] is True):
                for y in range(p * p, num + 1, p):
                    primes[y] = False
            p += 1
    for part in range(2, num + 1):
        if primes[part]:
            list_prime.append(part)
    return list_prime
