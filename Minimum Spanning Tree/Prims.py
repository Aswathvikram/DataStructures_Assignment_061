import numpy as np
import matplotlib.pyplot as plt

# Function to find the vertex with the minimum key value from the set of vertices not yet included in MST
def min_key(key, mst_set):
    min_value = float('inf')
    min_index = -1
    for v in range(V):
        if key[v] < min_value and not mst_set[v]:
            min_value = key[v]
            min_index = v
    return min_index

# Function to construct MST using Prim's algorithm
def prim_mst(graph):
    key = [float('inf')] * V
    parent = [-1] * V  # Array to store constructed MST
    key[0] = 0  # Start from the first vertex
    mst_set = [False] * V

    for _ in range(V - 1):
        u = min_key(key, mst_set)
        mst_set[u] = True
        
        for v in range(V):
            if graph[u][v] and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent

# Number of vertices in the graph
V = 5

# Define the adjacency matrix for the graph
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Get the parent array for the MST
parent = prim_mst(graph)

# Automatically generate node positions for a simple layout
node_positions = {i: (np.cos(2 * np.pi * i / V), np.sin(2 * np.pi * i / V)) for i in range(V)}

# Function to plot the original graph with weights
def plot_original_graph(graph):
    fig, ax = plt.subplots()

    # Plot all edges with weights
    for i in range(V):
        for j in range(i + 1, V):
            if graph[i][j] != 0:
                x_values = [node_positions[i][0], node_positions[j][0]]
                y_values = [node_positions[i][1], node_positions[j][1]]
                ax.plot(x_values, y_values, 'gray', linewidth=1)  # Solid line
                # Display weight at the midpoint of each edge
                mid_x = (x_values[0] + x_values[1]) / 2
                mid_y = (y_values[0] + y_values[1]) / 2
                ax.text(mid_x, mid_y, str(graph[i][j]), color="blue", fontsize=10)

    # Plot nodes as circles with numbers inside
    for node, (x, y) in node_positions.items():
        circle = plt.Circle((x, y), 0.1, color='lightblue', ec='black', zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, str(node), ha='center', va='center', fontsize=12, color='black')

    # Show the graph
    ax.set_title("Original Graph with Edge Weights")
    plt.axis("off")
    plt.show()

# Function to plot the MST with weights
def plot_mst(graph, parent):
    fig, ax = plt.subplots()

    # Plot MST edges with weights
    for i in range(1, V):
        u = parent[i]
        x_values = [node_positions[u][0], node_positions[i][0]]
        y_values = [node_positions[u][1], node_positions[i][1]]
        ax.plot(x_values, y_values, 'blue', linewidth=2)  # MST edges in blue
        # Display weight at the midpoint of each edge
        mid_x = (x_values[0] + x_values[1]) / 2
        mid_y = (y_values[0] + y_values[1]) / 2
        ax.text(mid_x, mid_y, str(graph[u][i]), color="black", fontsize=10)

    # Plot nodes as circles with numbers inside
    for node, (x, y) in node_positions.items():
        circle = plt.Circle((x, y), 0.1, color='lightblue', ec='black', zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, str(node), ha='center', va='center', fontsize=12, color='black')

    # Show the MST
    ax.set_title("Prim's Algorithm - Minimum Spanning Tree (MST) with Edge Weights")
    plt.axis("off")
    plt.show()

# Plot the original graph and the MST
plot_original_graph(graph)
plot_mst(graph, parent)

