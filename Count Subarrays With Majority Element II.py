class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        prefix = 0
        sl = SortedList([0]) 
        ans = 0
        
        for num in nums:
            prefix += 1 if num == target else -1
           
            ans += sl.bisect_left(prefix)
            sl.add(prefix)
            
        return ans
