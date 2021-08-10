def EulerCromer(particleList,dt):
    for p in particleList:
        p.velocity = p.getParticleVelocity() + p.getParticleAcceleration()*dt 
        p.position = p.getParticlePosition() + p.getParticleVelocity()*dt

def velocityVerlet(particleList,dt):
    for p in particleList:
        midVelocity =  p.getParticleVelocity() + 0.5*p.getParticleAcceleration()*dt
        p.position = p.getParticlePosition() + midVelocity*dt
        
