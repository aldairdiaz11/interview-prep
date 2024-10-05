class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left, self.right = None, None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if self.value == value:
            return self
        elif self.left and self.value > value:
            return self.left.get_node_by_value(value)
        elif self.right and self.value <= value:
            return self.right.get_node_by_value(value)
        else:
            return

    def depht_first_traversal(self):
        if self.left:
            self.left.depht_first_traversal()
        print(f"Depth: {self.depth}, Value: {self.value}")
        if self.right:
            self.right.depht_first_traversal()


if __name__ == '__main__':
    # Tests
    root = BinarySearchTree(15)
    root.insert(50)
    root.insert(125)
    root.insert(75)
    root.insert(25)

    print(root.get_node_by_value(125).value)
    print(root.get_node_by_value(10))  # returns None

    root.depht_first_traversal()
