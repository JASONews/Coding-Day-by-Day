"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

Solution: Dynamic programing (fibonacci)
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        n = [0] * (l+1)
        
        if l is 0:
            return 0
        if l is 1:
            return 0 if int(s[0]) is 0 else 1
            
        n[0] = 1
        n[1] = 1 if int(s[0]) > 0 else 0
        
        for i in range(2, l+1):
            k = int(s[i-1])
            d = int(s[i-2:i])
            
            ki = 1 if k > 0 else 0
            di = 1 if d > 9 and d < 27 else 0
            
            n[i] = n[i-1] * ki + n[i-2] * di
            
        return n[l]
            
            
        