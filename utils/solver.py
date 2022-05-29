import sys
import pygame
import time
sys.path.append('..')


from physics import particles as ptc
from physics import forces as force
import utils.vectors as vec
from utils.mng_files import *
from utils import mng_files as mngF
from time_integration import time_integration as integr


class Simulation:
    def __init__(self):
        self.particleList = []
        self.count = 0
        self.t = 0
        self.isSimRunning = True
        self.printFreq = 1
        self.dt = 0
        self.tfin = 0
        self.integrator = 'none'
        self.show = False # per mostrare grafico
        
    def updateTime(self):
        self.t += self.dt
        self.count += 1

    def stop(self):
        self.isSimRunning =  False

    def initializeSimulation(self):
        f = mngF.inputFile("config.txt")
        f.readFile(self) 

    def zeroAcceleration(self):
        for part in self.particleList:
            part.acceleration = vec.Vector2D(0,0)

    def computeParticleAcceleration(self):
        Simulation.zeroAcceleration(self)
        for firstIdx,firstPart in enumerate(self.particleList):
            for secondIdx,secondPart in enumerate(self.particleList):
                if firstIdx < secondIdx:
                    f = force.gravityForce(firstPart.mass, secondPart.mass,firstPart.position, secondPart.position)
                    firstPart.acceleration -= f/firstPart.mass
                    secondPart.acceleration += f/secondPart.mass
    
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

    def drawResult(self):
        x0 = 700       
        if self.count == 0:
            self.window = pygame.display.set_mode((x0,x0))
            for part in self.particleList:
                pos = part.position
                pygame.draw.circle(self.window,part.getParticleColor(),(x0/2 + pos.x/3,x0/2 + pos.y/3),2)
            pygame.display.update()
            pygame.time.delay(100)
        else:
            self.window.fill((0,0,0))
            for part in self.particleList:
                pos = part.getParticlePosition()
                mass = part.getParticleMass()
                pygame.draw.circle(self.window,part.getParticleColor(),(x0/2 + pos.x/3,x0/2 + pos.y/3),2)
            pygame.display.update()
            pygame.time.delay(100)

    def run(self):
        deleteFiles()
        Simulation.initializeSimulation(self)

        integrator = integr.setIntegrator(self.integrator)

        while self.isSimRunning:
            if (self.integrator == 'EC'):
                Simulation.computeParticleAcceleration(self)
                integrator.eulerCromer(self.particleList,self.dt)
            elif (self.integrator == 'Verlet'):
                integrator.velocityVerlet_firstStep(self.particleList,self.dt)
                Simulation.computeParticleAcceleration(self)
                integrator.velocityVerlet_secondStep(self.particleList,self.dt)

            if self.count%self.printFreq == 0:
                if self.show:
                    Simulation.drawResult(self)
                    time.sleep(0.1)
                else:
                    Simulation.writeResults(self)
            
            Simulation.updateTime(self)

            if self.t >= self.tfin:
                Simulation.stop(self)