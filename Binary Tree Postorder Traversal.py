#Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        if root.left:
            res.extend(self.postorderTraversal(root.left))
        if root.right:
            res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res