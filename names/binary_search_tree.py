class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None  # either None or Nodes # BinarySearchTrees (branches)
        # either None or Nodes # BinarySearchTrees (branches)
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the current node
        if value < self.value:
            # if smaller, go left. if we reach a left, what should we do?
            if self.left is not None:  # if there's value on the left and it's not None
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

            # if bigger, go right
        else:
            if self.right is not None:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
            # if no node to go to, (either left or right)
            # make the new node at that spot

            # Return True if the tree contains the value
            # False if it does not

    def contains(self, target):
        # compare value to the current node value
        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
