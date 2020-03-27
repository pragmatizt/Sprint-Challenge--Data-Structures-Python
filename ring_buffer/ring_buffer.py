from doubly_linked_list import DoublyLinkedList

"""Ring Buffer: fixed size; no beginning, no end.
2 Elements:
Append: adds elements
Get: returns all of the elements.

The `get` method, which is provided, returns all of the 
elements in the buffer in a list in their given order. It should 
not return any `None`   ## (SO no need to sort)

Question for self: how is this different, how is it the same from LRU?
- To add a dictionary or not?  Instructions don't mention anything about key-value entries.
- Let's assume we don't need to first.  How do we implement it without?
- Why is there a list_buffer_contents?
"""

class RingBuffer:
    def __init__(self, capacity):
        # LIMIT. Not defined above, but max # of nodes we can have
        self.capacity = capacity
        # COUNTER.  Current is same as size from lru project 
        self.current = None
        # LINKS to our DoublyLinkedList - called "storage" from queue project; "order" from lru cache project
        self.storage = DoublyLinkedList()


    """Need to insert new log, and remove old log."""
    def append(self, item):
    # Think: "set" from our LRU cache project
        if len(self.storage) < self.capacity:
            # Add newest item in tail
            self.storage.add_to_tail(item)
            # Set pointer to tail (since buffer not full)
            self.current = self.storage.tail

        else:  # If buffer is at full capacity
            # Have pointer go to oldest (in our case, head)
            if self.current == self.storage.tail:
                self.current = self.storage.head

            else:  # For first time overwriting, need to find next oldest
                # We shift to this next value because it is _now_ the oldest entry
                self.current = self.current.next
            
            # Overwrite the value
            self.current.value = item


    """After insertion and deletion from append,
    We return the list in their given order."""
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # Create a pointer, which starts at head of our LL
        pointer = self.storage.head

        # As long as pointer is not None,
        while pointer is not None:
            # append to [] the node's value
            list_buffer_contents.append(pointer.value)
            # Move to next node -- continue until you reach None
            pointer = pointer.next

        return list_buffer_contents



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
