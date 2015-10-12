"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Solution: DP
    arr[i] reprsents the longest valid parentheses substring end at s[i]
"""
ass Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        
        arr = [0] * (n+1)
        par = []
        
        st = 1
        maxi = 0
        while st < n+1:
            if s[st-1] == '(':
                par.append([1, st])
                arr[st] = 0
            else:# == ')'
                if len(par) == 0:
                    par.append([-1, st])
                    arr[st] = 0
                elif par[-1][0]  == 1:
                    l = par.pop()
                    arr[st] = st - l[1] + 1 + arr[l[1] -1]
                else:
                    par.append([-1, st])
                    arr[st] = 0
            if arr[st] > maxi:
                maxi = arr[st]
            st += 1
        
        return maxi
        
        
        

