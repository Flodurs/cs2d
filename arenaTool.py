
import numpy as np

import pygame
import zeichner
import world
import agent
import time
import random

class framework:
    def __init__(self):
        self.bRunning = True 
        self.renderer = zeichner.zeichner()
               
        self.w = world.world()
        random.seed()
        
        # pathB ="D:/Dev/cs2d/fighting/nets/gen4_1395_pol647.npy"
        # # #pathB = pathA
        # pathA = "D:/Dev/cs2d/fighting/nets/gen4_1395_pol647.npy"
        
        # pathB ="D:/Dev/cs2d/fighting/netsStrict/gen28.npy"
        # # #pathB = pathA
        # pathA = "D:/Dev/cs2d/fighting/netsStrict/gen28.npy"
        
        pathB ="D:/Dev/cs2d/cs2d/fxnets/gen12.npy"
        # # #pathB = pathA
        pathA = "D:/Dev/cs2d/cs2d/fxnets/gen0.npy"
        
        self.matrixA = np.load(pathA,allow_pickle=False)
        self.matrixB = np.load(pathB,allow_pickle=False)
        
        self.w.addAgent(agent.agent(np.array([400+random.randrange(-100,100),800.0]),random.uniform(0, np.pi*2),self.matrixA.shape[0]))
        self.w.addAgent(agent.agent(np.array([400+random.randrange(-100,100),0.0]),random.uniform(0, np.pi*2),self.matrixB.shape[0]))
        
        
        
        self.w.getAgents()[0].setConnectionMatrix(self.matrixA)
        self.w.getAgents()[1].setConnectionMatrix(self.matrixB)
        
        pygame.init()
        self.frame = 0
        
    def run(self):
        while self.bRunning == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bRunning = False
        
            
            self.update()
            self.render()
            time.sleep(0.02)
            if self.frame == 300:
                self.bRunning = False
                distA = np.linalg.norm(self.w.getAgents()[0].getPos()-np.array([400,400]))
                distB= np.linalg.norm(self.w.getAgents()[1].getPos()-np.array([400,400]))
        
        
        
                if distA < distB:
                    print("A Won")
                else:
                    print("B won")
            self.frame+=1
            #print(self.frame)
            
    def update(self):
        if self.w.update() != -1:
            time.sleep(3)
            self.bRunning = False
        print("----------")    
            
       
        
        
        # for world in self.worlds:
            # world.update()
            
            
        
    def render(self):
        self.renderer.render(self.w)
        
f = framework()
f.run()







