from collections import deque
def dfsWithGoalAndPath(graph,root,goal):
    queue = deque([[root]])
    visited = []

    while queue:
        path = queue.pop()
        node = path[-1]

        if node==goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(path+[neighbor])




Graph={
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

path =  dfsWithGoalAndPath(Graph,'A','I')

if  path:
    print(path)
else:
    print("Path Not Found")
