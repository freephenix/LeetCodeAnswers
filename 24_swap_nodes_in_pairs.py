# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pHead=head
        pHeadNext=head.next
        pHead.next=self.swapPairs(pHeadNext.next)
        pHeadNext.next=pHead
        return pHeadNext

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         new_h = ListNode(-1)
#         new_h.next = head
#         p1 = new_h
#         p2 = p1.next
#        
#         while p2!=None and p2.next!=None:
#             p1.next = p2.next
#             p2.next = p1.next.next
#             p1.next.next = p2
#            
#             p1 = p2
#             p2 = p2.next
#        
#         return new_h.next