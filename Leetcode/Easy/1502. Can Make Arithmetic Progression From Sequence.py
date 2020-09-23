from typing import List

"""
The idea is simple, just sort the array and find d.
After that just iterate over the array and check if a[i+1] - a[i] = d for every i. If not return false otherwise return true
Time Complexity is O(n * log(n)) with n being the size of the array
Space Complexity is O(1)
"""


def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    if len(arr) <= 1:
        return True

    d = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != d:
            return False
    return True
