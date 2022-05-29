import sys
sys.path.append('.')
from utils import solver

def main():
    sim = solver.Simulation()
    sim.run()

if __name__ == "__main__":
    main()