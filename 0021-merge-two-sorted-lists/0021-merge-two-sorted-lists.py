# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 
        
        # when list1 and list2 are not null
        while list1 and list2: 
            if list1.val < list2.val:
                # take list1 value and insert it into tail
                tail.next = list1
                # update pointer 
                list1 = list1.next
            # if list2 vlaues are smaller or equal to list1 value
            else:
                # insert list2 values into tail
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        #If one of the list is empty then just return the other list.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2 

        return dummy.next


        