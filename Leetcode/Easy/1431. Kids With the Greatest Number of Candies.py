from typing import List

"""
The idea is simple, we just need to iterate over every value in the array and check if after adding extraCandies to it it is bigger or equal to the maximum value in the array.
We use a list comprehension and return the array
Time complexity is O(n) with n being the length of the array
Space complexity is O(n) with n being the length of the array
"""


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]
