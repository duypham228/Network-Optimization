class Graph:
  def __init__(self):
    self.graph = {}

  def addVertex(self, vertex, weight):
    vertex = Vertex(vertex)


class Vertex:
  def __init__(self, verNum, neighbor):
    self.verNum = verNum
    self.neighbor = {}
