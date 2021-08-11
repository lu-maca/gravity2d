import sys
sys.path.append('C:\\Users\\Luca\\Desktop\\progetti\\fisica1\\gravity')

from utils import solver


class eulerCromer_C():
    def eulerCromer(self,particleList,dt):
        for p in particleList:
            p.velocity = p.getParticleVelocity() + p.getParticleAcceleration()*dt 
            p.position = p.getParticlePosition() + p.getParticleVelocity()*dt


class velocityVerlet_C:
    def __init__(self):
        midVelocity = []

    def nullMidVelocity(self):
        self.midVelocity = []

    def velocityVerlet_firstStep(self,particleList,dt):
        velocityVerlet_C.nullMidVelocity(self)

        for pIdx,p in enumerate(particleList):
            self.midVelocity.append(p.getParticleVelocity() + 0.5*p.getParticleAcceleration()*dt)
            p.position = p.getParticlePosition() + self.midVelocity[pIdx]*dt
        
    def velocityVerlet_secondStep(self,particleList,dt):
        for pIdx,p in enumerate(particleList):
            p.velocity = self.midVelocity[pIdx] + 0.5*p.getParticleAcceleration()*dt


def setIntegrator(name):
    if name == "EC":
        return eulerCromer_C()
    elif name == "Verlet":
        return velocityVerlet_C()