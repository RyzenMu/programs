class Node:
    def __init__(self, value):
        self.data = value

class LinkedStack:

    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
        else:
            temp = Node(value)
            temp.next = self.top
            self.top = temp

    def pop(self):
        if 