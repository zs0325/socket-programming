
from socket import *
serverName = "127.1.1.0"
serverPort = 12000
file1=open('cities.txt',encoding="utf8")
sentence= file1.readlines()
for line in sentence:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    print("Organizing City:",line)
    clientSocket.send(line.encode())
    modifiedLine = clientSocket.recv(1024)
    print ("South African City:", modifiedLine.decode(),"\n")
print("\n--------------------------------------")
clientSocket.close()