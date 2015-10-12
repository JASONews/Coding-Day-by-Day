"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Solution: DP
    arr[i][j] represents when s1, s2 and s3 respectly in length of i, j and i+j, it is interleaving string or not.

"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n3 != n1 + n2:
            return False
        n1 += 1
        n2 += 1
        
        arr = [[ False for i in range(0, n2)] for j in range(0, n1)]
        
        arr[0][0] = True
        
        for i in range(1, n1):
            if s1[i-1] == s3[i-1]:
                arr[i][0] = True
            else:
                break
            
        for j in range(1, n2):
            if s2[j-1] == s3[j-1]:
                arr[0][j] = True
            else:
                break
        
        
        for i in range(1, n1):
            for j in range(1, n2):
                k = i + j -1
                left = arr[i][j-1] and s3[k] == s2[j-1]
                up = arr[i-1][j] and s3[k] == s1[i-1]
                arr[i][j] = left or up
                
        return arr[-1][-1]