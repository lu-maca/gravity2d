import os
from os import listdir
import sys
sys.path.append('..')
from physics import particles as ptc
import utils.vectors as vec


def deleteFiles():
    my_path = 'RESULTS\\POS\\'
    for file_name in listdir(my_path):
        if file_name.endswith('.txt'):
            os.remove(my_path + file_name)

    my_path = 'RESULTS\\VEL\\'
    for file_name in listdir(my_path):
        if file_name.endswith('.txt'):
            os.remove(my_path + file_name)

class inputFile:
    def __init__(self,filename):
        self.dir_name = filename
    
    def readFile(self,simulation_parameters):
        file = open(self.dir_name, 'r')
        num_meth = False
        particle_line = False
        full = False
        line = file.readline()
        while True:
            if line == '--\n': # line separator 
                num_meth = False
                particle_line = False
                line = file.readline()
            elif line == '$NUMERICAL_METHOD\n' or num_meth == True:
                num_meth = True
                newline = file.readline()
                splitted_line = newline.split()
                if splitted_line[0] == 'dt': 
                    simulation_parameters.dt = float(splitted_line[2])
                elif splitted_line[0] == 'tfin':
                    simulation_parameters.tfin = float(splitted_line[2])
                elif splitted_line[0] == 'integrator':
                    simulation_parameters.integrator = splitted_line[2]
                elif splitted_line[0] == 'printfreq':
                    simulation_parameters.printFreq = int(splitted_line[2])
                elif splitted_line[0] == 'plot':
                    simulation_parameters.show = True 
                else: 
                    num_meth = False
                    line = file.readline()
            elif line == '$PARTICLE\n' or particle_line == True:
                particle_line = True
                newline = file.readline()
                splitted_line = newline.split()
                if splitted_line[0] == 'mass':
                    mass = float(splitted_line[2])
                elif splitted_line[0] == 'charge':
                    charge = float(splitted_line[2])
                elif splitted_line[0] == 'position':
                    position = vec.Vector2D(float(splitted_line[2]), float(splitted_line[3]))
                elif splitted_line[0] == 'velocity':
                    velocity = vec.Vector2D(float(splitted_line[2]), float(splitted_line[3]))
                elif splitted_line[0] == 'acceleration':
                    acceleration = vec.Vector2D(float(splitted_line[2]), float(splitted_line[3]))
                elif splitted_line[0] == 'color':
                    color = (int(splitted_line[2]), int(splitted_line[3]), int(splitted_line[4]))
                    full = True
                if full:
                    simulation_parameters.particleList.append(ptc.Particle(mass,charge,position,velocity,acceleration, color))
                    full = False
                    line = file.readline()
                    particle_line = False
            elif not line:
                break
        file.close()
        
        



    
