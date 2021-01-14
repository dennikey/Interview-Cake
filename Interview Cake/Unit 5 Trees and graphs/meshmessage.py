# You wrote a trendy new messaging app, MeshMessage, to get around flaky cell phone coverage.

'''
Given information about active users on the network, 
find the shortest route for a message from one user 
(the sender) to another (the recipient). Return a 
list of users that make up this route.

network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott'],
    ...
}

['Jayden', 'Amelia', 'Adam']
'''

'''
The input list is an adjacency list that is undirected (msgs go both ways)
and unweighted (no cost)
'''

'''
Since we want the shortest path, BFS is the way to go 
(BFS and DFS eventually find a path if one exists - BFS always finds shortest while DFS usually uses less space)
'''

'''
The reconstruct path will automatically get the shortest path/just need to reconstruct it
{'Min'     : None,
 'Jayden'  : 'Min',
 'Ren'     : 'Jayden',
 'Amelia'  : 'Jayden',
 'Adam'    : 'Amelia',
 'Miguel'  : 'Amelia',
 'William' : 'Min'}
'''

'''
Two edge cases are sender/receipient aren't in graph and there doesn't exist a route
'''

'''
1. During BFS, keep track of how we reached each node
2. After BFS, use dictionary to backtrack from recipient to sender
'''

from collections import deque

def reconstruct_path(previous_nodes, start_node, end_node):
    reversed_shortest_path = []

    # Start from the end of the path and work backwards
    current_node = end_node
    while current_node:
        reversed_shortest_path.append(current_node)
        current_node = previous_nodes[current_node]

    # Reverse our path to get the right order
    reversed_shortest_path.reverse()  # flip it around, in place
    return reversed_shortest_path  # no longer reversed


def bfs_get_path(graph, start_node, end_node):
    if start_node not in graph:
        raise Exception('Start node not in graph')
    if end_node not in graph:
        raise Exception('End node not in graph')

    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    # Keep track of how we got to each node
    # We'll use this to reconstruct the shortest path at the end
    # We'll ALSO use this to keep track of which nodes we've
    # already visited
    how_we_reached_nodes = {start_node: None}

    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()

        # Stop when we reach the end node
        if current_node == end_node:
            return reconstruct_path(how_we_reached_nodes, start_node, end_node)

        for neighbor in graph[current_node]:
            if neighbor not in how_we_reached_nodes:
                nodes_to_visit.append(neighbor)
                how_we_reached_nodes[neighbor] = current_node

    # If we get here, then we never found the end node
    # so there's NO path from start_node to end_node
    return None

'''
O(N+M) for BFS since O(N) is going through every node in graph and O(M) is look at the current node's neighbors
BFS and DFS are common enough to state as O(N+M)
O(N) space 
'''

'''
Use backtracking to assemble the path
1. Figuring out what additional information we need to store in order to rebuild our path at the end (how_we_reached_nodes, in this case).
2. Figuring out how to reconstruct the path from that information.
'''

