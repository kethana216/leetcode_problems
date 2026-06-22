class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for char in text:
            if char in count:
                count[char] += 1
    
        count['l'] //= 2
        count['o'] //= 2
        
        return min(count.values())
