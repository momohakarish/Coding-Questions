from typing import List

"""
The idea is simple just find the max, min, and sum of the array and then calculate the result using this formula:
result = (sum - max - min) / (len(salary) - 2)

Time complexity is O(n) with n being the length of the array
Space complexity is O(1) 
"""


def average(salary: List[int]) -> float:
    return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)

