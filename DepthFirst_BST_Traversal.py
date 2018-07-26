import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):

        if root is None:
            pass
        else:
            # self.queue = [root.data]
            print(root.data, end = " ")
            self.levelOrder(root.left)
            self.levelOrder(root.right)

    def postOrder(self, root):
        # Write your code here
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end=" ")


a = [3, 5, 4, 7, 2]
myTree = Solution()
root = None
for i in range(len(a)):
    data = a[i]
    root = myTree.insert(root, data)
myTree.levelOrder(root)
print(" ")
myTree.postOrder(root)