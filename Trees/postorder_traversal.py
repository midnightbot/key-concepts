# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        self.ans = []
        
        def postorder(root):
            if root is not None:
                if root.left:
                    postorder(root.left)
                    
                if root.right:
                    postorder(root.right)
                    
                    
                self.ans.append(root.val)
                
                
        postorder(root)
        return self.ans
        
