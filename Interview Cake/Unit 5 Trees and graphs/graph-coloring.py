# Given an undirected graph with maximum degree, find a graph coloring using at most D+1 colors

class GraphNode:
    
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]

def color_graph(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible for node with loop: %s' %
                            node.label)

        # Get the node's neighbors' colors, as a set so we
        # can check if a color is illegal in constant time
        illegal_colors = set([
            neighbor.color
            for neighbor in node.neighbors
            if neighbor.color
        ])

        # Assign the first legal color
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break

# O(N+M) time where N is the number of nodes and M is the number of edges
'''
- Check if each N node appears in its own neighbors -> O(N)
- Cross each of graph's M edges twice, once for each end -> O(M)
- In the worst case, check one more color than total number of neighbors and then check edge neighbors twice
Thus, O(N+M), but might not look like linear due to inner and outer loops 
'''
# O(D) space where D are the different colors
