from collections import deque

def DFS(graph, root):
    queue = deque([root])
    visited = []
    
    while queue:
        node = queue.pop()

        if node not in visited:
            visited.append(node)
            print(node, end=" ") 

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)


Graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B','H'],
    'E': ['B','G'],
    'F': ['C','G'],
    'G': ['E','F','I'],
    'H': ['D','I'],
    'I': ['G','H'],
}

DFS(Graph, 'A')
