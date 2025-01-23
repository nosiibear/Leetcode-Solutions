# Date: 5/19/23
# 98. Validate Binary Search Tree
# Given the root of a binary tree determine
# if it is a valid binary search tree (BST).

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        def bstSearch(root, low, high):
            print("---")
            print(root.val if root else "Empty")
            print(low)
            print(high)
            if root == None:
                return True
            else:
                if high != None and root.val >= high:
                    return False
                if low != None and root.val <= low:
                    return False
                return bstSearch(root.left, low, root.val) and bstSearch(root.right, root.val, high)

        return bstSearch(root, None, None)

nodes = []
nums = [10, 5, 15, 3, 6, 9, 30]
for i in range(0, 7):
    nodes.append(TreeNode(nums[i]))

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
#nodes[6].left = TreeNode(123)

#print(nodes[0].left.val)

print(Solution.isValidBST(Solution, nodes[0]))
