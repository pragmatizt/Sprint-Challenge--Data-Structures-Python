"""
So we have to use a recursion, and not a for loop.  
So basically, recursion occurs until it hits the base case, then it stops

Really this problem is one of changing the pointers opposite of each other, no?
"""

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
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        prev = None
        current = self.head
        while current is not None:
            next = current.next  # Node object has no attribute next
            current.next = prev
            prev = current
            current = next
        self.head = prev


"""
From geeks for geeks: https://www.geeksforgeeks.org/reverse-a-linked-list/

    # Function to reverse the linked list 
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

Basically it's about changing links between nodes.

We iterate through the linked list.  
In the loop, we:
- before changing next of current,
- store next node
next = curr-> next
- now change next of current
- this is where reversing happens
curr -> next = prev

Move prev and current one step forward
prev = curr
cur = next
============
BUT THIS IS ITERATIVE.  NEED TO DO IT RECURSIVELY
For recursion, we need to do this:
   1) Divide the list in two parts - first node and 
      rest of the linked list.
   2) Call reverse for the rest of the linked list.
   3) Link rest to first.
   4) Fix head pointer
"""
