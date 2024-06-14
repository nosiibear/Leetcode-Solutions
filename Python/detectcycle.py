# Date: 5/16/23
# Problem: 142. Linked List Cycle II
# Given the head of a linked liste, return the node where the cycle begins.
# If there is no cycle, return null.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        temp = head
        nodeList = [temp]
        print(type(nodeList))
        while temp.next != None:
            if temp.next in nodeList:
                print(type(temp.next))
                return temp.next
            else:
                nodeList.append(temp.next)
            temp = temp.next
        return null
        
list1 = ListNode(3)
list1.next = ListNode(2)
list1.next.next = ListNode(0)
list1.next.next.next = ListNode(-4)
list1.next.next.next.next = list1.next
node = Solution.detectCycle("a", list1)
print(type(node))
print(node.val)
#print(id(list1))
#print(id(list1.next))
#last = id(list1)
#iter = list1.next

#while iter != None:
    #print("iter")
    #print(id(iter))
    #print("last")
    #print(last)
    #print("num: " + str(iter.val))
    #print(id(iter) - last)
    #last = id(iter)
    #iter = iter.next
    
