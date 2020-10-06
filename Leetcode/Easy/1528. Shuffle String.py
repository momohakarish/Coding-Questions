from typing import List

"""
The idea is to just iterate over the string and indices array simultaneously and build an array as instructed and then return the array as a string
"""


def restoreString(s: str, indices: List[int]) -> str:
    output = ['0' for i in range(len(indices))]
    for ch, index in zip(s, indices):
        output[index] = ch
    return ''.join(output)