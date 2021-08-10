import sys
sys.path.append('C:\\Users\\Luca\\Desktop\\progetti\\fisica1\\gravity')

from physics import particles as ptc
from physics import forces as force
import utils.vectors as vec
from utils.mng_files import *
from time_integration import time_integration as integr

class Simulation:
    def __init__(self):
        self.dt = 0.1
        self.count = 0
        self.t = 0
        self.tfin = 100
        self.integrator = 'EC'
        self.isSimRunning = True
        self.particleList = []
        self.printFreq = 10

    def updateTime(self):
        self.t += self.dt
        self.count += 1

    def stop(self):
        self.isSimRunning =  False

    def initializeParticle(self):
        n = ptc.Particle(300,0,vec.Vector2D(1000,0),vec.Vector2D(0,100),vec.Vector2D(0,0))
        m = ptc.Particle(1500000,0,vec.Vector2D(0,0),vec.Vector2D(0,0),vec.Vector2D(0,0))
        self.particleList.append(n)
        self.particleList.append(m)

    def zeroAcceleration(self):
        for part in self.particleList:
            part.acceleration = vec.Vector2D(0,0)

    def computeParticleAcceleration(self):
        Simulation.zeroAcceleration(self)
        for firstIdx,firstPart in enumerate(self.particleList):
            for secondIdx,secondPart in enumerate(self.particleList):
                if firstIdx < secondIdx:
                    f = force.gravityForce(firstPart.mass, secondPart.mass,firstPart.position, secondPart.position)
                    firstPart.acceleration += f/firstPart.mass
                    secondPart.acceleration -= f/secondPart.mass
    
    def writeResults(self):
        f_pos = open('RESULTS\\POS\\' + str(self.count) + '.txt', 'x')
        for p in self.particleList:
            pos = p.getParticlePosition()
            f_pos.write(str(pos.x) +'\t' + str(pos.y) +'\n' )
        f_pos.close()

        f_vel = open('RESULTS\\VEL\\' + str(self.count) + '.txt', 'x')
        for p in self.particleList:
            vel = p.getParticleVelocity()
            f_vel.write(str(vel.x) +'\t' + str(vel.y) +'\n' )
        f_vel.close()


    def run(self):
        deleteFiles()
        Simulation.initializeParticle(self)
        while self.isSimRunning:
            if (self.integrator == 'EC'):
                Simulation.computeParticleAcceleration(self)
                integr.EulerCromer(self.particleList, self.dt)
            elif (self.integrator == 'Verlet'):
                integr.velocityVerlet_firstStep(self.particleList,self.dt)
            if self.count%self.printFreq == 0:
                Simulation.writeResults(self)
            
            Simulation.updateTime(self)

            if self.t >= self.tfin:
                Simulation.stop(self)