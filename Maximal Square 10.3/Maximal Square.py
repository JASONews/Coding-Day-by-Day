"""Leetcode
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

Solution: DP
    arr[i][j] represents the length of square end at matrix[i][j]
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ma = matrix
        n = len(matrix)
        if n is 0:
            return 0
            
        m = len(matrix[0])
        if m is 0:
            return 0
        arr = [[0 for k in range(0, m)] for q in range(0, 2)]
        maxi = 0
        for i in range(0, n):
            for j in range(0, m):
                arr[i%2][j] = int(ma[i][j])
                if i*j > 0 and ma[i][j] == '1':
                    arr[i%2][j] = min(arr[(i-1)%2][j], arr[i%2][j-1], arr[(i-1)%2][j-1]) + 1
                if maxi < arr[i%2][j]:
                    maxi = arr[i%2][j]
    
        return maxi**2