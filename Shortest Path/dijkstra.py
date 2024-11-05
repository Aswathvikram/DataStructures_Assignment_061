import heapq

def dijkstra(graph, source):
    # Initialize distances with infinity and set the source distance to 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    
    # Predecessor map to reconstruct the shortest path
    predecessors = {vertex: None for vertex in graph}
    
    # Priority queue to hold vertices to be processed
    priority_queue = [(0, source)]  # (distance, vertex)
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Skip processing if a shorter path has already been found
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, predecessors

def reconstruct_path(predecessors, source, destination):
    path = []
    current_vertex = destination
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = predecessors[current_vertex]
    path.reverse()  # Reverse the path to get the correct order
    return path

# Example usage
if __name__ == "__main__":
    # Graph representation as an adjacency list
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    source_vertex = 'A'
    distances, predecessors = dijkstra(graph, source_vertex)
    
    print(f"Distances from source vertex {source_vertex}:", distances)
    
    # Display shortest paths to each vertex
    for vertex in graph:
        if vertex != source_vertex:
            path = reconstruct_path(predecessors, source_vertex, vertex)
            print(f"Shortest path from {source_vertex} to {vertex}: {' -> '.join(path)} with distance {distances[vertex]}")
