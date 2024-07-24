#!/usr/bin/python3
"""Making Change challenge
"""


def makeChange(coins, total):
    """Calculate the number of coins needed to make the total amount given
    Args:
        coins: List of denominations
        total: the amount of money to change
    Returns: the number of coins
    """
    # sum up each coin x number, if < total return -1
    if total <= 0:
        return 0
    coins.sort()
    return coins
