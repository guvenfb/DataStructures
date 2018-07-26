class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head is None:
            self.head = Node(data)
            self.tail = self.head  # create a tail as well
            print("bostum")
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

            print("eklendim")

        return self.head  # i can return the head as well!

    def insertIntoN(self, head, data, nthLink):
        current = head
        count = 0
        if head: # by adding this, i made sure there is a non-None head
            while current.next and count < nthLink: # by checking current.next, I made sure temp = current.next does not fail
                current = current.next
                count += 1  #
                print(count)
            # this is where we want to add the new node
            temp = current.next
            print(temp)
            current.next = Node(data)  # the new node is added
            current.next.next = temp  # the rest of the links are added

        # return self.head
        return head


mylist= Solution()
T= [1,2,3,4,5]
head=None
for i in range(len(T)):
    data = T[i]
    head = mylist.insert(head,data)
mylist.display(head)
print("")
newhead = mylist.insertIntoN(head,99,0) # node count can be added as another private variable in case we try to add a node to N > size
mylist.display(newhead)

# Java: --> iterate to the tail every time you add a node
# public static  Node insert(Node head,int data){
# if(head == null){
#        return new Node(data);
#    }

# Node tmp = head;
# while(tmp.next != null){
#        tmp = tmp.next;
#    }
# tmp.next = new Node(data);
# return head;
# }