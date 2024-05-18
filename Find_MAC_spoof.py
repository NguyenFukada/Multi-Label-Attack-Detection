import numpy as np
import csv
import pandas as pd
import pickle
import subprocess

HOME = '/home/loghorizon'
outfile = HOME+ '/Multi-Label-Attacks-Detection/Mac_Spoof.csv'
def load_previous_data():
    try:
        with open('MacToIpDictionary.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:   
        return {}

def save_current_data(data):
    with open('MacToIpDictionary.pkl', 'wb') as f:
        pickle.dump(data, f)

MacToIpDictionary = {}

def main():
    global MacToIpDictionary
    try:
     MacToIpDictionary = load_previous_data()
     with open('dataTCP/ipsrc.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader = list(reader)
        #MacToIpDictionary[reader[-2][1]] = reader[-2][0]
        if MacToIpDictionary.get(reader[-2][1]) is None:
            MacToIpDictionary[reader[-2][1]] = reader[-2][0]
        elif (MacToIpDictionary[reader[-2][1]] != reader[-2][0]):
            for i in range(1,6):
                if reader[-2][0] != f'10.{i}0.0.254':
                      print("SPOOF")
                      with open(outfile, 'a') as f:
                       f.write(f"{reader[-2][0]},{reader[-2][1]}\n")
                    

        if MacToIpDictionary.get(reader[-1][1]) is None:
            MacToIpDictionary[reader[-1][1]] = reader[-1][0]
        elif (MacToIpDictionary[reader[-1][1]] != reader[-1][0]):
            for i in range(1,6):
                if reader[-1][0] != f'10.{i}0.0.254':
                    print("SPOOF")
                    with open(outfile, 'a') as f: 
                       f.write(f"{reader[-1][0]},{[reader[-1][1]]}\n")
                    
        print(MacToIpDictionary)
    except:
       pass
       # or pass
    save_current_data(MacToIpDictionary)
    
    
if __name__ == "__main__":
    main()