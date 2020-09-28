from typing import List

"""
Idea is simple just create a set of all seen numbers. Once we find a number inside the set we return it as it's the repeating one.
Time and Space complexity are O(n)
"""


def repeatedNTimes(A: List[int]) -> int:
    repeated = set()

    for num in A:
        if num in repeated:
            return num
        repeated.add(num)
    return -1
