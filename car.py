import math
from operator import mod
class car:
    def __init__(self):
        self.vitesse=0
        self.direction=0
        self.position=(0,0)
    def accelerate(self, v):
        self.vitesse+=v

    def decellerate(self,v):
        self.vitesse-=v
    def turnRight(self,direction):
        self.direction= (self.direction-direction) % math.pi

    def turnLeft(self,direction):
        self.direction+=(self.direction+direction) % math.pi
    def move(self):
        self.position = (self.position[0]+math.cos(self.direction)*self.vitesse, self.position[1]+math.sin(self.direction)*self.vitesse)
