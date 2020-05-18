# Neural Net project. 

class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        self.adjacencyList[vertex] = []
    
    def addEdge(self, v1, v2):
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)

graph = Graph()

graph.addVertex(1)
graph.addVertex(3)
graph.addVertex(2)

graph.addEdge(1,3)
graph.addEdge(1,2)

print(graph.adjacencyList)