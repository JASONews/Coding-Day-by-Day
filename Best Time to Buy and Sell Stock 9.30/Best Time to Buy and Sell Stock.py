"""Leetcode
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one 
    share of the stock), design an algorithm to find the maximum profit.

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n is 0:
            return 0
        
        maxi = 0
        mini = prices[0]
        
        for i in range(1, n):
            v = prices[i]-mini
            mini = prices[i] if prices[i] < mini else mini
            if maxi < v:
                maxi = v
                
        return maxi