#!/usr/bin/python3

""" Reverses linked list """
from markdown_it.rules_block import heading


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value, next=None):
        new_node = Node(value) 
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_llist(self):
        #print thelinked list
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def iterable(self):
        temp = self.head
        while temp:
            val = temp.value
            temp = temp.next
            return val

    def Prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.next = temp
        self.length += 1

    def pop_at_end(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
        
    
    def reverse(self):
        #1-->2-->3-->4-->5
        #create a variable to reverse head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        #Now create 2 variables that will iterate
        after = temp.next
        before = None
        #lets iterate over the list to reverse it
        for _ in range(self.length):
            after = temp.next
            temp.next = before #Now temp.next points to  none in the first iteration
            before = temp #before is now temp..self.head in this case
            temp = after # temp now becomes after 




    def get_node(self, index):
        #To get a node we pass in an index
        #We need to loop through the entire length of the list until we land on the index
        temp = self.head
        if index < 0 or index >= self.length: #for index less than 0,and index bigger than the length of the list.
            return None
        for _ in range(index):
            temp = temp.next #loop through the list while assigning next node to temp
            #when it lands on the index given, it goes out of loop and returns temp
        return temp

    def insert_in_middle(self, index, value):
        #if an index passed is 0 or its greater than length of the linked list
        if index < 0 or index > self.length:
            return False
        #Inserting at the beginning is like prepend()
        if index == 0:
            return self.Prepend(value)
        #Inserting at the end is like prepend
        if index == self.length:
            return self.append(value)
        #create a new node to insert
        new_node = Node(value)
        #variable that stores a node that is right before where we'll insert the new node
        temp = self.get_node(index - 1)
        #new_node.next should point to what temp.next has been pointing to
        new_node.next = temp.next
        #Now temp.next points to the new node
        temp.next = new_node
        self.length += 1 #increment new node
        return True
    def set_value(self, index, value):
        pass
    def pop_first(self):
        if self.length == 0:
            return None
        prev = self.head
        after = prev.next
        prev.next = self.head
        self.head = after
        prev.next = None
        return prev
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            pass #yet to create a function
        if index == self.length - 1:
            temp = self.pop_at_end()
            return temp
        return temp
    
    def size(self):
        return self.length
    #get sublist from a given point to another
    def reversebetween(self, left, right):
        if left == right:
            return self.head

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        pos = 1
        while pos < left:
            prev = prev.next
            pos+=1
        curr = prev.next
        while left < right:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            left+=1
        return dummy.next


    def swapnodes(self, k):
        size = 0
        temp = self.head

        while temp is not None:
            size += 1
            temp = temp.next

        l = size - k + 1
        if l == k:
            return self.head
        val_k = 0
        val_l = 0
        temp = self.head
        for i in range(1, size+1):
            if i == k:
                val_k = temp.value
            if i == l:
                val_l = temp.value
            temp = temp.next
        temp = self.head
        for i in range(1, size+1):
            if i == k:
                temp.val = val_l
            if i == l:
                temp.val = val_k
            temp = temp.next
        return self.head
        
if __name__ == "__main__":
    llist = LinkedList(10)
    llist.append(9)
    llist.append(8)
    llist.append(7)
    llist.append(6)
    llist.append(5)
    llist.append(4)
    llist.append(3)
    llist.print_llist()
    print()
    #llist.reverseBetween()
    #print(llist.get_node(1))
    ##print(llist.get_node(x - 2))
    #llist.swapnodes(2)
    #llist.print_llist()
    #llist.reversebetween(2,4)
    llist.swapnodes(2)
    llist.print_llist()
    