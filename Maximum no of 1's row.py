class Solution:
    def maxOnes (self, Mat, N, M):
        # code here 
        i, j = 0, 0
        while (i <= N or j < M):
            if Mat[i][j] == 1:
                return i
            elif i == N-1:
                i = 0
                j += 1
            else:
                i += 1
        return -1
