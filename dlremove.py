#!/usr/bin/python3 env

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def forward_traversal(self):
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
        new_node.prev = self.tail
        self.tail = new_node

    def size(self):
        return self.length


    def remove_at_index(self, index):
        """ remove at a given point """
        temp = self.head
        if temp is None:
            return None
        for _ in range(index):
            temp = temp.next
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        return temp

if __name__ == "__main__":
    llist = DoublyLinkedList(12)
    llist.append(13)
    llist.append(14)
    llist.append(15)
    llist.append(16)
    llist.append(17)
    llist.append(18)
    llist.forward_traversal()
    print()
    llist.remove_at_index(3)
    llist.forward_traversal()