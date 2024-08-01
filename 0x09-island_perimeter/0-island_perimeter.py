#!/usr/bin/python3
"""
island_perimeter Function
"""


def island_perimeter(grid):
    """Evaluates the perimeter of an island described in grid
    Args:
        grid: list descibing an island
    Returns:
        perimeter of described island
    """
    if len(grid) == 0:
        return 0
    ground = []
    perimeter = 0
    width = len(grid)
    length = len(grid[0])
    for x in range(width):
        for y in range(length):
            if grid[0][y] != 0 or grid[width - 1][y] != 0:
                return 0
            if grid[x][0] != 0 or grid[x][length - 1] != 0:
                print(grid)
                return 0
            if grid[x][y] == 1:
                ground.append((x, y))
                if grid[x - 1][y] == 0:
                    perimeter += 1
                if grid[x][y - 1] == 0:
                    perimeter += 1
                if grid[x][y + 1] == 0:
                    perimeter += 1
                if grid[x + 1][y] == 0:
                    perimeter += 1
    return perimeter
