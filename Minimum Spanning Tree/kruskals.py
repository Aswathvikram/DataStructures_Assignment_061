import numpy as np
import matplotlib.pyplot as plt

class StepByStepKruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    # Add an edge to the graph
    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    # Find function for Union-Find
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # Union function for Union-Find
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Display the original graph with all edges
    def plot_original_graph(self):
        node_positions = self.get_node_positions()
        fig, ax = plt.subplots(figsize=(6, 6))

        # Plot all edges as dashed lines
        for weight, u, v in self.edges:
            x_values = [node_positions[u][0], node_positions[v][0]]
            y_values = [node_positions[u][1], node_positions[v][1]]
            ax.plot(x_values, y_values, 'gray', linestyle='--', linewidth=1)
            # Display weight at the midpoint of each edge
            mid_x = (x_values[0] + x_values[1]) / 2
            mid_y = (y_values[0] + y_values[1]) / 2
            ax.text(mid_x, mid_y, str(weight), color="black", fontsize=8)

        # Plot nodes as circles with labels
        for node, (x, y) in node_positions.items():
            ax.plot(x, y, 'o', color='lightblue', markersize=15, markeredgecolor='black')
            ax.text(x, y, str(node), ha='center', va='center', fontsize=10, color='black')

        ax.set_title("Original Graph with All Edges")
        plt.axis("off")
        plt.show()

    # Kruskal's MST with step-by-step visualization
    def kruskal_mst_steps(self):
        result = []  # Store the MST edges
        self.edges = sorted(self.edges, key=lambda item: item[0])

        parent = list(range(self.V))
        rank = [0] * self.V

        step = 0
        for weight, u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If x and y are in different sets, no cycle is formed
            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)
                step += 1
                self.plot_step(result, step)
                if len(result) == self.V - 1:  # MST complete
                    break

        # Plot final MST
        self.plot_final_mst(result)

    # Generate circular layout for nodes
    def get_node_positions(self):
        angle = 2 * np.pi / self.V
        return {i: (np.cos(i * angle), np.sin(i * angle)) for i in range(self.V)}

    # Plot each step of MST formation
    def plot_step(self, mst_edges, step):
        node_positions = self.get_node_positions()
        fig, ax = plt.subplots(figsize=(6, 6))

        # Plot all edges as dashed lines
        for weight, u, v in self.edges:
            x_values = [node_positions[u][0], node_positions[v][0]]
            y_values = [node_positions[u][1], node_positions[v][1]]
            ax.plot(x_values, y_values, 'gray', linestyle='--', linewidth=1)

        # Plot MST edges added so far as solid lines
        for u, v, weight in mst_edges:
            x_values = [node_positions[u][0], node_positions[v][0]]
            y_values = [node_positions[u][1], node_positions[v][1]]
            ax.plot(x_values, y_values, 'blue', linewidth=2.5)
            # Display weight at the midpoint of each edge
            mid_x = (x_values[0] + x_values[1]) / 2
            mid_y = (y_values[0] + y_values[1]) / 2
            ax.text(mid_x, mid_y, str(weight), color="black", fontsize=8)

        # Plot nodes as circles with labels
        for node, (x, y) in node_positions.items():
            ax.plot(x, y, 'o', color='lightblue', markersize=15, markeredgecolor='black')
            ax.text(x, y, str(node), ha='center', va='center', fontsize=10, color='black')

        ax.set_title(f"Step {step}: Adding Edge to MST")
        plt.axis("off")
        plt.show()

    # Plot the final MST after all steps are complete
    def plot_final_mst(self, mst_edges):
        node_positions = self.get_node_positions()
        fig, ax = plt.subplots(figsize=(6, 6))

        # Plot MST edges as solid lines
        for u, v, weight in mst_edges:
            x_values = [node_positions[u][0], node_positions[v][0]]
            y_values = [node_positions[u][1], node_positions[v][1]]
            ax.plot(x_values, y_values, 'blue', linewidth=2.5)
            # Display weight at the midpoint of each edge
            mid_x = (x_values[0] + x_values[1]) / 2
            mid_y = (y_values[0] + y_values[1]) / 2
            ax.text(mid_x, mid_y, str(weight), color="black", fontsize=8)

        # Plot nodes as circles with labels
        for node, (x, y) in node_positions.items():
            ax.plot(x, y, 'o', color='lightblue', markersize=15, markeredgecolor='black')
            ax.text(x, y, str(node), ha='center', va='center', fontsize=10, color='black')

        ax.set_title("Kruskal's Algorithm - MST")
        plt.axis("off")
        plt.show()

# Example usage with 6 vertices
g = StepByStepKruskal(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 5)
g.add_edge(2, 4, 11)
g.add_edge(3, 4, 2)
g.add_edge(4, 5, 10)
g.add_edge(3, 5, 6)

# Display original graph
g.plot_original_graph()

# Run Kruskal's algorithm with step-by-step visualization
g.kruskal_mst_steps()
