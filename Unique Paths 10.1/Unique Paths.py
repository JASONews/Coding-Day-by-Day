"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Solution: dp
        split this problems into child problems 
        create an array arr[0,n] where a[i] is the way to go to ith block
        
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [0]*(n+1)
        arr[1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i is 1 and j > 1:
                    arr[j] = arr[j-1]
                else:
                    arr[j] = arr[j-1]+arr[j]
                    
        return arr[n]
