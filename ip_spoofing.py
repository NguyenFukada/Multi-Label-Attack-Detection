#!/usr/bin/python
from random import randrange
from sys import exit, stdin, argv
import subprocess
def generateSourceIP():
    not_valid = [10, 127, 254, 255, 1, 2, 169, 172, 192]

    first = randrange(1, 256)

    while first in not_valid:
        first = randrange(1, 256)
        #print first

    ip = ".".join([str(first), str(randrange(1,256)), str(randrange(1,256)), str(randrange(1,256))])
    print(ip)
    return ip

def startIPSpoofing (host):
    for i in range(1, 10):
        for j in range(1, 10):
            subprocess.run(["sudo", "nping", "--tcp", "-S", generateSourceIP(), "10.30.0.%d" % (j+i)])
            #host.cmd ("nping --tcp -S 10.10.0.%d 10.30.0.%d" % (5 + i, j))

def ipspoof_launch (doSpoof=False,ip_source=None):
    if doSpoof:
        startIPSpoofing (ip_source)

if __name__ == "__main__":
    doSpoof = False
    ip_source = generateSourceIP()
    if "spoof" in argv:
        doSpoof=True
    ipspoof_launch (doSpoof, ip_source)