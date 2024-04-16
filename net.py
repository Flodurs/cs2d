import numpy as np

class net:
    def __init__(self,nodeNum):
        self.nodes = np.zeros(nodeNum)
        self.nodeBuffer = np.zeros(nodeNum)
        #avoid initializing it here to increase **performance**
        self.connectionMatrix = []
        self.nodeNum = nodeNum
        
    def step(self):
        
        self.nodes = np.tanh(np.matmul(self.connectionMatrix, self.nodes))

    def setConnectionMatrix(self, matrix):
        self.connectionMatrix = matrix
        
    def getNode(self, nodeIndex):
        return self.nodes[nodeIndex]
    
    def setNode(self, nodeIndex, value):
        self.nodes[nodeIndex] = value
        
    def reset(self):
        self.nodes = np.zeros(self.nodeNum)
        
    def ReLU(self,x):
        return (abs(x) + x) / 2