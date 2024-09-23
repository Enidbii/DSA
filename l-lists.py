#!/usr/bin/python3 env

class Node:
    def __init__(self, data):
        self.data = data #Assigns data to node
        self.next = None #Initialize the next attribute to null

class LinkedList:
    def __init__(self):
        self.head = None

    #inserting a new node at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data) # creates new node
        new_node.next = self.head #Nxt for new node becomes current head
        self.head = new_node #Head now points to the new node

    def printList(self):
        temp = self.head #Start from the head of the list
        while temp:
            print(temp.data, end=' ') #Print the data in the current node
            temp = temp.next # Move to the next node
        print() #ensures the output is followed by a new line
if __name__ == "__main__":
    llist = LinkedList() #new linked list instance

    llist.insertAtBeginning('Fox')
    llist.insertAtBeginning('Brown')
    llist.insertAtBeginning('quick')
    llist.insertAtBeginning('the')

    #print the list

    llist.printList()


