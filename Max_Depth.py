class Solution:
    def dfs(self, node, max_depth=0, current_depth=0):
        if not node: #if previous node was a leaf
            return max(current_depth, max_depth)
            
        max_depth=self.dfs(node.left, max_depth, current_depth+1) #dfs in left branch
        max_depth=self.dfs(node.right, max_depth, current_depth+1) #dfs in right branch
        
        return max_depth
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.dfs(root)
        