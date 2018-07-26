class Node:
    def __init__(self,data):
        self.right = self.left = None
        self.data = data


class Solution:

    def __init__(self):
        self.maxheight = -1


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

    def MGinsert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data > root.data:
                current = root.right
                root.right = self.MGinsert(current, data)
            else:
                current = root.left
                root.left = self.MGinsert(current, data)
        return root

    def getHeight(self, root):  # get the height of the BST --> recursive. Mine is also recursive, and correct if I could set self.maxheight to an initial value outside of the getHeight function. HackerRank did not allow for that
        if root is None:
            return -1
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

'''
        if root is not None:
            self.height = 0
            self.getHeight(root.left)
            self.getHeight(root.right)
            self.height += 1
            print(self.height, self.maxheight)
            # print(self.maxheight)
            if self.height > self.maxheight:
                self.maxheight = self.height

        return self.maxheight - 1
'''
a = [3, 5, 2, 1, 4, 6, 7, 9, 8, 122]
# a = [3,4]
myTree = Solution()
root = None
root2 = None
for i in range(len(a)):
    data = a[i]
    root = myTree.insert(root, data)
    root2 = myTree.MGinsert(root2, data)

height = myTree.getHeight(root)
print(height)
height = myTree.getHeight(root2)
print(height)