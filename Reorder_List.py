# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:return
        slow = fast = head
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
        prev,curr = None,slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        node1,node2 = head,prev
        while node2.next:
            temp = node1.next
            node1.next = node2
            node1 = temp
            
            temp = node2.next
            node2.next = node1
            node2 = temp
