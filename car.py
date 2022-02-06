class Voiture:
    def __init__(self):
        self.vitesse=0
        self.direction=0
        self.position=(0,0)
    def accelerate(self, v):
        self.vitesse+=v

    def decellerate(self,v):
        self.vitesse-=v
    def turnRight(self,direction):
        self.direction+=direction

    def turnLeft(self,direction):
        self.direction+=direction

