import socket
import time
import numpy as np
import classifier
import rtmidi_python as rtmidi



UDP_IP = "0.0.0.0"
UDP_PORT = 5050
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

EPISILION = .2
THETA = .01
GAMMA = 25

G = [0x90,67,112]
A = [0x90,69,112]
B = [0x90,71,112]
D = [0x90,74,112]
C = [0x90,72,112]


LOOKUP = { 
	1 : "Checkmark", 
	2 : "Square (Clockwise) " , 
	3 : "Right",
	4 : "Left",
	5 : "Up",
	6 : "Down",
	7 : "Clockwise Circle",
	8 : "Counter Circle"
}

NOTES_LOOKUP = { 
	3 : G,
	5 : C,
	6 : A,
	7 : B,
	8 : D
}

classy = classifier.train()
sock.settimeout(.5)
def handle_data(data,log):
	float_dat = map(lambda x: float(x), data.split(","))
	return [float_dat[0],float_dat[1],-float_dat[2]]

log_data = False
data_stream_x = []
data_stream_y = []
data_stream_z = []
count_less_than_theta = 0
print "SERVER IS LISTENING"

midiout = rtmidi.MidiOut()
midiout.open_virtual_port("test1")
while True:


	try:
		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		out = handle_data(data,log_data)

		data_stream_x.append(out[0])
		data_stream_y.append(out[1])
		data_stream_z.append(out[2])
	except:
		if len(data_stream_x) > 20:
			val = classy(data_stream_x,data_stream_y,data_stream_z)
			# print LOOKUP[val]
			if val in NOTES_LOOKUP:
				print "NOTE: " + str(val)
				midiout.send_message(NOTES_LOOKUP[val])
			data_stream_x = []
			data_stream_y = []
			data_stream_z = []



	time.sleep(.0001)