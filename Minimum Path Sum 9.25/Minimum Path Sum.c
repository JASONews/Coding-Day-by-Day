int minPathSum(int** grid, int gridRowSize, int gridColSize) {
	 
	int * ans = (int *)malloc(sizeof(int)*(gridColSize+1));
	int right = 0;
	int down = 0;
	int ret = 0;
	 
	for (int k = 0; k < gridColSize+1; k++) {
		ans[k] = ~(1 << 31);
	}
	
	ans[gridColSize-1] = 0;
	 
	for (int i = gridRowSize, j = 0; i > 0; i--) {
		 
		for (j = gridColSize; j > 0; j--) {
			right = ans[j];
			down = ans[j-1];
			ans[j-1] = grid[i-1][j-1] + (right > down ? down : right);
		}
	}

	ret = ans[0];
	free(ans);
	return ret;
}
