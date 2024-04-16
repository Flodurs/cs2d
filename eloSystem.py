# Implements an elo System to evaluate Agent strength in self play
# k-Faktor = 15 like in tennis (they have constant k=15 i assume for a reason)
# division by 400 like chess aka 400 Point elo difference corresponds to expected 0.91 score for the higher rated Agent(Player)

class eloSystem:

    def __init__(self,playerNum):
        #print("innit eloSsytem")
        self.eloList = []
        
        self.k = 15
        for i in range(playerNum):
            self.addPlayer()
        
        
    def addPlayer(self):
        self.eloList.append(1200)
    
    
    def removePlayer(self):
        print("")
        
        
    def matchPlayed(self,playerA,playerB,resultA):
        #Erwartungswerte berechnen
        ErwartungswertA = 1/(1+10**((self.eloList[playerB]-self.eloList[playerA])/400))
        ErwartungswertB = 1-ErwartungswertA
        
        #Elo Zahlen updaten
        self.eloList[playerA]+=round(self.k*(resultA-ErwartungswertA))
        self.eloList[playerB]+=round(self.k*((1-resultA)-ErwartungswertB))
    
    
    
    def printElos(self):
        print(self.eloList)
        
    def getElos(self):
        return self.eloList
        
    
