import eloSystem
import world
import policy
import random
import zeichner
import zieher
import threading


class ladder:
    def __init__(self):
        random.seed()
        self.zieher = []
        self.matchNumberList = []
        self.policys = []
        self.eloSys = eloSystem.eloSystem
        
        #-------------------------
        
        for i in range(20):
            self.addRandomPolicy()
            
        print(len(self.policys))    
        self.zieh = zieher.zieher()
        self.zieh.seed(self,30,2)
        print(len(self.policys))    
        
    
    def update(self):
        pass
        #play random matches
        # for i in range(0,15):
            # print("\n--------------------------------------------------------------------------\nMatch: " + str(i*15) + "\n--------------------------------------------------------------------------")
            # for j,pol in enumerate(self.policys):
                # print("\n\n--------------------------------------------------------------------------\n")
                
                # self.playMatch(pol,random.choice(self.policys))
        
        
        #update zieher
        if self.zieh.update(self) == -1:
            self.zieh=zieher.zieher()
            self.zieh.seed(self,30,0)
            
        
    def playMatch(self,polA,polB):
        
        #print("Initiating Match: " +str(polA.getId()) + " vs " + str(polB.getId()))
        w = world.world()
        
        result = w.playMatch(polA.getMatrix(),polB.getMatrix())
        
        if result == 0:
            polA.matchPlayed(polB.getRating(),1)
            polB.matchPlayed(polA.getRating(),0)
            #print("Policy " + str(polA.getId()) + " Won")
            
        if result == 1:
            polA.matchPlayed(polB.getRating(),0)
            polB.matchPlayed(polA.getRating(),1)
            #print("Policy " +str(polB.getId()) + " Won")
            
        if result == -1:
            polA.matchPlayed(polB.getRating(),0.5)
            polB.matchPlayed(polA.getRating(),0.5)
            #print("Draw")
            
    def playRandomMatch(self,pol):
        if random.randrange(0,2) == 0:
            self.playMatch(pol,random.choice(self.policys))
        else:
            self.playMatch(random.choice(self.policys),pol)
            
    def playMatchAgainstBest(self,pol,spawn,offset):
        best = self.getRatingSortedPolicyList()[-offset]
        if spawn == 0:
            self.playMatch(pol,best)
        else:
            self.playMatch(best,pol)
            
        
    def playRandomMatchMultiTthread(self,pol):    
        pass
        
    def getPolicys(self):
        return self.policys
        
    def printRatings(self):
        print("---------------------------")
        for p in self.policys:
            print(p.getRating())
        print("---------------------------")
        
    def addRandomPolicy(self):
        self.policys.append(policy.policy(len(self.policys)))
        self.policys[-1].randomizeMatrix(60)
        
    def copyPolicyToTop(self,pol):
        self.addRandomPolicy()
        self.policys[-1].setMatrix(pol.getMatrix())
        self.policys[-1].setRating(pol.getRating())
        
    def getRandomPolicyFromPols(self):
        return random.choice(self.policys)
        
    def getRatingSortedPolicyList(self):
        return sorted(self.policys, key=lambda pol: pol.getRating())
        
        
     