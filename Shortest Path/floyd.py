def floyd_warshall(graph):
    # Initialize distance and predecessor matrices
    num_vertices = len(graph)
    distance = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    predecessor = [[None] * num_vertices for _ in range(num_vertices)]

    # Set initial distances and predecessors based on the graph
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                distance[i][j] = 0  # Distance to self is zero
            elif graph[i][j] is not None:
                distance[i][j] = graph[i][j]  # Use edge weight
                predecessor[i][j] = i  # Set predecessor

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    predecessor[i][j] = predecessor[k][j]

    return distance, predecessor

def reconstruct_path(predecessor, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessor[start][current]
    path.reverse()
    return path

# Example usage
if __name__ == "__main__":
    # Graph represented as an adjacency matrix
    # Using the same structure as before with labeled vertices
    labels = ['A', 'B', 'C', 'D']
    graph = [
        [0, 1, 4, None],  # Distances from A
        [1, 0, 2, 5],     # Distances from B
        [4, 2, 0, 1],     # Distances from C
        [None, 5, 1, 0]   # Distances from D
    ]
    
    distance, predecessor = floyd_warshall(graph)

    # Display shortest paths and distances
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j:
                path = reconstruct_path(predecessor, i, j)
                path_labels = ' -> '.join(labels[k] for k in path)  # Convert indices to labels
                print(f"Shortest path from {labels[i]} to {labels[j]}: {path_labels} with distance {distance[i][j]}")
