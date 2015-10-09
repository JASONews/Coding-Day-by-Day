"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)  -3      3
-5      -10     1
10      30      -5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Solution: DP
   rolling array arr[i] = the minimum point required to start at dungeon[i][j].
"""
ass Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        d = dungeon
        m = len(d)
        if m == 0:
            return 0
            
        n = len(d[0])
        
        if n is 0:
            return 0
        
        arr = [1 << 31] * (n+1)
        
        if d[-1][-1] >= 0:
            arr[-2] = 1
        else:
            arr[-2] = 0 - d[-1][-1] + 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                submin = min(arr[j], arr[j+1])
                cv = submin - d[i][j]
                if cv < 1:
                    cv = 1
                arr[j] = cv
                
        return arr[0]
        
        
