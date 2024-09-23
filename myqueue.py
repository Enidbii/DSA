#!/usr/bin/python3 env
from node import Node

class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def print_queue(self):
        temp = self.first
        if self.length == 0:
            return
        while temp:
            print(temp.value, end=' ')
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        #print(new_node.value, end=' ')
        return new_node

    def dequeue(self):
        temp = self.first
        if self.length == 0:
            return None
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        #print(temp.value, end=' ')
        return temp
    def size(self):
        return self.length
    
# myqueue = MyQueue()
# myqueue.enqueue(9)
# myqueue.enqueue(10)
# myqueue.enqueue(11)
# myqueue.enqueue(12)
# myqueue.print_queue()
# print()
# myqueue.dequeue()