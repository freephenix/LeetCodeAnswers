# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        trees = []
        trees.append(root)
        while trees:
            node = trees.pop()
            if not node:
                continue
            tmp = node.left
            node.left = node.right
            node.right = tmp
            trees.append(node.left)
            trees.append(node.right)
        return root