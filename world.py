#tile based world
import tile
import agent
import numpy as np
import darwin
import random
#import zeichner
import time

class world:
    def __init__(self):
        self.iSize = 20
        self.iTileSize = 40
        self.aTiles = [[tile.tile() for j in range(self.iSize)] for k in range(self.iSize)]
        self.aWalls = []
        self.aWalls.append([200,200,400,100])
        self.aWalls.append([200,500,400,100])
        
        self.aWalls.append([0,0,30,800])
        self.aWalls.append([770,0,30,800])
        
        # self.aWalls.append([398,398,4,4])
        
        #print("world init")
        self.agents = []
        #self.recalcWalls()
        
   
        

        
        
        #--------------------------physics------------
        self.simulationTime = 0 #time used for sim
        self.deltaT = 0.02
        
    def recalcWalls(self):
        self.aWalls = []
        for j in range(self.iSize):
            for k in range(self.iSize):
                if self.aTiles[j][k].getTyp() == 1:
                    self.aTiles[j][k].setPos(np.array([j*self.iTileSize,k*self.iTileSize]))
                    self.aWalls.append(self.aTiles[j][k])
        
    def reset(self):
        self.agentA.reset()
        
    def getWalls(self):
        return self.aWalls
        
    def update(self):
        return self.updateAgents()

    def updateAgents(self):
        for ind,ag in enumerate(self.agents):
            ag.update(self,self.deltaT)
           
            if ag.getHp() <= 0:
                return ind
        
        return -1
            
    def getTiles(self):
        return self.aTiles
        
    def getSize(self):
        return self.iSize
    
    def getAgents(self):
        return self.agents
        
    def addAgent(self,agent):
        self.agents.append(agent)
        
    def playMatch(self,matrixA,matrixB):
        self.agents = [agent.agent(np.array([400+random.randrange(-100,100),800.0]),random.uniform(0, np.pi*2),matrixA.shape[0]),agent.agent(np.array([400+random.randrange(-100,100),0.0]),random.uniform(0, np.pi*2),matrixB.shape[0])]
        self.agents[0].setConnectionMatrix(matrixA)
        self.agents[1].setConnectionMatrix(matrixB)
        
        for i in range(300):
            dead = self.update()
          
            if dead == 1:
                return 0
            if dead == 0:
                return 1
        
        distA = np.linalg.norm(self.agents[0].getPos()-np.array([400,400]))
        distB= np.linalg.norm(self.agents[1].getPos()-np.array([400,400]))
        
        
        
        if distA < distB:
            return 0
        return 1
        
        
        
         #0: netA won; 1: netB won
        
    
        

        
        
       
        
    