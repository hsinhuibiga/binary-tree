#Populating Next Right Pointers in Each Node II

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        Q = collections.deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node=Q.popleft()
                if i<size-1:
                    node.next=Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root