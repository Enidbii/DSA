#!/usr/bin/python3 env

#create nodes
#create linked list
#Add nodes to linked lists
#print linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        #head points to john and and next of John opoints to none
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("List is empty")
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next



# Node =>dat, next
#firstNode.data points to John, firstNode.next points to none
if __name__ == "__main__":
    firstNode = Node("John")
    linkedList = LinkedList()
    #linkedList.insert(firstNode)
    secondNode = Node("Ben")
    #linkedList.insert(secondNode)
    thirdNode = Node("Matt")
    #linkedList.insert(thirdNode)
    linkedList.printList()
