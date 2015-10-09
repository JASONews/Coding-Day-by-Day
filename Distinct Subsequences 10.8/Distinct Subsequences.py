"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"
"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)
        
        if n is 0:
            return 0
        if m is 0:
            return 1
            
        if m > n:
            return 0

        arr = [[0 for i in range(0, n)] for j in range(0, m)]
        
        if s[0] == t[0]:
                arr[0][0] = 1
                
        for j in range(1, n):
            if s[j] == t[0]:
                arr[0][j] = arr[0][j-1] + 1
            else:
                arr[0][j] = arr[0][j-1]
                
        for i in range(1, m):
            for j in range(1, n):
                if s[j] == t[i]:
                    arr[i][j] = arr[i-1][j-1]+arr[i][j-1]
                else:
                    arr[i][j] = arr[i][j-1]
        return arr[-1][-1]
