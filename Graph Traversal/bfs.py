import matplotlib.pyplot as plt
from collections import deque

# Define the graph with weights using an adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Define positions for visualization
positions = {
    'A': (1, 3),
    'B': (0, 2),
    'C': (2, 2),
    'D': (0, 1),
    'E': (1, 1),
    'F': (2, 1)
}

def draw_graph_step(traversal_order, current_node):
    plt.clf()
    plt.title("BFS Traversal Step-by-Step")
    plt.axis('off')

    # Draw edges with weights
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            x_values = [positions[node][0], positions[neighbor][0]]
            y_values = [positions[node][1], positions[neighbor][1]]
            plt.plot(x_values, y_values, 'gray', zorder=1)
            mid_x, mid_y = (x_values[0] + x_values[1]) / 2, (y_values[0] + y_values[1]) / 2
            plt.text(mid_x, mid_y, str(weight), color='blue', fontsize=10)

    # Draw nodes
    for node, (x, y) in positions.items():
        color = 'lightblue' if node not in traversal_order else 'orange'
        if node == current_node:
            color = 'red'
        plt.scatter(x, y, color=color, s=300, zorder=2)
        plt.text(x, y, node, fontsize=12, ha='center', va='center', zorder=3)

    plt.pause(1)
    plt.draw()

def bfs_weighted(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    plt.ion()
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            traversal_order.append(current_node)
            visited.add(current_node)

            draw_graph_step(traversal_order, current_node)

            for neighbor, _ in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    plt.ioff()
    plt.show()
    print("Traversal Order:", traversal_order)

# Run BFS
bfs_weighted(graph, 'A')
