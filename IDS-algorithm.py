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

    return None


def IDS(graph,start,goal,maxLimit):
    for limit in range(maxLimit+1):
        print("Trying limit : ",limit)
        path = DLS(graph,start,goal,limit)
        if path:
            return path

    return None



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

path = IDS(Graph,'A','I',5)

if path:
    print(path)
else:
    print("Path not found")
