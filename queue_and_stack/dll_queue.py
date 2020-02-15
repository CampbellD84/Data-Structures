from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        # if size of queue is greater than zero
        if self.size > 0:
            # store method call in variable
            dequed_node = self.storage.remove_from_head()
            # decrement size
            self.size -= 1
            return dequed_node
        else:
            return None

    def len(self):
        return self.size
