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
        return self.head

    def set_value(self, index, value):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

    def bubble_sort(self):
        temp = self.head
        sorted = []
        if temp is None:
            return
        while temp:
            sorted.append(temp.value)
            temp = temp.next
        for i in range(len(sorted)-1, 0, -1):
            for j in range(i):
                if sorted[j] > sorted[j+1]:
                    temp = sorted[j]
                    sorted[j] = sorted[j+1]
                    sorted[j+1] = temp
        root = None
        for item in sorted:
            self.append(item)








llist = LinkedList(12)
llist.append(13)
llist.append(14)
llist.append(15)
llist.append(16)
llist.print_list()
print()
llist.set_value(1, 32)
llist.print_list()
print()
print(llist.bubble_sort())
