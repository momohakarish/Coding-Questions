from typing import List


"""
The idea is iterating over all odd numbers until the length of the array and adding the sum of all sub arrays with odd length using slices.
This solution isn't efficient however it's simple

Time Complexity O(n^3) with n being the length of the array
Space Complexity O(1)
"""


def sumOddLengthSubarrays(arr: List[int]) -> int:
    output = 0
    for i in range(1, len(arr) + 1, 2):  # Iterating over the odd numbers
        for j in range(len(arr)):   # Iterating over the sub-arrays we need to sum
            if j + i > len(arr):    # Breaking if the sub array is out of bounds
                break
            output += sum(arr[j:j + i])
    return output
