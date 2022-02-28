
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    # Private helper functions
    def __insert(self, data, root):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self.__insert(data, root.left)
        elif data >= root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                self.__insert(data, root.right)

    # Traversals
    def __preOrder(self, root):
        print (root.data)
        if root.left:
            self.__preOrder(root.left)
        if root.right:
            self.__preOrder(root.right)

    # Wrapper Functions
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.__insert(data, self.root)

    def preOrder(self):
        self.__preOrder(self.root)


t=Tree()
print()
