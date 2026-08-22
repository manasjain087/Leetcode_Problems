"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self,x,next=None,random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
            

        # Original node -> copied node
        mapping = {}

        # Step 1: Create copied nodes
        current = head

        while current:
            mapping[current] = Node(current.val)
            current = current.next

        # Step 2: Connect next and random
        current = head

        while current:
            copy_node = mapping[current]

            copy_node.next = mapping.get(current.next)
            copy_node.random = mapping.get(current.random)

            current = current.next

        return mapping[head]
        