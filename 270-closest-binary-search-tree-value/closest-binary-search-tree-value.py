# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode | None, target: float) -> int:
        close = root.val
        while root:
            if (abs(root.val-target) < abs(close-target) or abs(root.val-target) == abs(close-target) and root.val < close):
                close = root.val
            if root.val>target:
                root = root.left
            else:
                root = root.right
        return close




        