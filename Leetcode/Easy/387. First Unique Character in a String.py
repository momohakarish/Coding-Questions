from collections import Counter

"""
The idea is simple. Count how much times each character appears in the string and then iterate through the string and check which character appears only ones.
Time and Space complexity are both O(n)
"""


def firstUniqChar(s: str) -> int:
    temp = Counter(s)

    for index, ch in enumerate(s):
        if temp.get(ch) == 1:
            return index
    return -1

