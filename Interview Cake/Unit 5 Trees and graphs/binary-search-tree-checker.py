# Write a function to check that a binary tree ↴ is a valid binary search tree

class BinaryTreeNode(object):
    
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_binary_search_tree(root): 
    # Start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # Depth-first traversal
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # If this node is invalid, we return false right away
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.left:
            # This node must be less than the current node
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:
            # This node must be greater than the current node
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    # If none of the nodes were invalid, return true
    # (at this point we have checked all nodes)
    return True

def recursive_is_binary_search_tree(root,
                          lower_bound=-float('inf'),
                          upper_bound=float('inf')):
    if not root:
        return True

    if (root.value >= upper_bound or root.value <= lower_bound):
        return False

    return (recursive_is_binary_search_tree(root.left, lower_bound, root.value)
            and recursive_is_binary_search_tree(root.right, root.value, upper_bound))

# O(n) time and O(n) space

'''
Greedy -> maximum and minimums and divide and conquer -> subtrees are correct
'''