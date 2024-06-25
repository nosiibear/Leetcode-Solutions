# Date: 5/19/23
# Problem: 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of
# its nodes' values. (i.e., from left to right, level by level).

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def findHeight(root, height):
            if root == None:
                return height
            print(root.val)
            return max(findHeight(root.left, height+1), findHeight(root.right, height+1))

        def findLevel(root, level, result):
            if root != None:
                if level == 0:
                    result.append(root.val)
                findLevel(root.left, level-1, result)
                findLevel(root.right, level-1, result)
        
        if root == None:
            return []
        
        height = findHeight(root, 0)
        result = []
        for i in range(0, height):
            level = []
            findLevel(root, i, level)
            result.append(level)
        print(result)

        return result
            

nodes = []
nums = [3, 9, 20, 77, 21, 15, 7]
for i in range(0, 7):
    nodes.append(TreeNode(nums[i]))

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
nodes[6].left = TreeNode(123)

#print(nodes[0].left.val)

print(Solution.levelOrder(Solution, nodes[0]))
