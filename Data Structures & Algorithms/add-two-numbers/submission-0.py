# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        prev = ListNode(None, None)
        while l1 or l2:
            temp = 0

            # addition
            if l1:
                temp += l1.val
            if l2:
                temp += l2.val
            if carry:
                temp += 1
                carry = False

            # calc the carry over
            if temp >= 10:
                carry = True
                temp -= 10
            
            # create the new node
            curr = ListNode(temp, None)

            # set the head for the answer
            if prev.val == None and prev.next == None:
                head = curr
            prev.next = curr
            prev = curr

            # move l1 and l2
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            curr.next = ListNode(1, None)
        return head