import tkinter as tk
from tkinter import messagebox
import heapq

# Dijkstra's Algorithm
def dijkstra(graph, start, end):
    # Priority queue to store (distance, node)
    queue = [(0, start)]
    distances = {start: 0}
    previous_nodes = {start: None}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_node == end:
            # Reconstruct the shortest path
            path = []
            while previous_nodes[current_node] is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start)
            path.reverse()
            return path, distances[end]
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return None, float('inf')

# Graph Representation (Adjacency List)
graph = {
    'A': [('B', 5), ('C', 10)],
    'B': [('A', 5), ('C', 2), ('D', 3)],
    'C': [('A', 10), ('B', 2), ('E', 7)],
    'D': [('B', 3), ('E', 1)],
    'E': [('C', 7), ('D', 1)]
}

