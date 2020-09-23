"""
Simple BST traversal just use the invariant of the binary search tree for efficient search
Time Complexity is O(n) with n being the number of nodes in the tree
Space Complexity is O(1)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(root: TreeNode, val: int) -> TreeNode:
    if root is None:
        return None
    if root.val == val:
        return root
    if val > root.val:
        return search(root.right, val)
    else:
        return search(root.left, val)


def searchBST(root: TreeNode, val: int) -> TreeNode:
    return search(root, val)