import heapq

def UCS(graph,start,goal):
    pq=[(0,start,[start])]

    while pq:
        cost,node,path = heapq.heappop(pq)

        if node==goal:
            return cost,path

        for neighbor,newCost in graph.get(node,[]):
            heapq.heappush(pq,(cost+newCost,neighbor,path+[neighbor]))



Graph={
    'A': [('B',2),('C',3)],
    'B': [('D',5),('E',1)],
    'C': [('F',4)],
    'D': [('H',2)],
    'E': [('G',7)],
    'F': [('G',9)],
    'G': [('I',2)],
    'H': [('I',6)],
}

cost,path=UCS(Graph,'A','I')
if cost:
    print("Cost : ", cost)
    print("Path : ",path)
