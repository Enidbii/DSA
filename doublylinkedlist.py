#!/usr/bin/python3 env


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

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

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def backward_traversal(self):
        temp = self.tail
        while temp:
            print(temp.value, end=' ')
            temp = temp.prev
        print()

    def insert(self, value):
        new_node = Node(value)
        temp = self.head
        new_node.next = temp
        if temp is not None:
            temp.prev = new_node
        self.head = new_node
        self.length += 1
        return self.head
    def insert_at_specific(self,value, k):
        new_node = Node(value)
        temp = self.head
        for _ in range(k-1):
            #print(temp.value, end=' ')
            temp = temp.next
        curr = temp.prev
        curr.next = new_node
        new_node.next = temp
        new_node.prev = curr
        self.length += 1

    def delete_at_beginning(self):
        temp = self.head
        before = None
        temp.prev = before
        after = temp.next
        if temp is None:
            return None
        temp.next = before
        temp.prev = before
        self.head = after
        self.length -= 1
        return self.head

    def del_end(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1

        return temp
    def get(self, index):
        if self.length == 0 or index > self.length:
            return None
        temp = self.head
        if self.length == 1:
            return temp

        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp.value
    def remove(self, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before

        return temp
    def set(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False

if __name__ == '__main__':
    new_list = DoublyLinkedList(5)
    new_list.append(6)
    new_list.append(7)
    new_list.append(8)
    new_list.append(9)
    new_list.append(10)
    new_list.append(11)
    new_list.insert(4)
    new_list.insert_at_specific(3, 4)
    new_list.forward_traversal()
    print()
    #print(new_list.get(1))
    new_list.remove(1)
    #new_list.delete_at_beginning()
    #new_list.del_end()
    #new_list.forward_traversal()
    #print()
    new_list.backward_traversal()
