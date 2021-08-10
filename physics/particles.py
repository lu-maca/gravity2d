import sys
sys.path.append('C:\\Users\\Luca\\Desktop\\progetti\\fisica1\\gravity')

from utils import vectors
from physics import forces


class Particle:
    # constructor
    def __init__(self, mass, charge , position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.charge = charge
        self.mass = mass

    # get methods 
    def getParticleMass(self):
        return self.mass
    
    def getParticlePosition(self):
        return self.position
    
    def getParticleVelocity(self):
        return self.velocity

    def getParticleAcceleration(self):
        return self.acceleration



    