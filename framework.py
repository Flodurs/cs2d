import pygame
import zeichner
import world
import agent


class framework:
    def __init__(self):
        self.bRunning = True 
        self.renderer = zeichner.zeichner()
               
        self.worlds = [world.world() for i in range(10)]
        self.worldViewd = 0
        pygame.init()
        
    def run(self):
        while self.bRunning == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bRunning = False
        
        
            self.update()
            self.render(self.worldViewd)
            
    def update(self):
        self.worlds[0].update()
        # for world in self.worlds:
            # world.update()
            
            
        
    def render(self,w):
        self.renderer.render(self.worlds[w],self.worlds[w].getAgents())
        
f = framework()
f.run()