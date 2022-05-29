import sys
sys.path.append('..')
from utils import vectors

# G = 6.67e-11
G = 10
def gravityForce(firstMass,secondMass,firstPosition,secondPosition):
    # force applied on 'secondMass' by 'firstMass'
    r = vectors.Vector2D.distance_to(secondPosition,firstPosition)
    f = -G*firstMass*secondMass/r**2 * (secondPosition - firstPosition)/r
    return f

