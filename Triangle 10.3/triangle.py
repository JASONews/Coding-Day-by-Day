"""Leetcode
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Solution: DP
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        tri = triangle
        n = len(tri)
        
        if n is 0:
            return 0
            
        m = len(tri[n-1])
        arr = list(tri[n-1])
        
        brr = range(0,n-1)[::-1]
        
        for i in  brr:
            for j in range(0, len(tri[i])):
                arr[j] = tri[i][j] + min(arr[j],arr[j+1])
                
        return arr[0]