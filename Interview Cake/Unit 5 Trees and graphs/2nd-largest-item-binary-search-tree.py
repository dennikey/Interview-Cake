# Write a function to find the 2nd largest element in a binary search tree.

def my_find_largest(root_node):
    last = root_node
    current = root_node.right

    while current.right is not None:
        last = current
        current = current.right
    
    return [last, current]

def my_find_second_largest(root_node):
    if (root_node is None) or (root_node.left is None and root_node.right is None):
        raise ValueError('??')

    ans = my_find_largest(root_node)
    
    if ans[1].left is None: 
        return ans[0].value
    else:
        # need to account for single left
        new_ans = my_find_largest(ans[1].left)
        return new_ans[1].value

'''
def find_largest(root_node):
    if root_node is None:
        raise ValueError('Tree must have at least 1 node')
    if root_node.right is not None:
        return find_largest(root_node.right)
    return root_node.value


def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    # Case: we're currently at largest, and largest has a left subtree,
    # so 2nd largest is largest in said subtree
    if root_node.left and not root_node.right:
        return find_largest(root_node.left)

    # Case: we're at parent of largest, and largest has no left subtree,
    # so 2nd largest must be current node
    if (root_node.right and
            not root_node.right.left and
            not root_node.right.right):
        return root_node.value

    # Otherwise: step right
    return find_second_largest(root_node.right)
'''

def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right

def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if (current.right and
                not current.right.left and
                not current.right.right):
            return current.value

        current = current.right

# O(h) time where h is height of tree and O(1) space

'''
Simplify, solve, and adapt strategy -> start with largest element
Breaking things down into cases -> largest has left subtree vs largest doesn't
'''