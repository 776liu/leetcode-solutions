# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        判断有环之后返回节点，哈希不满足常数空间级
        快慢指针找相遇点，再有两个指针走圈找节点

        slow:A+B
        fast:A+B+n(B+C)

        A = (n-1)(B+C)+C
        """
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                point1 = slow
                point2 = head

                while point1 != point2:
                    point1 = point1.next
                    point2 = point2.next

                return point1
            
        return None


                



        