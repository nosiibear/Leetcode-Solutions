# Date: 5/16/23
# Problem: 876. Middle of the Linked List
# Description: Given the head of a singly linked list,
# return the middle node of the linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        i = 1
        middle = head
        while head != None:
            head = head.next
            if i % 2 == 0:
                middle = middle.next
            i += 1

        return middle
        
head = ListNode(1, ListNode(2, ListNode(4, ListNode(8, ListNode(11, None)))))
iter = Solution.middleNode("a", head)
print("solution")
print(id(iter))
while iter != None:
    print(iter.val)
    iter = iter.next
