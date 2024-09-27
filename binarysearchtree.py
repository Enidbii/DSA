#!/usr/bin/python3 env
from inspect import stack


class Node:
    """
    creates a node
    value: value in the node
    """
    def __init__(self, value):
        """ initialises the node """
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        inserts tp the tree
        parameter: value to be inserted
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return  False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    def min_value(self, current_node):
        """
        :param current_node:
        :return: min_value
        """
        if self.root is None:
            return False
        temp = self.root
        if current_node == temp:
            while temp.left is not None:
                temp = temp.left
            return temp.value
        elif current_node is not temp:
            while temp:
                if current_node.value < temp.value:
                    temp = temp.left
                    if temp.left is None:
                        return temp.value
                else:
                    temp = temp.right
                    if temp.left is None:
                        return temp.value

    def in_order_traversal(self):
        """
        :return: A list
        """
        stack = []
        stack2 = []
        temp = self.root
        while True:
            while temp is not None:
                stack.append(temp)
                temp = temp.left
            if stack:
                temp = stack.pop()
                stack2.append(temp.value)
                temp = temp.right
            else:
                break
        return stack2

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

    def post_order_traversal(self):
        stack1 = []
        stack2 = []
        temp = self.root
        stack1.append(temp)
        while stack1:
            popped_node = stack1.pop()
            stack2.append(popped_node)
            if popped_node.left is not None:
                stack1.append(popped_node.left)
            if popped_node.right is not None:
                stack1.append(popped_node.right)
        while stack2:
            node = stack2.pop()
            print(node.value, end=" ")

    def bfs(self):
        queue = []
        temp = self.root

        queue.append(temp)
        while queue:
            popped_node = queue.pop(0)
            print(popped_node.value, end=' ')
            if popped_node.left is not None:
                queue.append(popped_node.left)
            if popped_node.right is not None:
                queue.append(popped_node.right)

    def dfs(self):
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
        return

    def kth_smallest(self, k):
        """
        finds the kth smallest value using inorder traversal
        """
        count = 1
        stack = []
        temp = self.root
        while True:
            while temp is not None:
                stack.append(temp)
                temp = temp.left
            if stack:
                temp = stack.pop()
                if count == k:
                    return temp.value
                temp = temp.right
                count += 1
            else:
                break

    def is_valid_bst(self):
        results_in_order = self.in_order_traversal()
        print(results_in_order)
        if results_in_order is None:
            return False
        if len(results_in_order) == 1:
            return True
        for i in range(1, len(results_in_order)):
            if results_in_order[i] <= results_in_order[i - 1]:
                return False
        return True
    def height(self, node):
        """
        find the height of a given node
        :param node:
        :return: height
        """
        return node.height


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
# my_tree.insert(29)
# my_tree.insert(37)
# my_tree.insert(40)
my_tree.insert(82)

print("Inorder traversal -->")
my_tree.in_order_traversal()
print()
print("Pre-order-traversal -->")
my_tree.pre_order_traversal()
print()
print("Post order traversal -->")
my_tree.post_order_traversal()
print()
print("Breadth First Search -->")
my_tree.bfs()
print()
print("Depth First Search -->")
my_tree.dfs()
print()
print(my_tree.kth_smallest(1))
print(my_tree.kth_smallest(3))
print(my_tree.kth_smallest(6))
print()

print("BST is valid:")
print(my_tree.is_valid_bst())

print(my_tree.height(my_tree.root.right.left))