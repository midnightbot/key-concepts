# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return TreeNode(val,None)
        def insert(val,root):
            
            if root is None:
                return
            
            elif root.val > val:
                if root.left:
                    insert(val,root.left)
                else:
                    root.left = TreeNode(val,None)
                    return root
                
            else:
                if root.right:
                    insert(val,root.right)
                    
                else:
                    root.right = TreeNode(val,None)
                    return root
                
        insert(val,root)
        return root
        
        
