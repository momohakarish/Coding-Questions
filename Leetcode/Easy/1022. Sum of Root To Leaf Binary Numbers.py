"""
The idea for both solutions is the same with the difference being slightly different implementation.
Efficiency is also the same for both solutions asymptotic wise.

The idea for solving the question is to iterate recursively over the tree and build a number for each root to leaf path using the values in the nodes.
When we reach a leaf we simply return the value of number we have constructed so far
We sum the results using recursion as well and we arrive at the solution

For both solutions:
Time Complexity is O(n) with n being the number of nodes in the tree
Space complexity is O(h) where h is the height of the tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Solution 1 
We build a string representing a binary number with the idea written above and return it when we reach a leaf
"""


def traverse(root: TreeNode, number: str) -> int:
    if root is None:
        return 0
    number += str(root.val)

    # If the node is a leaf
    if root.left is None and root.right is None:
        return int(number, 2)
    return traverse(root.left, number) + traverse(root.right, number)


def sumRootToLeaf(root: TreeNode) -> int:
    return traverse(root, '')


"""
Solution 2
We build a number calculating it's value from the bits as we traverse using bit shifts and addition.
"""


def traverse(root: TreeNode, number: int) -> int:
    if root is None:
        return 0

    number = number << 1
    number += root.val
    if root.left is None and root.right is None:
        return number
    return traverse(root.left, number) + traverse(root.right, number)


def sumRootToLeaf(root: TreeNode) -> int:
    return traverse(root, 0)

"""
Runtime: 32 ms, faster than 59.49% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
Memory Usage: 13.8 MB, less than 77.07% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary."""