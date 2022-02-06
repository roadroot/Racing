class Voiture:
    def __init__(self):
        self.vitesse=0
    def accelerer(self, v):
        self.vitesse+=v

    def decellerer(self,v):
        self.vitesse-=v
    