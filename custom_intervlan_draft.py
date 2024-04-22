from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import random
from multiprocessing import Process
import socket
from _thread import *
import threading


host_ips = []
# List chứa các quy trình
processes = []
hosts = []
switches = []


def hostToSwitch(net, switch, host):
    net.addLink(switch, host)
def switchToSwitch(net, switch1, switch2):
    net.addLink(switch1, switch2)

def setup_gateway(net, host_name, gateway):
    print(f"Setting up gateway for {host_name} with gateway {gateway}")
    Process(target=net.get(host_name).cmd, args=(
        f'route add default gw {gateway}',)).start()

print_lock = threading.Lock()
def threaded(c):
    while True:
 
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')      
            # lock released on exit
            print_lock.release()
            break
        # reverse the given string from client
        data = data[::-1]
        # send back reversed string to client
        c.send(data)
    # connection closed
    c.close()

def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port

def sever(host):
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
    
    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()
 
        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
 
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()
    

def client(host):
    port = 12345
 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    # connect to server on local computer
    s.connect(('127.0.0.1',port))
 
    # message you send to server
    message = "shaurya says geeksforgeeks"
    while True:
 
        # message sent to server
        s.send(message.encode('ascii'))
 
        # message received from server
        data = s.recv(1024)
 
        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :',str(data.decode('ascii')))
    # close the connection
        s.close()
 
def start_traffic(host_source, host_destination):
    sever(host_source)
    client(host_destination)

def myNetwork():
    net = Mininet(topo=None,
                  build=False)

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='127.0.0.1',
                           protocol='tcp',
                           port=6633)

    info('*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info('*** Add hosts\n')
    for i in range(1, 49):
        if i >= 1 and i <= 8:
            ip_address = f'10.10.0.{i}'
            gateway = '10.10.0.254'
        elif i >= 9 and i <= 16:
            ip_address = f'10.20.0.{i}'
            gateway = '10.20.0.254'
        elif i >= 17 and i <= 24:
            ip_address = f'10.30.0.{i}'
            gateway = '10.30.0.254'
        elif i >= 25 and i <= 32:
            ip_address = f'10.40.0.{i}'
            gateway = '10.40.0.254'
        elif i >= 33 and i <= 40:
            ip_address = f'10.50.0.{i}'
            gateway = '10.50.0.254'
        elif i >= 41 and i <= 48:
            ip_address = f'10.60.0.{i}'
            gateway = '10.60.0.254'

        host_ips.append(ip_address)
        host = net.addHost(f'h{i}', cls=Host, ip=f'{ip_address}/24')
        # hosts.append(host)

        # Liên kết máy chủ với switch
        hostToSwitch(net, s1, host)

    info('*** Add links\n')
    # connect switch 1 to other switches in switch array

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')

    net.get('s1').start([c0])
    # print(hosts)

    info('*** Post configure switches and hosts\n')
    p_s1 = Process(target=net.get('s1').cmd, args=(
        'source del_port.sh',))
    # p1 = Process(target=net.get('h1').cmd, args=('ettercap -T -i h1-eth0 -M ARP /10.0.0.3// /10.0.0.7//',))
    p_s1.start()
    info('*** Configuring gateway for hosts\n')
    for i in range(1, 49):
        if i >= 1 and i <= 8:
            gateway = '10.10.0.254'
        elif i >= 9 and i <= 16:
            gateway = '10.20.0.254'
        elif i >= 17 and i <= 24:
            gateway = '10.30.0.254'
        elif i >= 25 and i <= 32:
            gateway = '10.40.0.254'
        elif i >= 33 and i <= 40:
            gateway = '10.50.0.254'
        elif i >= 41 and i <= 48:
            gateway = '10.60.0.254'

        setup_gateway(net, f'h{i}', gateway)
    info('*** Running Traffic\n')
    
    hosts_destination = []
    for i in range(1, 49):
        host_source = random.choice(host_ips)
        # j is random integer from 10 to 60 withh step 10 and not equal to 30 and 40
        j = random.choice([10, 20, 50, 60])
        hosts_destination.append(f"10.{j}.0.{i}")
        start_traffic(host_source,hosts_destination)
    info('*** Done\n')
    CLI(net)

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
    # kill all the processes if the CLI is exited
    for p in processes:
        p.terminate()