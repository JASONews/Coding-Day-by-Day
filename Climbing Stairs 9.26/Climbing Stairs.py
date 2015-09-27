"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Solution: Dynamic programing (fibonacci)
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is 0:
            return 0
            
        arr = [-1]*(n+1)
        
        arr[0] = 1
        
        if n >= 1:
            arr[1] = 1
            
        
        return self.climb(n,arr)
        
    def climb(self, n, arr):
        if arr[n] is not -1:
            return arr[n]
            
        val = self.climb(n-1, arr)+self.climb(n-2, arr)
        arr[n] = val
        return val