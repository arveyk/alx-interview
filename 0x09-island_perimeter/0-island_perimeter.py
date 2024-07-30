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

    ground = []
    perimeter = 0
    for x in range(1, len(grid)):
        for y in range(1, len(grid)):
            if grid[x][y] == 1:
                if (x, y) in ground:
                    continue
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
