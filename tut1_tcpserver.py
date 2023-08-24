
from datetime import datetime,timedelta
from socket import *
# create the socket
# AF_INET == ipv4
# AF_INET6 == ipv6
# SOCK_STREAM == TCP
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
#bind a socket to some port on the server
serverSocket.bind(("",serverPort))
serverSocket.listen(5)
print ("The server is ready to receive")
file2= open("timediff.txt",encoding="utf8")
line= file2.readlines()
while True:
 for x in line:
     connectionSocket, addr = serverSocket.accept()
     sen = connectionSocket.recv(1024).decode()
     x=x.split(",")
     sen=sen.split(",")
     sen[1]=x[0]
     dt_instance=datetime.strptime(sen[0],'%Y-%m-%d')
     time_instance=datetime.strptime(sen[2],'%H:%M:%S')
     time=time_instance.time()   
     td=timedelta(hours=float(x[2]))
     sa_time=(time_instance+td).time()
     date=datetime.combine(dt_instance,time)
     date=(date+td).date()
     sentence=str(date)+","+sen[1]+","+str(sa_time)+","+sen[3]+","+sen[4]
     connectionSocket.send(sentence.encode())
     connectionSocket.close()

