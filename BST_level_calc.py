import math


class Node:
    def __init__(self, data, level):
        self.right = self.left = None
        self.data = data
        self.level = level


def ispower(n, base):
    if n == base:
        return True

    if base == 1:
        return False

    temp = base

    while (temp <= n):
        if temp == n:
            return True
        temp *= base

    return False


class Solution:
    def __init__(self):
        self.maxheight = -1

    def insert(self, root, data, level):
        if root is None:
            return Node(data, level)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data, root.level + 1)
                root.left = cur
            else:
                cur = self.insert(root.right, data, root.level + 1)
                root.right = cur
        return root

    def levelOrder(self, root):

        myqueue = [root]  # get the root as the first element of the queue
        count = 1
        cost = 0
        node_count = 1
        while len(myqueue) > 0:  # as long as we have something in it

            '''
            if ispower((count + 1),2):
                print("hey")
                level = math.log2(count+1) - 1
                cost = cost + node_count * level
                node_count = 0
            '''
            count += 1
            if myqueue[0].left is not None:
                myqueue.append(myqueue[0].left)  # add the left guy
                # print(myqueue[0].left.level)
                cost = cost + myqueue[0].left.level
                node_count += 1
            count += 1  # increment

            if myqueue[0].right is not None:
                myqueue.append(myqueue[0].right)  # add the right guy
                # print(myqueue[0].right.level)
                cost = cost + myqueue[0].right.level
                node_count += 1
            myqueue.pop(0)  # get rid of the top element
            # print(cost)
            # print(node_count)
        # cost = cost + node_count * (1 + level)
        return cost


n = int(input())
a = list(map(int, input().split()))  # get the array

myTree = Solution()
root = None
root = myTree.insert(root, a[0], 0)
for i in range(1, n):
    data = a[i]
    root = myTree.insert(root, data, 0)

print(myTree.levelOrder(root))
