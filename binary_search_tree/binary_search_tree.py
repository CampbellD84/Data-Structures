from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('./queue_and_stack')


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
        # set current node to self
        current_val = self
        # iterate through right nodes
        while current_val.right:
            # set current value to current right node value
            current_val = current_val.right

        return current_val.value

        # Recursive
        # if self.right is None:
        # return self. value
        # else:
        # return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)

        # left side recursive
        if self.left:
            self.left.for_each(cb)

        # right side recursive
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # L, R, Root

        # base case:
        # node is None | node has no child nodes
        if node is None:
            return
        # recursive case
        # go left (as far as possible)
        self.in_order_print(node.left)
        print(node.value)
        # go right (as far as possible)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # set up a QUEUE [nodes to backtrack to]
        bft_q = Queue()
        # init with 'node'
        bft_q.enqueue(node)

        # while queue is NOT empty
        while bft_q.len() != 0:
            # dequeue node
            curr_node = bft_q.dequeue()
            # print node.value
            print(curr_node.value)
            # enqueue node.left if exists, node.right if exists
            if curr_node.left:
                bft_q.enqueue(curr_node.left)
            if curr_node.right:
                bft_q.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create a STACK [nodes we need to backtrack to]
        dft_s = Stack()
        # init with 'node'
        dft_s.push(node)

        # while stack NOT empty
        while dft_s.len() != 0:
            # pop node from stack
            curr_node = dft_s.pop()
            # print node.value
            print(curr_node.value)
            # push node.left if exists, node.right if exists
            if curr_node.left:
                dft_s.push(curr_node.left)
            if curr_node.right:
                dft_s.push(curr_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
