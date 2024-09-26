#!/usr/bin/python3
""" UIng recursion in functions of binary search tree"""

class Node:
    """
    creates a node
    value: value in the node
    """
    def __init__(self, value):
        """ initialises the node"""
        self.value = value
        self.left = None
        self.right = None

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

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __r_delete(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left  is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete(current_node.right, sub_tree_min)
        return current_node
    def r_delete(self, value):
        self.__r_delete(self.root, value)



    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.left, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)




my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
print(my_tree.min_value(my_tree.root))
my_tree.r_delete(18)

# print(my_tree.r_contains(20))
# print(my_tree.r_contains(21))

