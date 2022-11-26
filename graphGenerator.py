import random
import math

class Graph:
  def __init__(self):
    self.graph = {}

  def addVertex(self, id):
    self.graph[id] = {}

  def addEdge(self, v1, v2, weight):
    if v1 not in self.graph:
      self.addVertex(v1)
    if v2 not in self.graph:
      self.addVertex(v2)
    self.graph[v1][v2] = weight

  def isEdge(self, v1, v2):
    if v1 == v2:
      return True
    if v1 in self.graph:
      if v2 in self.graph[v1]:
        return True
    return False


def sparseGraph(numVer):
  graph = Graph()

  for i in range(numVer - 1):
    graph.addEdge(i, i+1, random.randint(1,100))
  graph.addEdge(numVer-1, 0, random.randint(1,100))

  for i in range(numVer):
    while len(graph.graph[i]) < 6: 
      vertex = random.randint(0, numVer-1)
      if not graph.isEdge(i, vertex):
        graph.addEdge(i, vertex, random.randint(1,100))

  return graph

def denseGraph(numVer):
  graph = Graph()

  for i in range(numVer - 1):
    graph.addEdge(i, i+1, random.randint(1,100))
  graph.addEdge(numVer-1, 0, random.randint(1,100))

  numNeighbor = []
  mean = numVer / 5
  standard_dev = 50
  for i in range(numVer): 
    num = random.gauss(mean, standard_dev) 
    numNeighbor.append(math.floor(num))
  
  for i in range(numVer):
    while len(graph.graph[i]) < numNeighbor[i]:
      vertex = random.randint(0, numVer-1)
      if not graph.isEdge(i, vertex):
        graph.addEdge(i, vertex, random.randint(1,100))

  return graph

  






