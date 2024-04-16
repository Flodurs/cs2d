import policy
import random
import world
import numpy as np

class strictTrainer:
    def __init__(self):
        self.windowSize = 1000
        self.mutationValue = 0.004
        self.window = []
        
    def mutateMatrix(self,matrix):
        size = matrix.shape[0]
        flattened = matrix.flatten() + self.mutationValue*np.random.normal(-1,1,size**2)
        matrix = flattened.reshape((size,size))
        
    def mutatePol(self,pol):
        self.mutateMatrix(pol.getMatrix())
        
        
        
    def update(self):
        #generate Random Pol or Mutate Existing
        pol = policy.policy(1)
        if random.randrange(0,2) == 0:
            pol.setMatrix(random.choice(self.window).getMatrix())  
            self.mutatePol(pol)
        
        score = 0
        pol.randomizeMatrix(60)
        
        #let it play Matches vs Window
        w = world.world()
        for opponent in self.window:
            for i in range(5):
                score+=1-w.playMatch(opponent.getMatrix(),pol.getMatrix())
                score+=w.playMatch(pol.getMatrix(),opponent.getMatrix())
                
        
        
        print(score)
        #if it scores a certain score append it to windowSize
        if score >= (len(self.window)*2*5)/2:
            self.window.append(pol)
            pol.saveToFile("netsStrict/gen"+str(len(self.window)))
            print("Found")
    
    
st = strictTrainer()
while True:
    st.update()