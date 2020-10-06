
"""
The idea is simple. Just Iterate over the tree and check if a node's value is even. if it is return the sum of it's grand kids
Time and Space complexity is O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def iterate(root: TreeNode) -> int:
    if root is None:
        return 0
    output = 0
    if root.val % 2 == 0:
        if root.right is not None:
            if root.right.right is not None:
                output += root.right.right.val
            if root.right.left is not None:
                output += root.right.left.val
        if root.left is not None:
            if root.left.right is not None:
                output += root.left.right.val
            if root.left.left is not None:
                output += root.left.left.val
    return output + iterate(root.left) + iterate(root.right)


def sumEvenGrandparent(root: TreeNode) -> int:
    return iterate(root)