from socket import *
serverName = VivoBook4854
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = input("Enter file name")

clientSocket.sento(bytes(sentence, "utf-8"), (serverName, serverPort))
filecontents, serverAddress = clientSocket.recvfrom(2048)
print('From server:' , filecontents)
clientSocket.close()
