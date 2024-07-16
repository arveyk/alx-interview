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
    print(size)
    for x in range(0, int(size / 2)):
        for y in range(x, size - x - 1):
            """
            temp = matrix[x][y]
            temp2 = matrix[size - 1 - x][size - 1 - x]
            temp3 = matrix[size - 1]

            matrix[x][y] = matrix[y][size - 1 - x]
            matrix[y][size - 1 - x] = matrix[size - 1 - x][size - 1 - y]

            matrix[size - 1 - x][size - 1 - y] = matrix[size - 1 - y][x] 
            matrix[size - 1 - y][x] = temp
            """
            temp = matrix[x][y]
            temp2 = matrix[x][size - 1]

            matrix[x][y]  = matrix[size - y - 1][x]
            matrix[size - y - 1][x] = matrix[size - x - 1][size - y - 1]

            matrix[size - x - 1][size - y - 1] = matrix[y][size - x - 1]
            matrix[y][size - x - 1] = temp

