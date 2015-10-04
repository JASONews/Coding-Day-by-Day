"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lmax = nums[0]
        lmin = nums[0]
        maxi = nums[0]
    
        for i in range (1, n):
            temp = lmax
            lmax = max(lmax*nums[i], lmin*nums[i], nums[i])
            lmin = min(temp*nums[i], lmin*nums[i], nums[i])
            maxi = max(maxi, lmax)

        return maxi