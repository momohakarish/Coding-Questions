from typing import List

"""
The idea is to preform a BFS and each time we encounter a 1 we recursively search for neighbouring 1's and increment a counter while deleting each 1 we found to avoid circles.
We simply take the max number we found using that method
"""


def countArea(grid: List[List[int]], i: int, j: int) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
        return 0
    grid[i][j] = 0
    return 1 + countArea(grid, i + 1, j) + countArea(grid, i - 1, j) + countArea(grid, i, j + 1) + countArea(grid, i, j - 1)


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    max_area = 0

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                max_area = max(max_area, countArea(grid, i, j))
    return max_area
