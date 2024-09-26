#!/usr/bin/python3 env
""" AVL trees """

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        insert a node to a tree
        :param value: value to be inserted
        :return: tree
        """
        new_node = Node(value)
        if self.root is None:
            self.root = Node(value)

        temp = self.root
        while temp:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right
    def balance(self, node):
        """
        check if the bst is balanced
        :return: height difference
        """
        if not node:
            return 0
        return self.height(node.left - node.right)

    def height(self, node):
        """
        find the height of a given node
        :param node:
        :return: height
        """
        return node.height

    def right_rotate(self, y):
        """
        rotate to the right
        :param y:
        :return:
        """
        x = y.left
        z = x.right

        z.left = x
        z.right = y



    def left_rotate(self, x):
        """
        rotate the nodes to the left
        :param x:
        :return:
        """