# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if(head.next == None):
            return None

        nowN = 0
        lastP = nowP = returnP = nextP = head

        while(nowP.next != None):
            if((nowN - n + 1) >= 0): #lastP & nextP 右移
                if((nowN - n + 1) == 0):
                    nextP = nextP.next
                elif((nowN - n + 1) == 1):
                    nowP  = nowP.next
                    nextP = nextP.next
                else:
                    lastP = lastP.next
                    nowP  = nowP.next
                    nextP = nextP.next
            else:                   #lastP & nextP 不动
                nowP = nowP.next

            nowN = nowN + 1

        #返回returnP
        if ((nowN - n + 1) == 0):
            return head.next
        else:
            lastP.next = nextP
            return returnP


node5 = ListNode(5)
node4 = ListNode(4)
node4.next = node5

node3 = ListNode(3)
node3.next = node4

node2 = ListNode(2)
node2.next = node3

node1 = ListNode(1)
node1.next = node2

list = node1

# while(list != None):
#     print(list.val)
#     list = list.next

num = 5
print('num -', num)

solution = Solution()
resultP = solution.removeNthFromEnd(list, num)

while(resultP != None):
    print(resultP.val)
    resultP = resultP.next
