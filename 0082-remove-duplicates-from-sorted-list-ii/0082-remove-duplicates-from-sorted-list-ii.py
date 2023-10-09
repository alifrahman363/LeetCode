# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, None)
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next: 
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur.next, cur = None, cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next
        