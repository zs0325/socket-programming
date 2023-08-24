
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
#bind a socket to some port on the server
serverSocket.bind(("",serverPort))
serverSocket.listen(5)
print ("The server is ready to receive")
def dijkstra(graph, start, end):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    visited = set()
    prev = {node:None for node in graph}

    while len(visited) < len(graph):
        # Find node with minimum distance that hasnt been visited
        current = None
        for node in graph:
            if node not in visited and (current is None or distances[node] < distances[current]):
                current = node
        # If we've reached the end node, go back down the path and return it
        if current == end:    
            path = []
            while current is not None:
                path.append(current)
                current = prev[current] 
            if len(path)<=1 and start!=end:
                return None       
            return path[::-1]
        # Mark the current node as visited
        visited.add(current)
        # Update the distances of the adjacent nodes
        for adj, dist in graph[current].items():
             distance = distances[current] + dist
             if distance < distances[adj]:
              distances[adj] = distance
              prev[adj] = current
graph={
  "Bellville":{"Saps Int":1,"Bellville South":1,"Philippi":2,"Maitland":1,"Parow":1,"Landsdowne":2,"Rondebosch":2,
    "Kuils River":1,"Bishop Lavis":1,"Cape Town Central":2,"Table Bay Harbour":2,"Delft":1,"Mowbray":2,"Ravensmead":1,
    "Goodwood":1,"Port Of Entry":2,"Kensington":2,"Athlone":2,"Woodstock":2,"Belhar":1,"Manenburg":2,"Claremont":2,
    "Brackenfell":1,"Lingelethu West":1,"Gugulethu":5,"Langa":1,"Dieprivier":2,"Grassy Park":2,"Kirstenhof":5},
  "Nyanga":{"Bellville":4,"Athlone":1},
  "Saps Int":{"Philippi":1},
  "Bellville South":{"Manenburg":2},
  "Philippi":{},"Maitland":{},"Parow":{},"Landsdowne":{},
  "Rondebosch":{"Manenburg":2},
  "Kuils River":{"Landsdowne":3,"Dieprivier":1},
  "Wynberg":{"Table Bay Harbour":1},
  "Sea Point":{"Bellville":2},
  "Bishop Lavis":{"Mowbray":1,"Port Of Entry":2,"Table Bay Harbour":2},
  "Cape Town Central":{"Port Of Entry":1},
  "Table Bay Harbour":{"Mfuleni":2},
  "Delft":{"Maitland":1,"Durbanville":1,"Mfuleni":1,"Gugulethu":2},
  "Mowbray":{},"Ravensmead":{},
  "Goodwood":{"Gugulethu":1},
  "Elsies Rivier":{"Bellville":1,"Ravensmead":1,"Sea Point":1,"Woodstock":1},
  "Port Of Entry":{},"Kensington":{},"Athlone":{},"Woodstock":{},
  "Pinelands":{"Bellville":1,"Port Of Entry":2},
  "Belhar":{"Durbanville":1,"Gugulethu":1},
  "Manenburg":{"Athlone":1,"Claremont":1},"Claremont":{},
  "Gugulethu":{"Parow":1,"Landsdowne":1},
  "Durbanville":{},
  "Brackenfell":{"Athlone":3},
  "Langa":{"Kensington":1,"Lingelethu West":1,"Harare":4},
  "Mitchells Plain":{"Delft":1,"Bellville":2,"Kleinvlei":1},
  "Khayelitsha":{"Delft":2,"Bellville":3},
  "Mfuleni":{},"Lingelethu West":{},
  "Dieprivier":{"Steenburg":6},
  "Kleinvlei":{"Lingelethu West":1},
  "Harare":{"Landsdowne":4},
  "Grassy Park":{"Landsdowne":1,"Steenburg":1,"Kirstenhof":1},
  "Steenburg":{},"Kirstenhof":{}
}
while True:
 connectionSocket, addr = serverSocket.accept()
 source = connectionSocket.recv(1024).decode()
 destination = connectionSocket.recv(1024).decode()
 distance=dijkstra(graph,source,destination)
 connectionSocket.send(str(distance).encode())
 connectionSocket.close()