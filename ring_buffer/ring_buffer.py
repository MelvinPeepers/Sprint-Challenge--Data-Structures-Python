from doubly_linked_list import DoublyLinkedList

"""
Seems a Ring Buffer is also known as a Circular buffer, and is a type of queue (FIFO)

https://medium.com/better-programming/now-buffering-7a7d384faab5
"A circular buffer stores data in a fixed-size array. So once the size is set and the buffer is full, the oldest item in the buffer will be pushed out if more data is added."

My first pass pesudocode
Initialize
So if empty, add element
If not empty, check if full
	if not full, add element at head
	if full, add element at head, delete tail

"""


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == 0:  # if self.storage is empty
            self.storage.add_to_head(item)  # add item to head
            self.current = self.storage.head  # self.current stores self.storage.head

        elif len(self.storage) < self.capacity:  # else if storage is less the capacity
            self.storage.add_to_tail(item)  # add to tail
            self.current = self.storage.head

        elif len(self.storage) == self.capacity:  # else if storage is at capacity
            self.current.value = item
            self.current = self.current.next

        else:
            self.current.value = item
            self.current = self.storage.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents


buffer = RingBuffer(3)

# buffer.get()   # should return []
# tested and works!

# buffer.append('a')
# buffer.append('b')
# buffer.get()  # should return ['a', 'b']
# Tested and works!

buffer.append('a')
buffer.append('b')
buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']
# tested and works!


# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')
# buffer.get()   # should return ['d', 'b', 'c']
# tested and works!


buffer.append('e')
buffer.append('f')
buffer.get()   # should return ['d', 'e', 'f']
# tested and works!

print(buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
