class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

        左闭右开区间
        """

        mat = [[0] * n for _ in range(n)]
        count = 1
        start = 0
        while start <= n//2:
            for j in range(start, n - 1 - start):
                mat[start][j] = count
                count += 1
            for i in range(start, n - 1 - start):
                mat[i][n - 1 - start] = count
                count += 1
                
            for j in range(n - 1 - start, start, -1):
                mat[n - 1 - start][j] = count
                count += 1
            for i in range( n - 1 - start, start, -1):
                mat[i][start] = count
                count += 1

            start += 1
        if (n % 2 == 1):
            mat[n//2][n//2] =count

        return mat
    
    def generateMatrix2(self, n):
        """
        不考虑边界, 撞墙限制, 
        边界收缩,解矩阵,螺旋遍历,对角线遍历,旋转矩阵,围棋边缘处理
        """
        mat = [[0]*n for _ in range (n)]
        count = 1
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        while count <= n**2:
            for j in range(left, right + 1):
                mat [top][j] = count
                count += 1
            top += 1
            for i in range(top, bottom + 1):
                mat[i][right] = count
                count += 1
            right -= 1
            
            for j in range(right, left - 1, -1):
                mat[bottom][j] = count
                count += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                mat[i][left] = count
                count += 1
            left += 1
        return mat



    
    
        
