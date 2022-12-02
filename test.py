from graphGenerator import *
from heap import *

print("Start Testing ...")
print("------------------------------------------------")

# print("Test Normal Graph")
# graph = Graph()
# print("Test Add vertices 0 1 2")
# graph.addVertex(0)
# graph.addVertex(1)
# graph.addVertex(2)
# print(graph.graph)
# print("Test Add edges 0-1(5), 0-2(3), 2-3(10)")
# graph.addEdge(0,1,5)
# graph.addEdge(0,1,4)
# graph.addEdge(0,2,3)
# graph.addEdge(2,3,10)
# print(graph.graph)
# print("------------------------------------------------")

# print("Test Sparse Graph")
# sparseGraph = sparseGraph(7)
# print(sparseGraph.graph)
# print(sparseGraph.isEdge(3,4))


# denseGraph = denseGraph(5000)
# # print(denseGraph.graph[0])
# for i in range(10):
#     print(len(denseGraph.graph[i]))
# print(len(denseGraph.graph))

heap = Heap(10)
print(heap.D)
print(heap.P)
print(heap.H)
print(heap.maximum())
# print(heap)

