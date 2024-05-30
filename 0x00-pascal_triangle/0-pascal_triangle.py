#!/usr/bin/python3
""" script for a pascal triangle function
"""


def pascal_triangle(n):
    """ Function for creating and printing Pascal's triangle
        Args:
            n number of rows
        Returns: list with elements of the triangle
    """
    pascal = []
    prev_row = [1, 1]
    current_row = [1]
    if (n <= 0):
        return pascal
    pascal.append(1)
    if (n == 1):
        return pascal
    if (n == 2):
        pascal.append(1)
        return pascal
    for index in range(1, n):
        for row in range(1, index):
            c = prev_row[row - 1] + prev_row[row]
            current_row.append(c)
        current.append(1)
        pascal.append(current_row)
        prev_row = current_row
        current_row = [1]

    return pascal
