class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = defaultdict(int)
        count[0] = 1 
        
        prefix_sum = 0
        ans = 0
        
        for num in nums:
           
            if num == target:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            
            for prev_sum in range(prefix_sum):
                ans += count[prev_sum]
            
            count[prefix_sum] += 1
        
        return ans      
