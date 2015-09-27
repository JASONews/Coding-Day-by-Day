class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length is 0:
            return 0
        
        vals = [[-1 for i in range(0,length)] for j in range(0, length)]
        print nums
        print vals
        maxval = self.max_value(0,length-1,nums,vals)
        print vals
        return maxval

    def max_value (self, st, ed, nums, vals):
        print st,ed

        if vals[st][ed] is not -1:
            print vals
            return vals[st][ed]



        if st is ed:
            print "eq %s %s" % (st, ed)
            vals[st][ed] = nums[st]
            print vals
            return vals[st][ed]

        if ed - st is 1:
            print "=1= %s %s" % (st, ed)
            vals[st][ed] = max(nums[st],nums[ed])
            print vals
            return vals[st][ed]
        
        imax = [0]*(ed-st+1)
        
        for i in range(st,ed+1):
            print "index %s" % (i)
            left = self.max_value(st,i-2,nums,vals) if i-2 >= st else 0
            right = self.max_value(i+2, ed, nums, vals) if i+2 <= ed else 0
            print "left: %s right: %s" % (left, right)
            imax[i-st] = max(left,right) + nums[i]
        
        vals[st][ed] = max(imax)
        print vals
        return vals[st][ed]

print Solution().rob([1,2,1,0])
