import numpy as np
import random

class zieher:
    def __init__(self):
        self.assignedPolicys = []
        
        
        self.mutationValue = random.randrange(10,200)/10000
        # self.mutationValue = 0.005
        self.truncationRatio = 0.4
        self.evaluationRunNum = 10 #number of matches played
        requestRatingFlag = 0
        self.maxGeneration = 100
        self.evaluationMatchesPerPol = 10
        self.polNum = 0
        self.generation = 0
        self.maxEloIncreasedCounter = 0
        self.maxElo = 0
    
    def seed(self,ladder,amount,seedType):
        self.polNum = amount
        
        if seedType == 0:
        #take amount top player
            sortedRating = ladder.getRatingSortedPolicyList()
            for i in range(amount):
                ladder.copyPolicyToTop(sortedRating[-i+1])
                self.assignedPolicys.append(ladder.getPolicys()[-1])
        if seedType == 2:
            for i in range(amount):
                ladder.addRandomPolicy()
                self.assignedPolicys.append(ladder.getPolicys()[-1])
        if seedType == 1:
            for i in range(amount):
                ladder.copyPolicyToTop(ladder.getRandomPolicyFromPols())
                self.assignedPolicys.append(ladder.getPolicys()[-1])
            
        
    def advanceGeneration(self,ratings):
        pass
        
    
        
    def update(self,ladder):
        #check for stagnation
        sortedByRating = self.getAssignedPolSortedByRating()
        if sortedByRating[-1].getRating() > self.maxElo:
            self.maxEloIncreasedCounter = 0
            self.maxElo = sortedByRating[-1].getRating() 
            
            
            
        if self.maxEloIncreasedCounter >= 5:
            return -1
            
        self.maxEloIncreasedCounter+=1
    
    
    
    
    
    
        #let asigned players play evaluation matches
        self.generation+=1
        print(" ADVANCING GENERATION ")
       
        for i in range(self.evaluationMatchesPerPol):
            ladder.printRatings()
            print([pol.getRating() for pol in self.assignedPolicys])
            print("Generation: " +str(self.generation))
            print("Stagnation Detection: " +str(self.maxEloIncreasedCounter))
            
            for pol in self.assignedPolicys:
                print("-------------------------")
                ladder.playRandomMatch(pol)
                
            for pol in self.assignedPolicys:
                ladder.playMatchAgainstBest(pol,random.randrange(0,2),random.randrange(0,10))
                
        
            
                
                
        #truncate and copy splitAmount top Policiys
        splitAmount = int(self.polNum*self.truncationRatio)
        print(splitAmount)
        
        sortedByRating = self.getAssignedPolSortedByRating()
        
        sortedByRating[-1].saveToFile("nets/gen"+str(self.generation)+"_"+str(sortedByRating[-1].getRating())+"_pol"+str(sortedByRating[-1].getId()))
        
        for i in range(self.polNum-splitAmount):
            self.copyPol(sortedByRating[i],sortedByRating[-(i%splitAmount)-1])
            
        # for i in range(splitAmount):
            # ladder.copyPolicyToTop(sortedByRating[-(i+1)])
        
        
        
        #mutate
        for i in range(self.polNum-splitAmount):
            self.mutatePol(sortedByRating[i])
            
                
        return 0
    
        
   
    def addPolicy(self,policy):
        pass
        
    def mutateMatrix(self,matrix):
        size = matrix.shape[0]
        flattened = matrix.flatten() + self.mutationValue*np.random.normal(-1,1,size**2)
        matrix = flattened.reshape((size,size))
        
    def mutatePol(self,pol):
        self.mutateMatrix(pol.getMatrix())
        pol.setRating(1200)
    
    def getAssignedPolSortedByRating(self):
        return sorted(self.assignedPolicys, key=lambda pol: pol.getRating())
        
    def copyPol(self,polDest,polSrc):
        polDest.setMatrix(polSrc.getMatrix())
        polDest.setRating(polSrc.getRating())
        
    
        
    
        
    
    
    