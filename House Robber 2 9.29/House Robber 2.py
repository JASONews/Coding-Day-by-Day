"""
After robbing those houses on that street, the thief has found himself a new 
place for his thievery so that he will not get too much attention. This time,
 all houses at this place are arranged in a circle. That means the first house 
 is the neighbor of the last one. Meanwhile, the security system for these houses 
 remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Solution: Dynamic programing (fibonacci)
    fn 0 - n-1 
    vn 1 - n-2 
    fn and vn are approach of houses rober I 
    ans = max { fn-1, vn-2 + money.nth }
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n is 0:
            return 0
        
        if n < 4:
            return max(nums)
            
        fn_1 = max(nums[1], nums[0]) # f1
        fn_2 = nums[0] # f0
        fn = 0
        
        vn_1 = 0 # v1 1-2
        vn_2 = 0 # v0 start from 1
        vn = 0
        
        for i in range(2, n-1):
            
            # 0 - n-1
            fn = max(fn_2 + nums[i], fn_1)
            fn_2 = fn_1
            fn_1 = fn
            
            # 1 - n-2
            vn = max(vn_1, vn_2+nums[i-1])
            vn_2 = vn_1
            vn_1 = vn
            
        return max(fn, vn+nums[n-1])
