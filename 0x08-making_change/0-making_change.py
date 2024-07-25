#!/usr/bin/python3
"""Making Change challenge
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Calculate the number of coins needed to make the total amount given
    Args:
        coins: List of denominations
        total: the amount of money to change
    Returns: the number of coins
    """
    if total <= 0:
        return 0
    coins.sort()
    listLength = len(coins) - 1

    quo = coins[listLength]
    div = 0
    num = total
    if num % quo == 0:
        return num / quo
    Div_list = []
    while listLength >= 0:
        div += num // quo
        rem = num % quo
        if rem < quo:
            Div_list.append(num // quo)
            quo = coins[listLength - 1]
            num = rem
            listLength -= 1
    listLength = len(coins) - 1
    sum_of_coins = 0
    for x in Div_list:
        sum_of_coins += x * coins[listLength]
        listLength -= 1

    if sum_of_coins != total:
        return -1
    return div
