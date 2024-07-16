#!/usr/bin/python3
""" Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Function to rotate an n by n matric 90degrees clockwise
    Args:
        matrix: the matix to be rotated
    Returns: no return value
    """
    size = len(matrix)
    for x in range(0, int(size / 2)):
        for y in range(x, size - x - 1):
            temp = matrix[x][y]
            temp2 = matrix[x][size - 1]

            matrix[x][y] = matrix[size - y - 1][x]
            matrix[size - y - 1][x] = matrix[size - x - 1][size - y - 1]

            matrix[size - x - 1][size - y - 1] = matrix[y][size - x - 1]
            matrix[y][size - x - 1] = temp
