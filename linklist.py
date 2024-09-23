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

    def get_sublinklist(self, left, right):
        if left == right:
            return None

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(left - 1):
            start = prev.next

        curr = start
        for _ in range(right - left):
            curr = curr.next
        rest = curr.next
        curr.next = None
        prev.next = rest

        return start
        # val = None
        # temp = self.head
        # after = temp.next
        # self.head = self.tail
        # self.tail = temp
        # while start:
        #     temp.next = val
        #     val = temp
        #     temp = after
        # print(temp)




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

    def printlist(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    new_list = LinkedList(1)
    new_list.append(2)
    new_list.append(3)
    new_list.append(4)
    new_list.append(5)
    new_list.printlist()
    print()
    print(new_list.get_sublinklist(2, 4))