# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = lt = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                lt.next = l1
                l1 = l1.next
            else:
                lt.next = l2
                l2 = l2.next
            lt = lt.next
        
        if l1:
            lt.next = l1
        elif l2:
            lt.next = l2
        return l.next