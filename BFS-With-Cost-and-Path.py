from collections import deque
import heapq

def bfsWithCostAndGoal(graph, root, goal):
    queue = [(0, root, [root])] 
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, w in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + w, neighbor, path + [neighbor]))


Graph = {
    'A': [('B',2),('C',3)],
    'B': [('D',5),('E',1)],
    'C': [('F',4)],
    'D': [('H',2)],
    'E': [('G',7)],
    'F': [('G',9)],
    'G': [('I',2)],
    'H': [('I',6)],
}

cost, path = bfsWithCostAndGoal(Graph,'A','I')

if path:
    print("Path:", path)
    print("Cost:", cost)
else:
    print("Path Not Found")
