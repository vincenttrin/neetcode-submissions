# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        
        def check(node, d):
            if node:
                d += 1
                return max((check(node.left, d), check(node.right, d)))
            else:
                return d


        if root:
            return check(root, 0)
        else:
            return 0
