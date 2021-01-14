# Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.

'''
Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.
'''

'''
Use XOR all the integers in the list. When we XOR with the same ID again, it will cancel out the earlier change
'''

def find_unique_delivery_id(delivery_ids):
    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id

# O(n) time and O(1) space

'''
1. Cancel out matching numbers -> use XOR
2. Want to multiple or divide by 2 -> use left shift and right shift respectively
'''