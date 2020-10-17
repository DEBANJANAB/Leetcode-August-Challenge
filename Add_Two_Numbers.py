# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode((l1.val + l2.val) % 10)
        c = (l1.val + l2.val) // 10
        node = result
        while l1.next or l2.next:
            s = (l1.next.val if l1.next else 0) + (l2.next.val if l2.next else 0) + c
            node.next = ListNode(s % 10)
            if l1.next:
                l1 = l1.next
            if l2.next:
                l2 = l2.next
            node = node.next
            c = s // 10
        if carry:
            node.next = ListNode(c)
        return result
    