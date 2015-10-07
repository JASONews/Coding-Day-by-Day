"""
# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# Defination for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generate_tree(1, n)
        
        
    def generate_tree(self, st, ed):
        gtrees = []
        if st > ed or st <= 0 or ed <= 0:
            gtrees.append(None)
            return gtrees
        if st == ed:
            gtrees.append(TreeNode(st))
            return gtrees
            
        for i in range(st, ed+1):
                ltree = self.generate_tree(st, i-1)
                rtree = self.generate_tree(i+1,ed)
                for j in range(0,len(ltree)):
                    for k in range(0, len(rtree)):
                        t = TreeNode(i)
                        t.left = ltree[j]
                        t.right = rtree[k]
                        gtrees.append(t)
        return gtrees
        
        
