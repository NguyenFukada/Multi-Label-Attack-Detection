import numpy as np
import csv
import pandas as pd
import pickle

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
            main_string = '.0.254'
            index = main_string.find(reader[-2][0])
            if (index == -1):
                print("Spoof: ", reader[-2][1])

        if MacToIpDictionary.get(reader[-1][1]) is None:
            MacToIpDictionary[reader[-1][1]] = reader[-1][0]
        elif (MacToIpDictionary[reader[-1][1]] != reader[-1][0]):
            main_string = '.0.254'
            index = main_string.find(reader[-1][0])
            if (index == -1):
             print("Spoof: ", reader[-1][1])
        
        print(MacToIpDictionary)
    #     for key, value in MacToIpDictionary.items():
    # #print value
    #         if isinstance(value, str):
    #             print("len: ",)
       ### Do Some Stuff
    except:
       pass
       # or pass
    save_current_data(MacToIpDictionary)
    
    # Convert the DataFrame to a Dictionary
   

    # ethsrc_tcp = read_file('dataTCP/ethsrc.csv')
    # print(ethsrc_tcp)
    # ipsrc_tcp = read_file('dataTCP/ipsrc.csv')
    # ethdst_tcp = read_file('dataTCP/ethdst.csv')
    # ipdst_tcp = read_file('dataTCP/ipdst.csv')
    
    # ethdst_tcp = np.genfromtxt('dataTCP/ethdst.csv', delimiter=",",dtype=None, encoding=None)
    # ethsrc_tcp = np.genfromtxt('dataTCP/ethsrc.csv', delimiter=",",dtype=None, encoding=None)
    # ipsrc_tcp = np.genfromtxt('dataTCP/ipsrc.csv', delimiter=",",dtype=None, encoding=None)
    # ipdst_tcp = np.genfromtxt('dataTCP/ipdst.csv', delimiter=",",dtype=None, encoding=None)
    # ethdst_collect = ethdst_tcp[:, 0]
    # ethsrc_collect = ethsrc_tcp[:, 0]
    # ipsrc_collect = ipsrc_tcp[:, 0]
    # ipdst_collect = ipdst_tcp[:, 0]

    # for i in range (0, len(ethsrc_collect)):
    #     # print("len: ", MacToIpDictionary)
    #     #if ethsrc_collect[i] not in MacToIpDictionary:
    #     if MacToIpDictionary.get(ethsrc_collect[i]) is None:
    #        MacToIpDictionary[ethsrc_collect[i]] = ipsrc_collect[i]
    #        print("Mac: ", ethsrc_collect[i])
    #        print("IP: ",ipsrc_collect[i])
    #     elif MacToIpDictionary[ethsrc_collect[i]] == ipsrc_collect[i]:
    #         print("FOUND IT")
    #     else:
    #         MacToIpDictionary[ethsrc_collect[i]] = ipsrc_collect[i]
    #     if (len(MacToIpDictionary[ethsrc_collect[i]]) > 2):
    #         print("Spoof:",MacToIpDictionary[ethsrc_collect[i]])
    #         print("-------")

    
    # open file for writing, "w" is writing
    #w = csv.writer(open("output.csv", "w"))

# loop over dictionary keys and values
    # for data in MacToIpDictionary.items():
    #     w.writerow(data)
       

    

    # if ethdst_tcp not in MacToIpDictionary:
    #     MacToIpDictionary[ethdst_tcp] = ipdst_tcp
    # elif MacToIpDictionary[ethdst_tcp] == ipdst_tcp:
    #     pass
    # else:
    #     MacToIpDictionary[ethdst_tcp].extend(ipdst_tcp)
    # if (len(custom_intervlan.MacToIpDictionary[ethdst_tcp]) > 2):
    #     Mac = [ethdst_tcp]
    # with open('dataTCP/Mac_spoof.csv', 'w') as f:
    #  cursor = csv.writer(f, delimiter=",")
    #  cursor.writerow(ethdst_tcp)
    # f.close()
if __name__ == "__main__":
    main()