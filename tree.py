#!/usr/bin/python3 env

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


    def insert(self, data):
        new_node = Node(data)
        temp = self.root
        if self.root is None:
            self.root = new_node
            return
        queue = []
        queue.append(temp)
        while queue:
            popped_node = queue.pop(0)
            if popped_node.left is None:
                popped_node.left = new_node
                return
            elif popped_node.right is None:
                popped_node.right = new_node
                return
            else:
                queue.append(popped_node.left)
                queue.append(popped_node.right)


    def pre_order_traversal(self):
        stack = []
        temp = self.root
        stack.append(temp)
        while stack:
            popped_node = stack.pop()
            print(popped_node.value, end=" ")
            if popped_node.right is not None:
                stack.append(popped_node.right)
            if popped_node.left is not None:
                stack.append(popped_node.left)

    def is_mirror(self):
        if self.root is None:
            return False
        curr1 = Tree()
        curr2 = Tree()
        queue = []

        queue.append(curr1)
        queue.append(curr2)
        if self.root is None:
            return False
        while len(queue):
            curr1 = queue[0]
            queue.pop(0)
            curr2 = queue[0]
            queue.pop(0)
            if curr1.val != curr2.val:
                return False
            if curr1.left and curr2.right:
                queue.append(curr1.left)
                queue.append(curr2.right)
            elif curr1.left or curr2.right:
                return False
            if curr1.left and curr2.right:
                queue.append(curr1.right)
                queue.append(curr2.left)
            elif curr1.left or curr2.right:
                return False
        return True

my_tree = Tree()
my_tree.insert(1)
my_tree.insert(2)
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(4)
my_tree.insert(4)
my_tree.insert(3)
my_tree.pre_order_traversal()
