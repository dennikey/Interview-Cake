# You have a singly-linked list and want to check if it contains a cycle.

'''
Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.
'''

class LinkedListNode(object):
    
    def __init__(self, value):
        self.value = value
        self.next  = None

'''
Using a set, we could store all the nodes we’ve seen so far. 
but that would be O(n) space
'''

def contains_cycle(first_node):
    # Start both runners at the beginning
    slow_runner = first_node
    fast_runner = first_node

    # Until we hit the end of the list
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        # Case: fast_runner is about to "lap" slow_runner
        if fast_runner is slow_runner:
            return True

    # Case: fast_runner hit the end of the list
    return False

# O(n) time and O(1) space

# Proof by contradiction that fast runner will never skip over slow runner since 
# after the skipping step, fast_runner will be 1 node ahead of slow_runner since speed differs by 1
# before the skipping step, fast_runner will be 2 nodes back and slow_runner will be 1 node back -> started from same node