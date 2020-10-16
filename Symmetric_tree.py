def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            
            if left and right and left.val == right.val:
                stack.append((left.right, right.left))
                stack.append((left.left, right.right))
            elif left is None and right is None:
                continue
            else:
                return False
        
        return True