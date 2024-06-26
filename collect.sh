#!/bin/bash


for i in {1..2000}
do
    echo "Collecting flow on switch br0 turn $i"
    # extract essential data from raw data
    # sudo ovs-ofctl -O OpenFlow13 dump-flows s"$j" > data/raw.txt
    sudo ovs-ofctl -O OpenFlow13 dump-flows br0 > data/raw.txt
    sudo ovs-ofctl -O OpenFlow13 dump-flows br0 > dataTCP/rawtcp.txt
    # sudo ovs-ofctl dump-flows tcp:10.20.0.1:6633 > data/raw.txt #uncomment to run in real environment
    
    grep "nw_src" data/raw.txt > data/flowentries.csv
    grep "arp_op=1" data/raw.txt > ARP_data/ARP_Request_flowentries.csv
    grep "arp_op=2" data/raw.txt > ARP_data/ARP_Reply_flowentries.csv

    grep "tcp" dataTCP/rawtcp.txt > dataTCP/flowentries.csv

    packets=$(awk -F "," '{split($4,a,"="); print a[2]","}' data/flowentries.csv)
    bytes=$(awk -F "," '{split($5,b,"="); print b[2]","}' data/flowentries.csv)
    # ipsrc=$(awk -F "," '{split($15,c,"="); print c[2]","}' data/flowentries.csv)    #14 cho l3
    # ipdst=$(awk -F "," '{split($16,d,"="); print d[2]","}' data/flowentries.csv)    #15 cho l3

    ipsrc=$(awk -F "," '{split($14,c,"="); print c[2]","}' data/flowentries.csv)    
    ipdst=$(awk -F "," '{split($15,d,"="); print d[2]","}' data/flowentries.csv)    
    ethsrc=$(awk -F "," '{split($12,e,"="); print e[2]","}' data/flowentries.csv)   
    ethdst=$(awk -F "," '{split($13,f,"="); print f[2]","}' data/flowentries.csv)   
    eth_src_reply=$(awk -F "," '{split($12,e,"="); print e[2]","}' ARP_data/ARP_Reply_flowentries.csv)   
    ip_dst_reply=$(awk -F "," '{split($15,d,"="); print d[2]","}' ARP_data/ARP_Reply_flowentries.csv) 



    ipsrc_tcp=$(awk -F "," '{split($14,c,"="); print c[2]","}' dataTCP/flowentries.csv)    #14 cho l3
    ipdst_tcp=$(awk -F "," '{split($15,d,"="); print d[2]","}' dataTCP/flowentries.csv)
    ethsrc_tcp=$(awk -F "," '{split($12,e,"="); print e[2]","}' dataTCP/flowentries.csv)   
    ethdst_tcp=$(awk -F "," '{split($13,f,"="); print f[2]","}' dataTCP/flowentries.csv)      

    if test -z "$packets" || test -z "$bytes" || test -z "$ipsrc" || test -z "$ipdst" 
    then
        state=0
    else
        echo "$packets" > data/packets.csv
        echo "$bytes" > data/bytes.csv

        echo "$ipsrc" > data/ipsrc.csv
        echo "$ipdst" > data/ipdst.csv
        echo "$ethsrc" > data/ethsrc.csv
        echo "$ethdst" > data/ethdst.csv
        echo "$eth_src_reply" > ARP_data/eth_src_reply.csv
        echo "$ip_dst_reply" > ARP_data/ip_dst_reply.csv

        #echo "$ipsrc_tcp,$ethsrc_tcp" > dataTCP/ipsrc.csv
        echo "$ipdst_tcp" > dataTCP/ipdst.csv
        echo "$ethsrc_tcp" > dataTCP/ethsrc.csv
        echo "$ethdst_tcp" > dataTCP/ethdst.csv
        ipsrc_filtered=$(echo "$ipsrc_tcp" | grep -Ev '\b254\b')
        ethsrc_filtered=$(echo "$ethsrc_tcp" | grep -v -F -f <(echo "$ipsrc_filtered"))
        paste -d ',' <(echo "$ipsrc_tcp" | sed 's/,//g') <(echo "$ethsrc_tcp" | sed 's/,//g') >> dataTCP/ipsrc.csv
    fi
    python3 computeTuples.py
    #python3 inspector.py
    truncate -s 0 ARP_Broadcast/arp_broadcast.csv
    #truncate -s 0 Mac_Spoof.csv
    # truncate -s 0 f2.csv
    # python3.11 inspector.py
    # python3.11 inspector.py
    sleep 2.5
done