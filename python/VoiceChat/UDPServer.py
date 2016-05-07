from socket import *
serverPort = 4170
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print "The server is ready to recive data"
i = 0
while 1:
	print i
	i += 1
	message,clientAddress = serverSocket.recvfrom(2048)
	print message
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage,clientAddress)
