from typing import List

"""
The idea is simple, we just need to iterate over every value in the array and check if it's bigger or equal to the maximum value in the array.
We add that result (True or False) to our output array and return it at the end of the loop.
Time complexity is O(n) with n being the length of the array
Space complexity is O(n) with n being the length of the array
"""


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    output = []
    max_candies = max(candies)

    for candy in candies:
        output.append(candy + extraCandies >= max_candies)

    return output
