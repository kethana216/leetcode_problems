class Solution:
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        size = r - l + 1
        
        if size == 1:
            return 0 if n > 1 else 1
        
        dp_up = [[0] * size for _ in range(n)]
        dp_down = [[0] * size for _ in range(n)]

        for j in range(size):
            dp_up[0][j] = 1
            dp_down[0][j] = 1
        
        for i in range(1, n):
        
            prefix_down = 0
            for j in range(size):
                dp_up[i][j] = prefix_down
                prefix_down = (prefix_down + dp_down[i-1][j]) % MOD
         
            suffix_up = 0
            for j in range(size - 1, -1, -1):
                dp_down[i][j] = suffix_up
                suffix_up = (suffix_up + dp_up[i-1][j]) % MOD
        
        ans = 0
        for j in range(size):
            ans = (ans + dp_up[n-1][j] + dp_down[n-1][j]) % MOD
            
        return ans
