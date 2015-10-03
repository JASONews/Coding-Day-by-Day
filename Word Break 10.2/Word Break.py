"""Leetcode
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

Solution: DP
    arr[i] represents substring from 0 to i is whether breakable 
    First check if 0-ith substring if in wordDict
    if not, then check all substring that can be broken + endofsubstring-ith
    
"""
class Solution(object):
    
    def wordBreak(self, s, wd):
        n = len(s)
        
        if n is 0 or n is 1:
            return s in wd
            
        arr = [False]*n
        
        for i in range(0, n):
            if s[0:i+1] in wd:
                arr[i] = True
                continue
            for j in range(0, i):
                if arr[j]:
                    if s[j+1:i+1] in wd:
                        arr[i] = True
                        break
        return arr[n-1]