class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        size = r - l + 1
        
        if n == 1:
            return size
        if size == 1:
            return 0
        
        def mat_mul(A, B):
            res = [[0] * (2 * size) for _ in range(2 * size)]
            for i in range(2 * size):
                for k in range(2 * size):
                    if A[i][k]:
                        for j in range(2 * size):
                            res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            return res
        
        def mat_pow(mat, power):
            res = [[0] * (2 * size) for _ in range(2 * size)]
            for i in range(2 * size):
                res[i][i] = 1
            
            while power:
                if power & 1:
                    res = mat_mul(res, mat)
                mat = mat_mul(mat, mat)
                power >>= 1
            return res
        
        
        T = [[0] * (2 * size) for _ in range(2 * size)]
        
        
        for j in range(size):
            for k in range(j):
                T[k + size][j] = 1 
       
        for j in range(size):
            for k in range(j + 1, size):
                T[k][j + size] = 1 
 
        init = [1] * (2 * size)
        
        T_pow = mat_pow(T, n - 1)
        
       
        ans = 0
        for i in range(2 * size):
            row_sum = 0
            for j in range(2 * size):
                row_sum = (row_sum + T_pow[i][j] * init[j]) % MOD
            ans = (ans + row_sum) % MOD
        
        return ans
