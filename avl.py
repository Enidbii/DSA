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
        while temp:
            if self.balance(temp) is True:
                return
            else:
                if temp.left.right == new_node:
                    if (self.height(temp) == 2) or self.height(temp) == -2:
                        self.left_right_rotation(temp)
                if temp.right.left == new_node:
                    if self.height(temp) == 2 or self.height(temp) == -2:
                        self.right_left_rotation(temp)
                if temp.left.left == new_node:
                    if self.height(temp) == 2 or self.height(temp) == -2:
                        self.left_rotate(temp)
                if temp.right.right == new_node:
                    if self.height(temp) == 2 or self.height(temp) == -2:
                        self.right_rotate(temp)

    def balance(self, node):
        """
        check if the bst is balanced
        :return: height difference
        """
        if (self.height(node.left) - self.height(node.right)) <= 1:
            return True
        else:
            return False


    def height(self, node):
        """
        find the height of a given node
        :param node: node from where we are getting height
        :return: height
        """
        return node.height

    def left_rotate(self, y):
        """
        rotate to the right
        :param y: node to rotate from
        :return: upadated root
        """
        #y is the first unbalanced node
        x = y.left
        z = x.left

        x.left = z
        x.right = y

        x.height = max(self.height(x.left), self.height(y.right))

        return x


    def right_rotate(self, x):
        """
        rotate the nodes to the left
        :param x: node to rotate to the right
        :return:
        """
        y = x.right
        z = y.right

        y.left = x
        y.right = z

        y.height = max(self.height(y.left), self.height(y.right))
        return y

    def left_right_rotation(self, y):
        x = y.left
        z = x.right

        y.left = z
        z.right = x

        self.left_rotate(y)

    def right_left_rotation(self, x):
        y = x.right
        z = y.left

        x.right = z
        z.left = y

        self.right_rotate(x)
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

avl_tree = AVL()
avl_tree.insert(23)
avl_tree.insert(25)
avl_tree.insert(28)
avl_tree.insert(29)
avl_tree.dfs()
