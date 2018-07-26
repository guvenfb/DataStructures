class Solution:
    # Write your code here
    def __init__(self):
        self.__stack = []
        self.__queue = []  # initialize the stack and the queue

    def pushCharacter(self, ch):  # push the character onto a stack
        self.__stack = [ch] + self.__stack

    def enqueueCharacter(self, ch):  # enqueue the character in a queue
        self.__queue.append(ch)

    def popCharacter(self):
        popped = self.__stack[0]
        self.__stack = self.__stack[1:]
        return popped

    def dequeueCharacter(self):
        dequeued = self.__queue[0]
        self.__queue = self.__queue[1:]
        return dequeued


s = "racecar"
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")