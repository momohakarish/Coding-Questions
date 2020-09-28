from typing import List

"""
The idea is to do a BFS and each time we reach a 1 we go and recursively and delete all neighbouring ones and that way we can treat a 1 as an island.
We increment a counter each time we encounter a 1 and simply return it at the end.
"""


def delete(self, grid: List[List[str]], i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return
    if grid[i][j] == '0':
        return
    grid[i][j] = '0'
    self.delete(grid, i + 1, j)
    self.delete(grid, i - 1, j)
    self.delete(grid, i, j + 1)
    self.delete(grid, i, j - 1)


def numIslands(self, grid: List[List[str]]) -> int:
    count = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if grid[i][j] == '1':
                count += 1
                self.delete(grid, i, j)
    return count
