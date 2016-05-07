from socket import *
serverName = "127.0.0.1"
serverPort = 4170
clientSocket = socket(AF_INET,SOCK_DGRAM)
while 1:
	message = raw_input("input lowcase sentence:\n")
	if message == "1":
		break
	clientSocket.sendto(message,(serverName,serverPort))
	modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
	print modifiedMessage
clientSocket.close()
