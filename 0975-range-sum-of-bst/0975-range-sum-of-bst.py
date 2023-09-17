# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # if there is no node sum should be zero
        if not root: 
            return 0 
        
        # root value < low ? call rangeSumBST with the right node as root
        elif root.val < low :
            return self.rangeSumBST(root.right, low, high)
        
        # root value > high ? call rangeSumBST with the left node as root
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        # root value within range? sum up all the value of nodes
        return root.val + self.rangeSumBST(root.left, low, high)+ self.rangeSumBST(root.right , low, high)

        