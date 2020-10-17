# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes. Only nodes itself may be changed.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        n = head.next

        p.next = self.swapPairs(n.next)
        n.next = p
        return n
    
    