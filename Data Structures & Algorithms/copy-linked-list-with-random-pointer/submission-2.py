"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        import copy
        nodes = {}
        curr = head
        if not head: return
        def populate_map(node):
            if node and node not in nodes:
                nodes[node] = copy.copy(node)
                populate_map(node.next)
                populate_map(node.random)
            return

        populate_map(curr)

        curr = head
        while curr:
            nc = nodes[curr]
            if curr.next:
                nc.next = nodes[curr.next]
            if curr.random:
                nc.random = nodes[curr.random]
            curr = curr.next

        return nodes[head]