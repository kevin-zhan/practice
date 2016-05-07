from socket import *
serverPort = 5161
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(100)

print 'The server is ready to receive'
while 1:
	conncetionSocket,addr = serverSocket.accept()
	sentence = conncetionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	conncetionSocket.send(capitalizedSentence)

	conncetionSocket.close()


