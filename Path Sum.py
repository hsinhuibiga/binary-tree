#Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        queue = [(root, sum)]
        while len(queue) > 0:
            node, tmp_sum = queue.pop()
            if node:
                if not node.left and not node.right and node.val == tmp_sum:
                    return True
                queue.insert(0, (node.right, tmp_sum-node.val))
                queue.insert(0, (node.left, tmp_sum-node.val))
        return False