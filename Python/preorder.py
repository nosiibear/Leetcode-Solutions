# Date: 5/18/23
# Problem: 589. N-ary Tree Preorder Traversal
# Given the root of an n-ary tree,
# return the preorder traversal of its nodes' values.

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        def recursivePreorder(self, root, results):
            print(root.val)
            results.append(root.val)
            if root.children != None:
                for i in range(0, len(root.children)):
                    recursivePreorder(self, root.children[i], results)

        results = []
        recursivePreorder(self, root, results)
        print(results)
        return results

nodes = []
for i in range(0, 14):
    nodes.append(Node(i+1))

nodes[0].children = [nodes[1], nodes[2], nodes[3], nodes[4]]
nodes[2].children = [nodes[5], nodes[6]]
nodes[3].children = [nodes[7]]
nodes[4].children = [nodes[8], nodes[9]]
nodes[6].children = [nodes[10]]
nodes[7].children = [nodes[11]]
nodes[8].children = [nodes[12]]
nodes[10].children = [nodes[13]]

#print(nodes[0].val)
#print(nodes[0].children[0].val)
#print(nodes[0].children[2].val)


print(Solution.preorder(Solution, nodes[0]))
