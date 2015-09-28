#include <stdio.h>
#include <stdlib.h>

/**
 * Leetcode
 * Given a positive integer n, find the least number of perfect square numbers 
 * (for example, 1, 4, 9, 16, ...) which sum to n.
 * For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, 
 * return 2 because 13 = 4 + 9.
 *
 * Solution: DP (我为人人型)
 */

int msqrt(int n) {
    float xn = n/2;
    while(xn*xn - n > 0.01 || xn*xn-n < -0.01)
        xn = xn - (xn*xn - n)/(xn*2);
    return (int)xn;
}

int numSquares(int n) {
    int * a = (int *) malloc(sizeof(int)*(n+1));
    int temp = 0;
    int sq = 0;
    for (int i = 0; i <n+1; i++)
        a[i] = ~(1 << 31);
    a[0] = 0;
    if (n > 0) {
        a[1] = 1;
        
        for (int i = 1; i < n+1; i++) {
            sq = msqrt(i);
            if (i == sq * sq)
                a[i] = 1;
            for (int j = 1; i + j*j <= n; j++) {
                if ((a[i]+1) < a[i+j*j])
                    a[i+j*j] = a[i]+1;
            }
        }
    }
    temp = a[n];
    free(a);
    return temp;
    
}