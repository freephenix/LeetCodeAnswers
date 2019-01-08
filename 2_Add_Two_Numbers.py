# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        RListNode = ListNode(0);
        HListNode = RListNode;
        c = 0;
        while((l1 != None) | (l2 != None) | (c != 0)):

            if ((l1 == None) & (l2 == None)):
                if(c == 1) :
                    RListNode.val = c;
                    c = 0;

            elif(l1 == None):
                if ((l2.val + c) >= 10):
                    temp = l2.val + c - 10;
                    c = 1;
                else:
                    temp = l2.val + c;
                    c = 0;

                RListNode.val = temp;
                if((l2.next != None) | c==1):
                    RListNode.next = ListNode(0);
                    RListNode = RListNode.next;
                l2 = l2.next;

            elif (l2 == None):
                if ((l1.val + c) >= 10):
                    temp = l1.val + c - 10;
                    c = 1;
                else:
                    temp = l1.val + c;
                    c = 0;

                RListNode.val = temp;
                if ((l1.next != None) | c==1):
                    RListNode.next = ListNode(0);
                    RListNode = RListNode.next;
                l1 = l1.next;

            else:
                if ((l1.val + l2.val + c) >= 10):
                    temp = l1.val + l2.val + c - 10;
                    c = 1;
                else:
                    temp = l1.val + l2.val + c;
                    c = 0;

                RListNode.val = temp;
                if ((l1.next != None) | (l2.next != None) | c==1):
                    RListNode.next = ListNode(0);
                    RListNode = RListNode.next;
                l2 = l2.next;
                l1 = l1.next;

        return HListNode;


#初始化链表与数据
l1 = ListNode(1)
h1 = l1;
# l1.next = ListNode(4)
# l1 = l1.next;
# l1.next = ListNode(3)
# l1 = l1.next;
# l1.next = ListNode(2)
# l1 = l1.next;
# l1.next = ListNode(1)

l2 = ListNode(9)
h2 = l2;
l2.next = ListNode(9)
# l2 = l2.next;
# l2.next = ListNode(1)

solution = Solution()
PListNode = solution.addTwoNumbers(h1, h2);

while(PListNode != None):
    print(PListNode.val);
    PListNode = PListNode.next;
