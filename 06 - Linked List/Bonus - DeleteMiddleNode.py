class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None
        fast = head.next
        curr = head 
        while fast.next and fast.next.next:
            fast = fast.next.next
            curr = curr.next
        temp = curr
        temp = temp.next
        curr.next = temp.next
        return head