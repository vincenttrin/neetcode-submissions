# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approach 1: go through each list and add element to the list. time intensive and inneficient
# approach 2: Iterate through all lists. Create a heap, pop from heap and build a linked list.

# do we need to return a linked list with the node objects or are values enough?

class Solution:    
    import heapq
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for ll in lists:
            temp = ll
            while temp:
                heapq.heappush(nodes, temp.val)
                temp = temp.next

        if not nodes:
            return None
        curr = ListNode(heapq.heappop(nodes), None)
        head = curr
        while nodes:
            temp = ListNode(heapq.heappop(nodes), None)
            curr.next = temp
            curr = temp
        return head
