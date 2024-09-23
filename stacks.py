#!/usr/bin/python3 env
from node import Node

class Stack:
    def __init__(self):
        #new_node = Node(value)
        self.top = None
        self.height = 0

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value, end=' ')
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        #print("My returned node %s" % new_node)
        return new_node.value
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        print(temp.value, end=" ")
        return temp.value
    
    def size(self):
        return self.height
    
# stack = Stack()
# stack.push(12)
# stack.push(10)
# stack.push(9)
# stack.push(8)
# stack.push(7)
# stack.print_stack()
# print()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
