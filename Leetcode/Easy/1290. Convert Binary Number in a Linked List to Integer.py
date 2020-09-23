"""
The idea is simple just iterate through the list creating a string representing a binary number and then convert it into an int and return
Time Complexity is O(n) with n being the length of the list
Space complexity is O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head: ListNode) -> int:
    output = ''
    iterator = head

    while iterator is not None:
        output += str(iterator.val)
        iterator = iterator.next

    return int(output, 2)
