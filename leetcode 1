# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        max_sum = 0
        n = len(vals)
        for i in range(n // 2):
            twin_sum = vals[i] + vals[n - 1 - i]
            max_sum = max(max_sum, twin_sum)
        
        return max_sum
