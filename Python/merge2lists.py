# Date: 5/16/23
# Problem: 21. Merge Two Sorted Lists
# Description: Merge the two given sorted lists into one
# by splicing their nodes together.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        i1 = list1
        i2 = list2
        merge = ListNode(None, None)
        if i1.val < i2.val:
            merge.val = i1.val
            i1 = i1.next
        else:
            merge.val = i2.val
            i2 = i2.next
        mergeHead = merge
            
        #print("Merge: " + str(merge.val))
        
        while i1 != None and i2 != None:
            #print("i1: " + str(i1.val))
            #print("i2: " + str(i2.val))
            #print("mg: " + str(merge.val))
            if i1.val < i2.val:
                merge.next = ListNode(i1.val, None)
                i1 = i1.next
            else:
                merge.next = ListNode(i2.val, None)
                i2 = i2.next
            merge = merge.next

        if i1 == None:
            merge.next = i2
        else:
            merge.next = i1

        return mergeHead

list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
list3 = ListNode(1, None)
iter = list1
newList = ListNode(iter.val, None)
newListHead = newList
while iter != None and iter.next != None:
    iter = iter.next
    newList.next = ListNode(iter.val, None)
    newList = newList.next
iter = newListHead
#print("here")
while iter != None and iter.val != None:
    #print(iter.val)
    iter = iter.next

iter = Solution.mergeTwoLists("a", list1, list2)
print("solution")
while iter != None:
    print(iter.val)
    iter = iter.next
