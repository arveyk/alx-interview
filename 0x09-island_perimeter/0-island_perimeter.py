#!/usr/bin/python3
"""
island_perimeter Module
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
    if length == 0:
        return 0
    for x in range(width):
        for y in range(length):
            if (x > 0 and x < width - 1) and (y > 0 and y < length - 1):
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
            if x == 0:
                if y == 0:
                    if grid[x][y] == 1:
                        if grid[x + 1][y] == 0:
                            perimeter += 1
                        if grid[x][y + 1] == 0:
                            perimeter += 1
                if y == length - 1:
                    if grid[x][y] == 1:
                        if grid[x + 1][y] == 0:
                            perimeter += 1
                        if grid[x][y - 1] == 0:
                            perimeter += 1
                if y > 0 and y < length - 1:
                    if grid[x][y] == 1:
                        if grid[x][y + 1] == 0:
                            perimeter += 1
                        if grid[x][y - 1] == 0:
                            perimeter += 1
                        if grid[x + 1][y] == 0:
                            perimeter += 1
            if x == width - 1:
                if y == 0:
                    if grid[x][y] == 1:
                        if grid[x - 1][y] == 0:
                            perimeter += 1
                        if grid[x][y + 1] == 0:
                            perimeter += 1
                if y == length - 1:
                    if grid[x][y] == 1:
                        if grid[x - 1][y] == 0:
                            perimeter += 1
                        if grid[x][y - 1] == 0:
                            perimeter += 1
                if y > 0 and y < length - 1:
                    if grid[x][y] == 1:
                        if grid[x][y - 1] == 0:
                            perimeter += 1
                        if grid[x - 1][y] == 0:
                            perimeter += 1
                        if grid[x][y + 1] == 0:
                            perimeter += 1
                if x > 0 and x < width - 1:
                    if y == 0:
                        if grid[x - 1][y] == 0:
                            perimeter += 1
                        if grid[x][y + 1] == 0:
                            perimeter += 1
                        if grid[x + 1][y] == 0:
                            perimeter += 1
                    if y == length - 1:
                        if grid[x - 1][y] == 0:
                            perimeter += 1
                        if grid[x][y - 1] == 0:
                            perimeter += 1
                        if grid[x + 1][y] == 0:
                            perimeter += 1
                        
    return perimeter
