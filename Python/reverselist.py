# Date: 5/16/23
# Problem: 206. Reverse Linked List
# Description: Given the head of a singly linked list,
# reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return None

        prev = None
        
        while head != None:
            print(head.val)
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
        
head = ListNode(1, ListNode(2, ListNode(4, None)))
iter = Solution.reverseList("a", head)
print("solution")
while iter != None:
    print(iter.val)
    iter = iter.next
