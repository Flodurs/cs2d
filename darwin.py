import random
import copy
import statistics
import numpy as np
import os
import numpy as np
import math

class darwin:
    def __init__(self,nodeNum, genoTypeNum, oldGenoTypeNum):
        print("Init darwin")
        random.seed()
        
        self.genoTypeNum = genoTypeNum
        self.oldGenoTypeNum = oldGenoTypeNum
        self.nodeNum = nodeNum
        self.generation = 0
        self.mutationRate = 0.009
       
       
        #Bruh stacked * with lists doesnt do what i thought it does (only do it once)
        self.genoTypes = np.zeros((genoTypeNum, nodeNum, nodeNum))
        self.oldGenoTypes = np.zeros((oldGenoTypeNum, nodeNum, nodeNum))
        
        self.allTimeBest = np.zeros((nodeNum,nodeNum))
        self.allTimeBestFit = 0
        
        self.oldGenoTypePointer = 0
        self.oldGenoTypeFlag = 0
        
        self.randomizeGenoTypes()
        
    def getAllTimeBest(self):
        return self.allTimeBest
        
    def storeOldGenoType(self,genoTypeIndex):
        for j in range(self.nodeNum):
            for k in range(self.nodeNum):
                self.oldGenoTypes[self.oldGenoTypePointer][j][k] = self.genoTypes[genoTypeIndex][j][k]
        self.oldGenoTypePointer+=1
        if self.oldGenoTypePointer >= self.oldGenoTypeNum:
            self.oldGenoTypePointer = 0
            self.oldGenoTypeFlag = 1
    
    def insertOldGenoTypeIntoPop(self,targetGenoTypeIndex):
        if self.oldGenoTypePointer != 0:
            if self.oldGenoTypeFlag == 1:
                index = random.randrange(0,self.oldGenoTypeNum)
            else:
                index = random.randrange(0,self.oldGenoTypePointer)
        else:
            index = 0
            
            
        for j in range(self.nodeNum):
            for k in range(self.nodeNum):
                self.genoTypes[targetGenoTypeIndex][j][k] = self.oldGenoTypes[index][j][k]
                    
    def printGenePool(self):
        print("-----------------------")
        for i in range(self.genoTypeNum):
            print(self.genoTypes[i])
        print("-----------------------")
        
    def getGenoType(self,genoTypeIndex):
        return self.genoTypes[genoTypeIndex]
        
    def randomizeGenoTypes(self):
        for gt in range(self.genoTypeNum):
            for j in range(self.nodeNum):
                for k in range(self.nodeNum):
                    self.genoTypes[gt][j][k] = random.randrange(-30000,30000)/30000
            
        
    def mutateGenoType(self,genoTypeIndex,mutationRate):
        flattened = self.genoTypes[genoTypeIndex].flatten() + mutationRate*np.random.normal(0,1,self.nodeNum**2)
        self.genoTypes[genoTypeIndex] = flattened.reshape((self.nodeNum,self.nodeNum))
           
    def performCrossover(self,indexA,indexB,targetIndex):
        for j in range(self.nodeNum):
            for k in range(self.nodeNum):
                if random.randrange(0,2) == 0:
                    self.genoTypes[targetIndex][j][k]=self.genoTypes[indexA][j][k]
                else:
                    self.genoTypes[targetIndex][j][k]=self.genoTypes[indexB][j][k]
                    
    def getMutationRate(self):
        return self.mutationRate
        
    def advanceGeneration(self,fitnessList):
        self.generation += 1
        #self.mutationRate = np.exp(-0.01*self.generation)
        #self.mutationRate = 0.02*math.sin(self.generation*(math.pi/100))
        
        #if self.mutationRate < 1/(self.nodeNum**2):
        #self.mutationRate = 0.001
            
        sortedFitness = np.argsort(fitnessList)
        
        # print(self.oldGenoTypeFlag)
        # print(self.oldGenoTypePointer)
        
        # if max(fitnessList) > self.allTimeBestFit:
            # self.allTimeBestFit = max(fitnessList)
            # index = np.where(fitnessList == max(fitnessList))[0][0]
            # #print(self.allTimeBestFit)
            # for j in range(self.nodeNum):
                # for k in range(self.nodeNum):
                    # self.allTimeBest[j][k]=self.genoTypes[index][j][k]
                    
        topNum = 15
            
        for u in range(topNum):
            self.storeOldGenoType(sortedFitness[-(u+1)])
        
        
        for u in range(self.genoTypeNum-topNum):
            for j in range(self.nodeNum):
                for k in range(self.nodeNum):
                    self.genoTypes[sortedFitness[u]][j][k]=self.genoTypes[sortedFitness[-(u%topNum+1)]][j][k]
                    
        for i in range(self.genoTypeNum-topNum):
            self.mutateGenoType(sortedFitness[i],self.mutationRate)
        
        for i in range(1):
            self.insertOldGenoTypeIntoPop(sortedFitness[i])
                    
        
            
        
        
        
        
        
        
        
        
    
        
        
       
        
        