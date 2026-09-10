# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        cur = slow.next
        slow.next=None
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev 
            prev = cur
            cur = nxt


        start, end = head, prev
        while end:
            tmp1 = start.next
            tmp2 = end.next

            start.next = end
            end.next = tmp1
            start = tmp1
            end = tmp2

            
        