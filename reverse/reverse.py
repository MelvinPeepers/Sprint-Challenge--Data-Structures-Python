class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # TO BE COMPLETED
        # initialize
        prev = None
        current = self.head
        # while loop
        while(current is not None):
          # create a temp to point to next
            next = current.next_node
            # reverse the direction by setting the next point to the prev
            current.next_node = prev
            # set the prev to the next
            prev = current
            # set current to the temp
            current = next
        # update the linked list
        self.head = prev


"""
python3 test_reverse.py --v
test_add_to_head (__main__.LinkedListTests) ... ok
test_contains (__main__.LinkedListTests) ... ok
test_empty_reverse (__main__.LinkedListTests) ... ok
test_longer_reverse (__main__.LinkedListTests) ... ok
test_single_reverse (__main__.LinkedListTests) ... ok

Ran 5 tests in 0.001s
OK
"""
