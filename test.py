class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def sublinklist(self, left, right):
        # Initialize dummy node and pointers
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        # Move prev to the node before the `left` position
        for _ in range(left - 1):
            prev = prev.next

        # Initialize pointers for the reversal
        start = prev.next
        then = start.next

        # Reverse the nodes between `left` and `right`
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        # Adjust the head of the list if needed
        if left == 1:
            self.head = prev.next

        print(dummy.next)  # Return the head of the modified list

linkedlist = LinkedList(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.append(6)
linkedlist.sublinklist(2, 4)

