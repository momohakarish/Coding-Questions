from typing import List

"""
The idea is to just build a prefix sum array using the formula:
prefix[i] = prefix[i - 1] + nums[i]
while iterating over the nums array for i > .
Time and Space complexity is O(n)
"""


def runningSum(nums: List[int]) -> List[int]:
    output = [nums[0]]
    for i in range(1, len(nums)):
        output.append(output[i - 1] + nums[i])
    return output