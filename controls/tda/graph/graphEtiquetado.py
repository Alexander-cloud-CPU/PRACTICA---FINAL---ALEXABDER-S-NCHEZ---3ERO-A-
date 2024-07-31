from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.graphManaged import GraphManaged
import os

class GrafoEtiquetado(GraphManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.vertices = {}
    
    def agregar_vertice(self, id_vertice, etiqueta):
        if id_vertice not in self.vertices:
            self.vertices[id_vertice] = etiqueta
        else:
            raise ArrayPositionException("El vertice ya existe")
        
    def agregar_arista(self, origen, destino, peso=1):
        if origen in self.vertices and destino in self.vertices:
            self.insert_edges_weight(origen, destino, peso)
        else:
            raise ArrayPositionException("Uno o dos vertices no existen")

    def mostrar_grafo(self):
        for vertice in self.vertices:
            print(f"Vértice {vertice} - Etiqueta: {self.vertices[vertice]}")
            adyacentes = self.adjacent(vertice)
            if not adyacentes.isEmpty:
                for i in range(0, adyacentes._length):
                    arista = adyacentes.get(i)
                    print(f"  Arista hacia {arista._destination} con peso {arista._weight}")
    
    def paint_graph_etiquetado(self):
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + "/static/d3/grafo.js"
        js = 'var nodes = new vis.DataSet(['
        # vertices
        for vertice, etiqueta in self.vertices.items():
            js += f'{{id: {vertice}, label:"{etiqueta}"}},\n'
        js += ']);\n'
        # edges
        js += 'var edges = new vis.DataSet(['
        for origen in self.vertices:
            adyacentes = self.adjacent(origen)
            if not adyacentes.isEmpty:
                for i in range(0, adyacentes._length):
                    arista = adyacentes.get(i)
                    js += f'{{from: {origen}, to: {arista._destination}, label:"{arista._weight}"}},\n'
        js += ']);\n'
        js += 'var container = document.getElementById("mynetwork"); var data = {nodes: nodes, edges: edges,};var options = {};var network = new vis.Network(container, data, options);'
        with open(url, 'w') as f:
            f.write(js)