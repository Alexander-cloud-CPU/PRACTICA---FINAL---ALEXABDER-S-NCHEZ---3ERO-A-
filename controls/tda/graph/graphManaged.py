from controls.tda.graph.graph import Graph
from controls.tda.linked.linkedList import Linked_List
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.adjacent import Adjacent
from math import nan
import heapq
class GraphManaged(Graph):
    def __init__(self, num_vert) -> None:
        super().__init__()
        self.__numVert = num_vert
        self.__numEdg = 0
        self.__listAdjacent = []
        for i in range(0, num_vert):
            self.__listAdjacent.append(Linked_List())

    def setNumEdg(self, number):
        self.__numEdg = number  

    @property
    def num_vertex(self):
        return self.__numVert
    
    @property
    def num_edges(self):
        return self.__numEdg
    
    def exits_edges(self,v1, v2): 
        band = False
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            listAdj = self.__listAdjacent[v1]
            if not listAdj.isEmpty:
                arraAdj = listAdj.toArray
                for i in range(0, listAdj._length):
                    adj = arraAdj[i]
                    if adj._destination == v2:
                        band = True
                        break         
        else:
            raise ArrayPositionException("Delimite out - 1")
        return band
    
    def weight_edges(self, v1, v2):
        weight = None
        if self.exits_edges(v1, v2):
            if v1 <= self.num_vertex and v2 <= self.num_vertex:
                listAdj = self.__listAdjacent[v1]
                if not listAdj.isEmpty:
                    arraAdj = listAdj.toArray
                    for i in range(0, listAdj._length):             #QUE NO ESTE REDONDANDO
                        adj = arraAdj[i]
                        if adj._destination == v2:
                            weight = adj._weight
                            break         
            else:
                raise ArrayPositionException("Delimite out - 2")
        return weight
                
    def insert_edges_weight(self, v1, v2, weight):
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            if not self.exits_edges(v1, v2):
               self.__numEdg += 1
               adj = Adjacent()
               adj._destination = v2
               adj._weight = weight
               self.__listAdjacent[v1].add(adj, self.__listAdjacent[v1]._length)
               self.paint_graph()
        else:
            raise ArrayPositionException("Delimite out - 3")
               
    def insert_edges(self, v1, v2):
        self.insert_edges_weight(v1, v2, nan)
        
    def adjacent(self, v1):
        return self.__listAdjacent[v1]
    
    def floyd_warshall(self, origen, destino):
        dist = [[float('inf')] * self.num_vertex for _ in range(self.num_vertex)]
        pred = [[None] * self.num_vertex for _ in range(self.num_vertex)]
        camino = "ruta: "
        
        for i in range(0,len(pred)):
            for j in range(0,len(pred)):
                camino += str(pred[i][j]) + " --> "
        
        for i in range(self.num_vertex):
            dist[i][i] = 0

        for v1 in range(self.num_vertex):
            for adj in self.adjacent(v1).toArray:
                v2 = adj._destination
                dist[v1][v2] = adj._weight
                pred[v1][v2] = v1

        for k in range(self.num_vertex):
            for i in range(self.num_vertex):
                for j in range(self.num_vertex):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        pred[i][j] = pred[k][j]

        camino = self.obtener_camino(pred, origen, destino)
        ruta = "Camino: "
        for i in range(0, len(camino)):
           etiqueta = self.getLabel(camino[i])
           ruta += etiqueta + " --> " 

        return ruta, dist
    
    def obtener_camino(self, pred, start, end):
        if pred[start][end] is None:
            return None  # No hay camino
        camino = []
        while end is not None:
            camino.insert(0, end)
            end = pred[start][end]
        return camino

    def reconstruct_path_fw(self, start, end, pred):
        path = []
        if pred[start][end] is None:
            return path
        while end is not None:
            path.insert(0, end)
            end = pred[start][end]
        return path
    
    def dijkstra(self, start_vertex):
        dist = [float('inf')] * self.num_vertex
        dist[start_vertex] = 0
        prev = [None] * self.num_vertex
        pq = [(0, start_vertex)]

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

            if current_dist > dist[current_vertex]:
                continue

            for adj in self.adjacent(current_vertex).toArray:
                neighbor = adj._destination
                weight = adj._weight
                distance = current_dist + weight

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    prev[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

        return dist, prev

    def reconstruct_path_dijkstra(self, start, end, prev):
        path = []
        while end is not None:
            path.insert(0, end)
            end = prev[end]
        return path if path[0] == start else []