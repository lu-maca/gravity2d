import sys
sys.path.append('..')

from utils import vectors
from physics import forces

red = (200,0,0)

class Particle:
    # constructor
    def __init__(self, mass, charge , position, velocity, acceleration, color):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.charge = charge
        self.mass = mass
        self.color = color

    # get methods 
    def getParticleMass(self):
        return self.mass
    
    def getParticlePosition(self):
        return self.position
    
    def getParticleVelocity(self):
        return self.velocity

    def getParticleAcceleration(self):
        return self.acceleration

    def getParticleColor(self):
        return self.color
    



    