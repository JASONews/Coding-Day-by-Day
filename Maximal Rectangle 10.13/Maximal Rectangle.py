"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

Solution: DP
    arr[i] : ith consequent 1s
    val[i] : the total value of i+min in the arr e.g. arr [1,2,1,0] then val's key range from 1 to 2
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ma = matrix
        
        m = len(ma)
        if m is 0:
            return 0
            
        n = len(ma[0])
        if n is 0:
            return 0

        arr = [0 for i in range(0, n)]

        maxi = 0
        for i in range(0, m):
                for j in range(0, n):
                        if ma[i][j] == '1':
                                arr[j] += 1
                        else:
                                arr[j] = 0

                tm = max(arr)
                mi = max(min(arr), 1)
                val = [0]*(tm-mi+1)

                for x in range(0, n):
                        for k in range(0, len(val)):
                                
                                if arr[x] >= k+mi > 0 and arr[x-1] >= k+mi > 0:
                                        val[k] += k+mi
                                else:
                                        if val[k] > maxi:
                                                maxi = val[k]
                                        if arr[x] >= k+mi:
                                                val[k] = k+mi
                                        else:
                                                val[k] = 0
                                if val[k] > maxi:
                                                maxi = val[k]

        return maxi

