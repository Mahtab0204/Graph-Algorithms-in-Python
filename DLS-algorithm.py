def DLS(graph,start,goal,limit):
    stack = [(start,[start],0)]
    visited = [start]

    while stack:
        node,path,depth=stack.pop()

        if node==goal:
            return path

        if depth<limit:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append((neighbor,path+[neighbor],depth+1))



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

path = DLS(Graph,'A','I',4)

if path:
    print(path)
else:
    print("Path not found")
