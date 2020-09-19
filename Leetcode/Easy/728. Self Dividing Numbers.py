from typing import List


"""
Checks if the number is self dividing according to the definition given by the question
Time complexity is O(l) with l being the number of digits in the number
Space complexity is O(1)
"""


def self_dividing(num: int) -> bool:
    for digit in str(num):
        if num % int(digit) != 0:
            return False
    return True


"""
The idea is simple and it's just iterating over all the numbers in the range given and checking if they are self dividing
Using the schema of [L ,R] to represent our range
Time complexity is O(n * l) with n being (R - L)
Space complexity is O(n)
"""


def selfDividingNumbers(left: int, right: int) -> List[int]:
    output = []
    for i in range(left, right + 1):
        if '0' in str(i):
            continue
        if self_dividing(i):
            output.append(i)
    return output

