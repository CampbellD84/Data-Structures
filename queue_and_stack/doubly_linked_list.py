"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # create new node
        new_node = ListNode(value)
        # increment length of DLL
        self.length += 1
        # set head/tail to new ListNode if none
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # set the prev/next pointers
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # set value to equal head ListNode value
        value = self.head.value
        # call delete on the tail
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # create new ListNode
        new_node = ListNode(value)
        # increment length of DLL
        self.length += 1
        # if new ListNode is not head and not tail
        # set new ListNode as head and tail if only ListNode in DLL
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            # pointer to new node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # set value to equal tail ListNode value
        value = self.tail.value
        # call delete on the tail
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # if ListNode is head in DLL, return
        if node is self.head:
            return
        # Set value of ListNode
        value = node.value
        # delete ListNode
        self.delete(node)
        # Add ListNode to head of DDL
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # if ListNode is tail in DLL, return
        if node is self.tail:
            return
        # Set value of ListNode
        value = node.value
        # delete ListNode
        self.delete(node)
        # Add ListNode to tail of DDL
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if not self.head and not self.tail:
            return
        # If there is only 1 node in DLL
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = self.length - 1
        # If ListNode is Head
        elif self.head == node:
            self.head = node.next
            self.length = self.length - 1
            node.delete()
        # If ListNode is Tail
        elif self.tail == node:
            self.tail = node.prev
            self.length = self.length - 1
            node.delete()
        else:
            self.length = self.length - 1
            node.delete()
        node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        max_value = None
        temp_var = None

        temp_var = max_value = self.head

        while temp_var != None:
            if temp_var.value > max_value.value:
                max_value = temp_var
            temp_var = temp_var.next

        return max_value.value
