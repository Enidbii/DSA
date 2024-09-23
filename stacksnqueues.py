#!/usr/bin/python3 env
import sys
from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

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
    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            curr = temp.next
            temp.next = None
            self.top = curr
        return temp
class Queue:
    def __init__(self, value=False):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp, end=' ')
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.next = None
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            temp = self.first
            curr = temp.next
            temp.next = None
            self.first = curr
        self.length -= 1
        return temp.value
    def size(self):
        return self.length

def reverse_string(string):
    stack = Stack()

if __name__ == "__main__":
    queue1 = Queue(1)
    print(type(queue1))
    queue1.enqueue(2)
    queue1.enqueue(3)
    queue1.enqueue(4)
    queue1.enqueue(5)
    queue1.print_queue()
    print()
    lenngth = queue1.size()
    for _ in range(lenngth):
        list_1 = []
        x = queue1.dequeue()
        print(type(x))
        list_1.append(x)
        stack1 = list_1.pop()
        stack2 = Stack(stack1)
        stack2.push(stack1)
        print(stack2, end=' ')

        # print(x.value)
        # new_queue = Queue(x)
        # new_queue.enqueue(x)
    # x = Stack(x)
    # x.push(x)
    # print(x)

     # print()
     # queue1.print_queue()
