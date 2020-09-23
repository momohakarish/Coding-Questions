from typing import List


"""
The idea is to store all indices which don't satisfy our condition in two arrays one for odd and one for even and then swapping the values in those indices
Time Complexity is O(n) with n being the length of the array
Space complexity is O(n)
"""


def sortArrayByParityII(A: List[int]) -> List[int]:
    odd = []
    even = []

    for i, num in enumerate(A):
        if i % 2 == 0 and num % 2 != 0:
            even.append(i)
        elif i % 2 != 0 and num % 2 == 0:
            odd.append(i)

    for i, j in zip(odd, even):
        A[i], A[j] = A[j], A[i]

    return A
