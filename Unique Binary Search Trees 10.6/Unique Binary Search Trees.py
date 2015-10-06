"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Solution: DP
        if we choose i as root then there are left: 0~i-1 right: i+1~n sub trees
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        arr = [0] * (n+1)
        arr[0] = 1
        arr[1] = 1
        for i in range(2, n+1):
            for j in range(1,i+1):
                arr[i] += arr[j-1]*arr[i-j]
        
        return arr[-1]
