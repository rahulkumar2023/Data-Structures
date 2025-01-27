"""
This program creates a comparison between Breadth-First Search (BFS) and Depth-First Search (DFS) and generates randomly connected graphs and trees.
"""

import random

# Generate a random graph
def generate_graph(n, additional_edges=0):
    """
    Generates a random undirected graph with n nodes.
    - Ensures the graph is connected by linking each node to at least one previous node.
    - Adds additional random edges to increase complexity.
    - Returns an adjacency list representation of the graph.
    """
    adj_list = {i: set() for i in range(n)}  # Initialize adjacency list

    # Ensure connectivity by linking each node to at least one previous node
    for i in range(1, n):
        j = random.randint(0, i-1)  # Randomly select a previous node
        adj_list[i].add(j)  # Add the edge
        adj_list[j].add(i)  # Add the reverse edge (undirected graph)

    # Add additional random edges
    while additional_edges > 0:
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)

        # Add an edge if u and v are distinct and not already connected
        if u != v and v not in adj_list[u]:
            adj_list[u].add(v)
            adj_list[v].add(u)
            additional_edges -= 1

    return adj_list

# Calculate the diameter of a graph using BFS
def bfs_diameter(adj_list):
    """
    Calculates the diameter of a graph using BFS.
    - Performs two BFS traversals:
        1. To find the farthest node from an arbitrary starting node.
        2. To find the farthest distance from that node, which is the diameter.
    - Returns the diameter (longest shortest path between any two nodes).
    """
    def bfs(start):
        """
        Helper function to perform BFS from a starting node.
        - Returns the farthest node and its distance from the start.
        """
        queue = [start]
        distances = {start: 0}  # Track distances from the start node
        last_node = start  # Initialize the last visited node

        while queue:
            current = queue.pop(0)  # Dequeue the current node

            for neighbor in adj_list[current]:  # Visit all neighbors
                if neighbor not in distances:  # Check if the neighbor is unvisited
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)  # Enqueue the neighbor
                    last_node = neighbor  # Update the last node visited

        return last_node, distances[last_node]  # Return the farthest node and its distance

    farthest_node = next(iter(adj_list))  # Start BFS from any node
    _, dist = bfs(farthest_node)  # First BFS to find the farthest node
    farthest_node, _ = bfs(farthest_node)  # Second BFS to find the diameter
    _, diameter = bfs(farthest_node)  # Third BFS to confirm the diameter

    return diameter

# Calculate the sum of visited edges using DFS
def sum_edges_dfs(start, adj_list):
    """
    Calculates the sum of visited edges using DFS.
    - Traverses the graph starting from the given node.
    - Counts edges as they are visited.
    - Returns the total edge count.
    """
    visited = set()  # Track visited nodes
    stack = [start]  # Initialize stack with the starting node
    edge_sum = 0  # Initialize the edge sum

    while stack:
        node = stack.pop()  # Pop the top node

        if node not in visited:
            visited.add(node)  # Mark the node as visited

            for neighbor in adj_list[node]:  # Explore neighbors
                if neighbor not in visited:
                    edge_sum += 1  # Increment edge count
                    stack.append(neighbor)  # Push neighbor onto the stack

    return edge_sum

# Calculate the sum of visited edges using BFS
def sum_edges_bfs(start, adj_list):
    """
    Calculates the sum of visited edges using BFS.
    - Traverses the graph starting from the given node.
    - Counts edges as they are visited.
    - Returns the total edge count.
    """
    visited = set()  # Track visited nodes
    queue = [start]  # Initialize queue with the starting node
    edge_sum = 0  # Initialize the edge sum

    while queue:
        node = queue.pop(0)  # Dequeue the front node

        if node not in visited:
            visited.add(node)  # Mark the node as visited

            for neighbor in adj_list[node]:  # Explore neighbors
                if neighbor not in visited:
                    edge_sum += 1  # Increment edge count
                    queue.append(neighbor)  # Enqueue neighbor

    return edge_sum

# Run the experiment
def run_experiment():
    """
    Runs the experiment to compare BFS and DFS:
    - Part 1: Generates a tree and a graph, calculates their diameters.
    - Part 2: Calculates average diameters for different sizes.
    - Part 3: Compares edge visitation counts between BFS and DFS.
    """
    # Part 1: Demonstration with n = 8
    n = 8
    tree_graph = generate_graph(n)  # Generate a tree with 8 nodes
    print("Part 1: Tree Adjacency List for n = 8:", tree_graph)
    print("Diameter of the tree:", bfs_diameter(tree_graph))

    graph_with_edges = generate_graph(n, 8)  # Generate a graph with additional edges
    print("Graph with additional edges:", graph_with_edges)
    print("Diameter of the graph:", bfs_diameter(graph_with_edges))

    # Part 2: Diameter Experiment for different sizes
    ns = [20, 40, 60, 80, 100]  # Graph sizes for the experiment
    print("\nPart 2: Diameter Experiments")
    for size in ns:
        avg_diameters = {'tree': [], 'graph': []}

        for _ in range(10):  # Repeat the experiment 10 times for averaging
            tree = generate_graph(size)  # Generate a tree
            avg_diameters['tree'].append(bfs_diameter(tree))
            graph = generate_graph(size, size)  # Generate a graph with additional edges
            avg_diameters['graph'].append(bfs_diameter(graph))

        # Calculate and display the average diameters
        avg_tree_dia = sum(avg_diameters['tree']) / 10
        avg_graph_dia = sum(avg_diameters['graph']) / 10
        print(f"n = {size}, Avg Tree Diameter = {avg_tree_dia:.2f}, Avg Graph Diameter = {avg_graph_dia:.2f}")

    # Part 3: Edge Sum Comparison between DFS and BFS
    print("\nPart 3: DFS vs BFS Comparison")
    for size in ns:
        edge_sums = {'dfs': [], 'bfs': []}

        for _ in range(10):  # Repeat to average results
            graph = generate_graph(size, size)  # Generate a graph
            start_vertex = random.choice(list(graph.keys()))  # Select a random start vertex
            edge_sums['dfs'].append(sum_edges_dfs(start_vertex, graph))
            edge_sums['bfs'].append(sum_edges_bfs(start_vertex, graph))

        # Calculate and display the average edge sums
        avg_dfs = sum(edge_sums['dfs']) / 10
        avg_bfs = sum(edge_sums['bfs']) / 10
        ratio = avg_dfs / avg_bfs if avg_bfs != 0 else float('inf')  # Calculate the ratio
        print(f"n = {size}, Avg DFS Sum = {avg_dfs:.2f}, Avg BFS Sum = {avg_bfs:.2f}, Ratio = {ratio:.2f}")

# Run the experiment
run_experiment()
