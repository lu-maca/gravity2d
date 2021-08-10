import sys
sys.path.append('C:\\Users\\Luca\\Desktop\\progetti\\fisica1\\gravity')
from utils import solver

def main():
    
    sim = solver.Simulation()
    sim.run()

if __name__ == "__main__":
    main()