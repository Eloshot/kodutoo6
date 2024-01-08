from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(f"Visited: {start}")
        visited.add(start)

        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}


dfs(graph, list(graph.keys())[0])