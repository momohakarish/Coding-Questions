"""
The idea is to use a DFS.
First we need to find out the height of the tree so we if a leaf is at the deepest level.
After finding out the height we just traverse the tree and check if we found a leaf and if yes if it is at the deepest level.
We simply return the sum of those leaves.

Time and Space complexity are O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root: TreeNode, depth: int) -> int:
    if root is None:
        return depth

    return max(height(root.left, depth + 1), height(root.right, depth + 1))


def traversal(root: TreeNode, depth: int, height: int) -> int:
    if root is None:
        return 0

    if root.left is None and root.right is None:
        if depth + 1 == height:
            return root.val
        else:
            return 0
    return traversal(root.left, depth + 1, height) + traversal(root.right, depth + 1, height)


def deepestLeavesSum(root: TreeNode) -> int:
    return traversal(root, 0, height(root, 0))
