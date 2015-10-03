"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Solution: DP
            set arr[j] where ob[i][j] is 1 to be 0
"""
class Solution(object):
    def uniquePathsWithObstacles(self, ob):
        """
        :type ob: List[List[int]]
        :rtype: int
        """
        ob = obstacleGrid 
        if len(ob) is 0:
            return 0
        if len(ob[0]) is 0:
            return 0
            
        arr = [0]*(len(ob[0]))
        arr[0] = 1
        for i in range(0, len(ob)):
            for j in range(0, len(arr)):
                if ob[i][j] is 1:
                    arr[j] = 0
                elif j > 0:
                    if i is 0:
                        arr[j] = arr[j-1]
                    else:
                        arr[j] = arr[j] + arr[j-1]
                        
        return arr[-1]
