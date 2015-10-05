"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
Solution: DP
        the list of all ugly number is produced by following three list:
        1x2 2x2 3x2 4x2 5x2 ...
        1x3 2x3 3x3 4x3 5x3 ...
        1x5 2x5 3x5 4x5 5x5 ...
        therefore, the list arr store the list of ugly numbers
        we find a way to sort these three lists 
        i, j, k respectly represent the index of above three lists.
        the new elmenent of arr should be the smllest value in all 
        three lists. i.e.
            arr[m] = min(arr[i]*2, arr[j]*3, arr[k]*5)
"""
ass Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is 0 or n is 1:
            return n
        
        arr = [1]*n
        i, j, k = 0, 0, 0
        for m in range(1, n):
            vi, vj, vk = arr[i]*2, arr[j]*3, arr[k]*5
            arr[m] = min(vi, vj, vk)
            i += (vi == arr[m])
            j += (vj == arr[m])
            k += (vk == arr[m])
            
            
        return arr[-1]
                
