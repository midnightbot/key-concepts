# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        def replacementnode(root):
            cur = root.right
            while cur is not None and cur.left is not None:
                cur = cur.left
                
            return cur
        
        def remove(root,key):
            if root is None:
                return None
            
            elif root.val > key:
                root.left = remove(root.left,key)
                
            elif root.val < key:
                root.right = remove(root.right, key)
            
            elif root.val == key:
                if root.left is None and root.right is None:##no child
                    return None
                
                elif root.left is None and root.right is not None:##only right child
                    return root.right
                
                elif root.right is None and root.left is not None:##only left child
                    return root.left
                
                elif root.left is not None and root.right is not None:##both child
                    ##replace right subtrees smallest node with this node and then it will be at the end(without any children, them simply remove it)
                    p = replacementnode(root)
                    root.val = p.val
                    root.right = remove(root.right,p.val)
                       
            return root
        return remove(root,key)
        #return root
