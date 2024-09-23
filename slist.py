#!/usr/bin/python3 env
from types import NoneType


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.next = None
        self.tail = new_node

    def set_value(self, index, value):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value


llist = LinkedList(12)
llist.append(13)
llist.append(14)
llist.append(15)
llist.append(16)
llist.print_list()
print()
llist.set_value(1, 32)
llist.print_list()

