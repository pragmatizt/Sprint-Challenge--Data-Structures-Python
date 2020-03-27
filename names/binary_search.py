# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == value:
            pass
        elif value < self.value:
            if self.left:
                return self.left.insert(value)

            else:
                self.left = BinarySearchTree(value)
                return(value, 'Added')
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                return(value, 'Added')

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If our target matches the value, return True, and stop the search
        if target == self.value:
            return True
        # Otherwise, try the left branch
        # If target is left than value
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else: 
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        
        cb(self.value)

        # if right is present
        if self.left:
            self.left.for_each(cb)
        
        # if left is present
        if self.right:
            self.right.for_each(cb)
