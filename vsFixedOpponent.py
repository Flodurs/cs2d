import numpy as np
import world
import policy
import multiprocessing


class fixedOppTrainer:

    def __init__(self):
        self.oppPols = []
        self.policys = []
        
        self.truncationRatio = 0.35
        self.polNum = 100
        self.oppNum = 1
        self.mutationValue= 0.01
        self.evalRunsNum = 20
        
        self.generation=0
        
        for i in range(self.oppNum):
            self.oppPols.append(self.getRandomPolicy())
        
        for i in range(self.polNum):
            self.policys.append(self.getRandomPolicy())
    
    
    def update(self):
        #evaluate 
        self.parallelEvalPols()
        
        
        #selectAndMutate
        
        self.selectAndMutate()
        self.printInfo()
        for pol in self.policys:
            pol.setScore(0)
        self.generation+=1    
            
        if self.generation%10 == 0:
            self.copyPol(self.oppPols[0],self.getPolSortedByScore()[-1])
        
        
    def evaluatePols(self):
       
        for i in range(self.evalRunsNum):
            for pol in self.policys:
                for opp in self.oppPols:
                    w = world.world()
                    result = w.playMatch(pol.getMatrix(),opp.getMatrix())
                    
                    if result == 0:
                        pol.addScore(1)
                        
                    w = world.world()
                    result = w.playMatch(opp.getMatrix(),pol.getMatrix())
                    
                    if result == 1:
                        pol.addScore(1)
                   
    def parallelEvalPols(self):
        pool = multiprocessing.Pool(20)
        w = world.world()
        
        for pol in self.policys:
            for opp in self.oppPols:
                processes = [pool.apply_async(w.playMatch, args=[pol.getMatrix(),opp.getMatrix()]) for i in range(self.evalRunsNum)]
                results = [p.get() for p in processes]
                
                pol.addScore(sum([1 for r in results if r == 0]))
                

                processes = [pool.apply_async(w.playMatch, args=[opp.getMatrix(),pol.getMatrix()]) for i in range(self.evalRunsNum)]
                results = [p.get() for p in processes]
               
                pol.addScore(sum([1 for r in results if r == 1]))                
                
        
        
    def selectAndMutate(self):
        splitAmount = int(self.polNum*self.truncationRatio)
        sortedByScore = self.getPolSortedByScore()
        
        sortedByScore[-1].saveToFile("fxnets/gen"+str(self.generation))
        
        for i in range(self.polNum-splitAmount):
            self.copyPol(sortedByScore[i],sortedByScore[-(i%splitAmount)-1])
            
        for i in range(self.polNum-splitAmount):
            self.mutatePol(sortedByScore[i])    
       
        
    def mutateMatrix(self,matrix):
        size = matrix.shape[0]
        flattened = matrix.flatten() + self.mutationValue*np.random.normal(-1,1,size**2)
        matrix = flattened.reshape((size,size))
        
    def mutatePol(self,pol):
        self.mutateMatrix(pol.getMatrix())
        
    def getPolSortedByScore(self):
        return sorted(self.policys, key=lambda pol: pol.getScore())
        
    def getRandomPolicy(self):
        pol = policy.policy(len(self.policys))
        pol.randomizeMatrix(60)
        return pol
        
    def printInfo(self):
        print("-------------------------------------")
        scores = [p.getScore() for p in self.policys]
        print(scores)
        print("Best: " + str(max(scores)) + "/" + str(self.evalRunsNum*self.oppNum*2))
        
    def copyPol(self,polDest,polSrc):
        polDest.setMatrix(polSrc.getMatrix())
        polDest.setRating(polSrc.getRating())
        
if __name__ == "__main__":  
    fx = fixedOppTrainer()
    for i in range(100):
        fx.update()
        
    
    
    
    