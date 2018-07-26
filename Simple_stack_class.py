class Stack:
    def __init__(self):
        self.elements = []
        self.max = None
        self.size = 0

    def insert(self, data):
        self.elements.append(data)
        if self.max is None:
            self.max = data
        else:
            self.max = max(data, self.max)
        self.size += 1

    def pop(self):
        popped = self.elements.pop(self.size-1)
        self.size = self.size - 1
        if popped == self.max:
            if self.size > 0:
                self.max = max(self.elements)
            else:
                self.max = None
    def print_max(self):
        print(self.max)

