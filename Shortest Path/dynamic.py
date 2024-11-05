def find_shortest_paths(graph, labels, destination):
    N = len(graph)
    
    # Initialize costs and paths
    J = {label: float('inf') for label in labels}
    Path = {label: [] for label in labels}
    
    J[destination] = 0  # Cost to reach the destination from itself is 0
    Path[destination] = [destination]  # Path to destination is just itself

    # Process vertices
    for _ in range(N - 1):  # Repeat N-1 times
        for i in range(N):  # For each vertex i
            for j in range(N):  # For each vertex j
                if graph[i][j] is not None:  # Check if there's a directed edge
                    # If a shorter path is found
                    if J[labels[i]] > graph[i][j] + J[labels[j]]:
                        J[labels[i]] = graph[i][j] + J[labels[j]]
                        Path[labels[i]] = Path[labels[j]] + [labels[i]]

    return J, Path

# Define the graph and labels
labels = ['A', 'B', 'C', 'D']
graph = [
    [0, 1, 4, None],  # Distances from A
    [1, 0, 2, 5],     # Distances from B
    [4, 2, 0, 1],     # Distances from C
    [None, 5, 1, 0]   # Distances from D
]

destination = 'A'
result_costs, result_paths = find_shortest_paths(graph, labels, destination)

# Formatting the output
for source in labels:
    if source != destination:
        path = ' -> '.join(result_paths[source])  # Create a path string
        print(f"Shortest path from {source} to {destination}: {path} with distance {result_costs[source]}")
