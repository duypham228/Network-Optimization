from graphGenerator import *


graph = Graph()
graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addEdge(0,1,5)
graph.addEdge(0,2,3)
graph.addEdge(2,3,10)

sparseGraph = sparseGraph(10)



# print(graph.graph)
print(sparseGraph.graph)
print(sparseGraph.isEdge(3,4))