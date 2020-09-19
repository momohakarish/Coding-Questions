from typing import List

"""
The idea is simple iterate over both lists in parallel and check if qureyTime is in the range [startTime, endTime] inclusive.
count the number of times the condition was satisfied
"""


"""
Solution 1
Time Complexity O(n) with n being the length of the lists
Space complexity O(1)
"""


def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    count = 0
    for start, end in zip(startTime, endTime):
        if start <= queryTime <= end:
            count += 1
    return count


"""
Solution 2 
We can make this a one liner using list comprehension although this is less space efficient as we make an array of dummy values
Time Complexity O(n) with n being the length of the lists
Space complexity O(n)
"""


def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    return len([0 for start, end in zip(startTime, endTime) if start <= queryTime <= end])
