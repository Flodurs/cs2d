import numpy as np
import random


class policy:
    def __init__(self,id):
        self.matrix = []
        self.id = id
        
        self.k = 40
        self.rating = 1200
        self.matchesPlayed = 0
        
        self.score = 0
        
        
    def matchPlayed(self,opponentRating,score):
        self.matchesPlayed+=1
        Erwartungswert = 1/(1+10**((opponentRating-self.rating)/400))
        self.rating+=round(self.k*(score-Erwartungswert))
        print("Policy "+str(self.id) + " new Rating is "+str(self.rating))
        
    def setMatrix(self,matrix):
        self.matrix = np.zeros((matrix.shape))
        for j in range(len(self.matrix)):
            for k in range(len(self.matrix)):
                self.matrix[j][k]=matrix[j][k]
    
    def getMatrix(self):
        return self.matrix
        
    def getRating(self):
        return self.rating
        
    def setRating(self,rating):
        self.rating = rating
        
    def getMatchesPlayed(self):
        return self.matchesPlayed
        
    def getId(self):
        return self.id
    
    def randomizeMatrix(self,size):
        self.matrix = np.zeros((size,size))
        for j in range(len(self.matrix)):
            for k in range(len(self.matrix)):
                self.matrix[j][k]=random.randrange(-10000,10000)/10000
        
    def saveToFile(self,path):
        np.save(path, self.matrix, allow_pickle=False)
        
    def loadFromFile(self,path):
        pass
        
    def setScore(self,s):
        self.score = s
        
    def getScore(self):
        return self.score
        
    def addScore(self,s):
        self.score += s
    
        
        
        