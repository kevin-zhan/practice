from socket import *
serverName = "127.0.0.1"
serverPort = 5161
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input("Input lowercase sentence:\n")
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print "From server: ", modifiedSentence
clientSocket.close()
