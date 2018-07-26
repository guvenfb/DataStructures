import sys

class Node:
    def __init__(self,data):
        self.right = self.left = None
        self.data = data


class Solution:

    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def levelOrder(self, root):

        myqueue = [root] # get the root as the first element of the queue
        while len(myqueue) > 0: # as long as we have something in it

            if myqueue[0].left is not None:
                myqueue.append(myqueue[0].left)  # add the left guy
            if myqueue[0].right is not None:
                myqueue.append(myqueue[0].right)  # add the right guy
            print(myqueue[0].data, end = " ")
            myqueue.pop(0)  # get rid of the element




a = [3,5,4,7,2,1]
myTree=Solution()
root=None
for i in range(len(a)):
    data=a[i]
    root=myTree.insert(root,data)
myTree.levelOrder(root)

# 3 2 5 1 4 7