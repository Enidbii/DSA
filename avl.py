#!/usr/bin/python3 env
""" AVL trees """

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        """
        insert a node to a tree
        :param value: value to be inserted
        :return: tree
        """
        if not node:
            return Node(value)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
                node.left.parent = node #sets parent
                self._inspect_insertion(node.left_child)
            else:
                node.left = self.__insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                node.right.parent = node #set parent
            else:
                node.right = self.__insert(node.right, value)
        else:
            print("Value already in the tree")



    def balance(self, node):
        """
        check if the bst is balanced
        :return: height difference
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)


    def height(self, node):
        if self.root is not None:
           return self.__height(self.root, 0)
        else:
            return 0
    def __height(self, node, node_height):
        if node is None:
            return node_height
        left_height = self.__height(node.left, node_height+1)
        right_height = self.__height(node.right, node_height+1)
        return max(left_height, right_height)

    def _left_rotate(self, z):
        sub_root=z.parent
        y=z.right_child
        t2=y.left_child
        y.left_child=z
        z.parent=y
        z.right_child=t2
        if t2 is not None:
            t2.parent=z
        y.parent=sub_root
        if y.parent is None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height=1+max(self.height(z.left_child), self.height(z.right_child))
        y.height=1+max(self.height(y.left_child), self.height(y.right_child))


    def _right_rotate(self, z):
            """
            rotate the nodes to the left
            :param y: node to rotate to the right
            :return:
            """
            sub_root = z.parent
            y = z.left_child
            t3 = y.right_child
            y.right_child = z
            z.parent = y
            z.left_child = t3
            if t3 is not None:
                t3.parent = z
            y.parent = sub_root
            if y.parent is None:
                self.root = y
            else:
                if y.parent.left_child == z:
                    y.parent.left_child = y
                else:
                    y.parent.right_child = y
            z.height = 1 + max(self.height(z.left_child), self.height(z.right_child))
            y.height = 1 + max(self.height(y.left_child), self.height(y.right_child))

    def _inspect_insertion(self, node, path=[]):
        if node.parent is None:
            return
        path = [node] + path

        left_height = self.height(node.parent.left)
        right_height = self.height(node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [node.parent] + path
            self._balance_node(path[0], path[1], path[2])
            return

        new_height = 1 + node.height
        if new_height > node.parent.height:
            node.parent.height = new_height

        self._inspect_insertion(node.parent, path)

    def _inspect_deletion(self, cur_node):
        if cur_node == None: return

        left_height = self.height(cur_node.left_child)
        right_height = self.height(cur_node.right_child)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_deletion(cur_node.parent)

    def _balance_node(self, z, y, x):
        if y==z.left and x==y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)





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
avl_tree.insert(30)
avl_tree.insert(40)
print(avl_tree.in_order_traversal())
