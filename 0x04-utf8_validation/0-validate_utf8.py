#!/usr/bin/python3
""" Module for UTF8 validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Function to check if a data set represents a valid UTF-8 encoding
    Args:
        data: list to be validated
    Returns: True if it is, false if otherwise
    """
    byte_Count = 0
    for element in data:
        if byte_Count > 0:
            if element >> 6 != 0b10:
                return False
            byte_Count -= 1
        else:
            if element >> 7 == 0:
                byte_Count = 0
            elif element >> 5 == 0b110:
                byte_Count = 1
            elif element >> 4 == 0b1110:
                byte_Count = 2
            elif element >> 3 == 0b11110:
                byte_Count = 3
            else:
                return False

    return byte_Count == 0
