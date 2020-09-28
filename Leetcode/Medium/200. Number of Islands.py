from typing import List

"""
The idea is to do a BFS and each time we reach a 1 we go and recursively delete all neighbouring ones and that way we can treat a 1 as an island.
We increment a counter each time we encounter a 1 and simply return it at the end.
"""


def delete(grid: List[List[str]], i: int, j: int):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return
    if grid[i][j] == '0':
        return
    grid[i][j] = '0'
    delete(grid, i + 1, j)
    delete(grid, i - 1, j)
    delete(grid, i, j + 1)
    delete(grid, i, j - 1)


def numIslands(grid: List[List[str]]) -> int:
    count = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if grid[i][j] == '1':
                count += 1
                delete(grid, i, j)
    return count
