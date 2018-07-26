class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def SortedInsert(head, data):
    if head is None:
        return Node(data)
    else:
        cur = head
        while data > cur.data and cur.next:
            cur = cur.next    # we have the location!

        new_node = Node(data)
        if cur.data < data:
            temp = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = temp

        else:
            temp = cur.prev
            new_node.next = cur
            new_node.prev = temp
            cur.prev = new_node
            if temp is None:
                head = new_node
            else:
                temp.next = new_node
        return head

def Make_DLL(head, data):
    cur = head

    if cur == None:
        head = Node(data)
        print("returning")
        return head

    while cur.next:

        cur = cur.next

    print("here", cur.data, data)
    new_node = Node(data)
    cur.next = new_node
    new_node.prev = cur


def show_DLL(head):
    cur = head
    while cur.next:
        print(cur.data, end = " ")
        cur = cur.next
    print(cur.data, end = " ")

head = Node(1)
liste = [4,8]
for i in liste:
    # print(i)
    Make_DLL(head, i)

# print(head.data, head.next.data)
# show_DLL(head)
head = SortedInsert(head, 13)
show_DLL(head)