import pygame
import numpy as np
import random

width,height=500,400
screen = pygame.display.set_mode((width,height))

pygame.init()

class Boid():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speed=10
    
    def draw(self):
        #pygame.draw.rect(screen,(255,255,255),(self.x+10,self.y+10,10,10))
        ##############################################################L_vert####M_vert#####R_Vert
        pygame.draw.polygon(surface=screen, color=(255, 0, 0),points=[(self.x+(self.x*10),self.y+(self.y*30)), (self.x+(self.x*20), self.y+(self.y*10)), (self.x+(self.x*30),self.y+(self.y*30))])

boids=[]

for i in range(0,5):
    boids.append(Boid(i,i))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for boid in boids:
        boid.draw()
    
    pygame.display.update()