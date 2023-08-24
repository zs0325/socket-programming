

from socket import *
serverName = "127.1.1.0"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
file1=open("shortestPath.txt","a")
start= input("Insert source station corresponding with any of the following:\nBellville,Nyanga,SAPS-Int,Bellville South,Rondebosch,Kuils River,Wynberg,Sea Point,Bishop Lavis,Cape Town Central, Table Bay Harbour,Delft,Goodwood,Elsies Rivier,Pinelands,Belhar,Manenburg,Gugulethu,Brackenfell,Langa,Mitchells Plain,Khayelitsha,Dieprivier,Kleinvlei,Harare,Grassy Park\n").title()
end=input("Insert destination:").title()
clientSocket.send(start.encode())
clientSocket.send(end.encode())
modifiedLine = clientSocket.recv(1024)
file1.write(f"Shortest path from {start} to {end}: "+modifiedLine.decode()+"\n")
print("\n--------------------------------------")
clientSocket.close()