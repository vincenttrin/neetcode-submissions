# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find Middle
        slow_tail = ListNode(0,head)
        slow, fast = head, head
        while fast and fast.next:
            slow_tail = slow_tail.next
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
            slow_tail=slow_tail.next

        middle = slow

        # split lists
        slow_tail.next = None

        # Reverse second half
        prev = None
        curr = middle
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        middle = prev
        # Merge Lists
        curr = head
        while curr and middle:
            f_temp = curr.next
            s_temp = middle.next

            curr.next = middle
            middle.next = f_temp
            curr = f_temp
            middle = s_temp
            