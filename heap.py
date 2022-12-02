import math

class Heap:
    def __init__(self, num):
        self.H = [None] * num
        self.D = [None] * num
        self.P = [None] * num
        self.lastNode = 0
    
    def findPosition(self, id):
        return self.P[id]

    def getValue(self, id):
        return self.D[id]

    def maximum(self):
        return self.H[0]

    def insert(self, id, value):
        self.D[id] = value


def findParent(index):
    return 
        

