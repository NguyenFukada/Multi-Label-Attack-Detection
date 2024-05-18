from subprocess import call
import random
import time
import subprocess
from random import randrange

def main():
    for i in range(1,10): 
        subprocess.run(["sudo", "nping", "--tcp","10.20.0.9","10.20.0.10"]) 
        subprocess.run(["sudo", "nping", "--tcp","10.20.0.10","10.20.0.11"])
        subprocess.run(["sudo", "nping", "--tcp","-c 4","10.20.0.11","10.20.0.12"])
        subprocess.run(["sudo", "nping", "--tcp","-c 4","10.20.0.12","10.20.0.13"])
        subprocess.run(["sudo", "nping", "--tcp","10.20.0.13","10.20.0.14"])
        subprocess.run(["sudo", "nping", "--tcp","10.20.0.14","10.20.0.15"])
        subprocess.run(["sudo", "nping", "--tcp","-c 4","10.60.0.41","10.60.0.42"])
        subprocess.run(["sudo", "nping", "--tcp","-c 4","10.60.0.44","10.60.0.43"])
        subprocess.run(["sudo", "nping", "--tcp","10.60.0.45","10.60.0.46"])
        subprocess.run(["sudo", "nping", "--tcp","10.60.0.46","10.60.0.47"]) 
        subprocess.run(["sudo", "nping", "--tcp","10.50.0.33","10.50.0.34"]) 
        subprocess.run(["sudo", "nping", "--tcp","-c 4","10.50.0.34","10.50.0.35"])
        subprocess.run(["sudo", "nping", "--tcp","10.50.0.35","10.50.0.36"])
        subprocess.run(["sudo", "nping", "--tcp","-c 4","10.50.0.36","10.50.0.37"])
        subprocess.run(["sudo", "nping", "--tcp","10.50.0.37","10.50.0.38"])
        subprocess.run(["sudo", "nping", "--tcp","-c 4","10.50.0.38","10.50.0.39"])   
    
if __name__ == "__main__":
    main()