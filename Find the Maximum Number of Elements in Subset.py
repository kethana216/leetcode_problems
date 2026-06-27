from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        ans = 1 
        
        
        if 1 in cnt:
            ans = max(ans, cnt[1] - (1 - cnt[1] % 2))
        
        for x in cnt:
            if x == 1: 
                continue
                
            length = 0
            cur = x
            while cnt[cur] >= 2:
                length += 2
                cur = cur * cur
                if cur > 10**9: 
                    break
        
            
            if cnt[cur] >= 1:
                length += 1
            else: 
              
                length -= 1
            
            ans = max(ans, length)
        
        return ans
