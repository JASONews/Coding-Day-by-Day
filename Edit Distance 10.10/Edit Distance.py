"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

Solution: DP
    arr[i][j] is minimum operations required to do when converting word1 to word2.
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        
        arr = [ [0 for i in range(0, n+1)] for j in range(0, m + 1)]
        
        for i in range(0, n+1):
            arr[0][i] = i
        for j in range(0, m+1):
            arr[j][0] = j
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[j-1] == word2[i-1]:
                    arr[i][j] = min(arr[i][j-1]+1, arr[i-1][j-1])
                else:
                    arr[i][j] = min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j]) + 1
        
        return arr[m][n]
