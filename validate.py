
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.root = None
    def insert(self, value):
        """
        inserts tp the tree
        parameter: value to be inserted
        """
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.val == temp.val:
                return  False
            if new_node.val < temp.val:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def isvalidbst(self):
        """
        :type root: TreeNode
        :rtype: bool
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
                stack2.append(temp.val)
                temp = temp.right
            else:
                break

        if len(stack2) == 0:
            return False
        elif len(stack2) == 1:
            return True
        elif len(stack2) > 1:
            result = []
            i = 0
            while i < len(stack2) - 1:
                j = i + 1
                if stack2[i] < stack2[j]:
                    result.append((stack2[i], stack2[j]))
                i += 1
                #return True
            print(result)
            #return False

my_tree = Solution()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.isvalidbst()

