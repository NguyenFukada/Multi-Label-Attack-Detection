#!/bin/bash
for i in {1..2000}
do
    echo "Collecting flow on switch br0 turn $i"
    # extract essential data from raw data
    sudo ovs-ofctl -O OpenFlow13 dump-flows br0 > dataTCP/rawtcp.txt
    grep "tcp" data/raw.txt > dataTCP/flowentries.csv

    ipsrc=$(awk -F "," '{split($14,c,"="); print c[2]","}' dataTCP/flowentries.csv)    #14 cho l3
    ipdst=$(awk -F "," '{split($15,d,"="); print d[2]","}' dataTCP/flowentries.csv)
    ethsrc=$(awk -F "," '{split($12,e,"="); print e[2]","}' dataTCP/flowentries.csv)   
    ethdst=$(awk -F "," '{split($13,f,"="); print f[2]","}' dataTCP/flowentries.csv)   

    # ipSpectable = {}
    # ipSpectable[ethsrc] = ipsrc
    # ipSpectable[ethdst] = ipdst

    if test -z "$ipsrc" || test -z "$ipdst" 
    then
        state=0
    else
        
        echo "$ipsrc" > dataTCP/ipsrc.csv
        echo "$ipdst" > dataTCP/ipdst.csv
        echo "$ethsrc" > dataTCP/ethsrc.csv
        echo "$ethdst" > dataTCP/ethdst.csv
        
    fi
    sleep 1

done