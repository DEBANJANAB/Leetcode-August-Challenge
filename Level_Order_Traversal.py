# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        
        def traversal(level,node):
            if node is not None:
                if len(ans)<=level:
                    ans.append([node.val])
                else:
                    ans[level].append(node.val)
                    
                traversal(level+1,node.left)
                traversal(level+1,node.right)
                
        traversal(0,root)
            
        return ans    