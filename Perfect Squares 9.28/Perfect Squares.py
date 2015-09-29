import math
import time

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        vals = [n]*(n+1)
        vals[0] = 0
        if n > 0:
            vals[1] = 1
            for i in range(2,n+1):
                if i % int(math.sqrt(i)) is 0:
                        vals[i] = 1
                        continue
                for j in range(0, i):
                    vals[i] = min(vals[i], vals[i-j]+vals[j])
            
        return vals[n]

start = time.time()
n = 8328
s = Solution().numSquares(n)
print "time: %s ms" % ((time.time() - start)*1000)
print s, n
        