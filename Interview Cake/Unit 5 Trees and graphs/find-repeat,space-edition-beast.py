# Find a duplicate, Space Edition™ BEAST MODE

'''
Find the duplicate in list of integers with:
1. the integers are in the range 1..n
2. the list has a length of n+1

Do this in O(N) time and O(1) space
'''

'''
Imagine each item in the list as a node in a linked list. In any linked list, ↴ each node has a value and a "next" pointer. In this case:

The value is the integer from the list.
The "next" pointer points to the value-eth node in the list (numbered starting from 1). For example, if our value was 3, the "next" node would be the third node.
'''

'''
If two nodes have the same value, their next pointers will point to the same node!
'''

'''
the last node never has any incoming pointers since list has a length n + 1 
and all the values are nn or less, 
there can never be a pointer to the last position 
(can treat the last position as the head of the linked list)

there’s never an end to our list since no pointer points to None (must have a loop)
'''

'''
The first node in the cycle always has at least two incoming pointers!
The pattern is a few nodes then a cycle since it has no None end
'''

'''
We know the position of a node with multiple incoming pointers is a duplicate in our list because the nodes that pointed to it must have the same value.
We find a node with multiple incoming pointers by finding the first node in a cycle.
We find the first node in a cycle by finding the length of the cycle and advancing two pointers: one starting at the head of the linked list, and the other starting ahead as many steps as there are steps in the cycle. The pointers will meet at the first node in the cycle.
We find the length of a cycle by remembering a position inside the cycle and counting the number of steps it takes to get back to that position.
We get inside a cycle by starting at the head and walking nn steps. We know the head of the list is at position n + 1n+1
'''

def find_duplicate(int_list):
    n = len(int_list) - 1

    # STEP 1: GET INSIDE A CYCLE
    # Start at position n+1 and walk n steps to
    # find a position guaranteed to be in a cycle
    position_in_cycle = n + 1
    for _ in range(n):
        position_in_cycle = int_list[position_in_cycle - 1]
        # we subtract 1 from the current position to step ahead:
        # the 2nd *position* in a list is *index* 1

    # STEP 2: FIND THE LENGTH OF THE CYCLE
    # Find the length of the cycle by remembering a position in the cycle
    # and counting the steps it takes to get back to that position
    remembered_position_in_cycle = position_in_cycle
    current_position_in_cycle = int_list[position_in_cycle - 1]  # 1 step ahead
    cycle_step_count = 1

    while current_position_in_cycle != remembered_position_in_cycle:
        current_position_in_cycle = int_list[current_position_in_cycle - 1]
        cycle_step_count += 1

    # STEP 3: FIND THE FIRST NODE OF THE CYCLE
    # Start two pointers
    #   (1) at position n+1
    #   (2) ahead of position n+1 as many steps as the cycle's length
    pointer_start = n + 1
    pointer_ahead = n + 1
    for _ in range(cycle_step_count):
        pointer_ahead = int_list[pointer_ahead - 1]

    # Advance until the pointers are in the same position
    # which is the first node in the cycle
    while pointer_start != pointer_ahead:
        pointer_start = int_list[pointer_start - 1]
        pointer_ahead = int_list[pointer_ahead - 1]

    # Since there are multiple values pointing to the first node
    # in the cycle, its position is a duplicate in our list
    return pointer_start

# O(n) time and O(1) space
