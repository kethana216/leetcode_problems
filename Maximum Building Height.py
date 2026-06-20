class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
    
        restrictions.sort()
        
        m = len(restrictions)
        
        
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0])
        
        
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0])
        
      
        ans = 0
        for i in range(1, m):
            h1, h2 = restrictions[i - 1][1], restrictions[i][1]
            dist = restrictions[i][0] - restrictions[i - 1][0]
            
            ans = max(ans, (h1 + h2 + dist) // 2)
            
        return ans
