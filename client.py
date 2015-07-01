import socket
import time
UDP_IP = "127.0.0.1"
UDP_PORT = 5050
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
for i in range(10000):
	if i %100 == 0:
		print i
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	time.sleep(.01)
