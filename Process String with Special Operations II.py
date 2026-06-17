class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        lengths = [0] * (n + 1)
        
        for i in range(n):
            ch = s[i]
            if ch.islower():
                lengths[i + 1] = lengths[i] + 1
            elif ch == '*':
                lengths[i + 1] = max(0, lengths[i] - 1)
            elif ch == '#':
                lengths[i + 1] = lengths[i] * 2
            elif ch == '%':
                lengths[i + 1] = lengths[i]
        
    
        if k >= lengths[n]:
            return '.'
        
    
        for i in range(n - 1, -1, -1):
            ch = s[i]
            L = lengths[i] 
            
            if ch.islower():
                if k == L: 
                    return ch
                
            elif ch == '*':
                
                continue
            elif ch == '#':
                
                if k >= L:
                    k -= L
            elif ch == '%':
                
                k = L - 1 - k
        
        return '.'
