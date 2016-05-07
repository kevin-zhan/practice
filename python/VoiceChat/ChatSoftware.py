from socket import *
import pyaudio
import wave
import time

def open():
	serverPort = 5160
	serverSocket = socket(AF_INET,SOCK_STREAM)
	serverSocket.bind(('',serverPort))
	serverSocket.listen(1)
	print 'Software is running'
	while 1:
		conncetionSocket,addr = serverSocket.accept()
		sentence = conncetionSocket.recv(1024)
		if sentence == "RequestChat":
			conncetionSocket.send("OK")
			conncetionSocket.close
			return True
		conncetionSocket.close()	

def openAndCall():
	serverName = "127.0.0.1"
	serverPort = 5160
	clientSocket = socket(AF_INET,SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	sentence = "RequestChat"
	clientSocket.send(sentence)
	get = clientSocket.recv(1024)
	clientSocket.close()
	if get == "OK":
		return True
	return False

def sendVoice():
	#sound info
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	RECORD_SECONDS = 51
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)
	#net info
	HOST = '127.0.0.1'  # The remote host
	PORT = 4170  # The same port as used by the server
	clientSocket = socket(AF_INET,SOCK_DGRAM)

	print "Begin chatting"
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)
	    clientSocket.sendto(data,(HOST,PORT))

	print "Done chatting"

	stream.stop_stream()
	stream.close()
	p.terminate()
	clientSocket.close()
	print "Closed"


def playVoice():
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	RECORD_SECONDS = 4
	WAVE_OUTPUT_FILENAME = "server_output.wav"
	WIDTH = 2
	frames = []

	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(WIDTH),
	                channels=CHANNELS,
	                rate=RATE,
	                output=True,
	                frames_per_buffer=CHUNK)

	HOST = ''   # Symbolic name meaning all available interfaces
	PORT = 4170    # Arbitrary non-privileged port

	serverSocket = socket(AF_INET,SOCK_DGRAM)
	serverSocket.bind(('',PORT))

	data,clientAddress = serverSocket.recvfrom(CHUNK)
	print('Connected by', clientAddress)
	i = 1
	while i < 500:
		i += 1
		print i
		stream.write(data)
		data,clientAddress = serverSocket.recvfrom(CHUNK)
		frames.append(data)

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

	stream.stop_stream()
	stream.close()
	p.terminate()
	serverSocket.close()



