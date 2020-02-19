from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return

        # BST Empty
        elif self.value is None:
            self.value = BinarySearchTree(value)
        # Insert into Right subtree
        elif value >= self.value:
            # TBC
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # Insert into Left subtree
        else:
            # TBC
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base Cases:
        # 1) target found
        if self.value == target:
            return True

        contained_in_subtree = False
        # if target is less than current val, move left in BST
        if target < self.value:
            # if target != left, False
            if not self.left:
                return False
            else:
                contained_in_subtree = self.left.contains(target)
        # else target is greater than current val, move right in BST
        else:
            # if target != right, False
            if not self.right:
                return False
            else:
                contained_in_subtree = self.right.contains(target)

        return contained_in_subtree

    # Return the maximum value found in the tree

    def get_max(self):
        # right as far as you can go
        if not self:
            return None

        current_val = self
        while current_val.right:
            current_val = current_val.right

        return current_val.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # 1) Base case:
        # Left = None and Right = None

        # 2) Recursive case:
        # go left AND right
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
