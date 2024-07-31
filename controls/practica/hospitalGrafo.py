from controls.tda.graph.graphLabelNoManaged import GraphLabelNoManaged
from controls.practica.hospitalControl import HospitalControl
from controls.practica.distancia import Distancia
import os, re

class HospitalGrafo:
    def __init__(self):
        self.__grafo = None
        self.__ndao = HospitalControl()
        self.__dirPhysical = "static/d3/grafo.js"

    @property
    def _grafo(self):
        if self.__grafo == None:
            self.create_graph()
        return self.__grafo

    @_grafo.setter
    def _grafo(self, value):
        self.__grafo = value
    
    def create_graph(self,origen = None, destino = None):
        if os.path.exists(self.__dirPhysical):
            list = self.__ndao._list()
            if list._length  > 0:
                
                self.__grafo = GraphLabelNoManaged(list._length)
                arr = list.toArray
                for i in range(0, len(arr)):
                    self.__grafo.label_vertex(i, arr[i]._nombre)
                    
                with open(self.__dirPhysical, 'r') as file:
                    grafo_old = file.readlines()
                    
                    for line in grafo_old:
                        if "from:" in line:
                            line = line.strip()
                            o = re.search(r'from:\s*(\d+)', line)
                            d = re.search(r'to:\s*(\d+)', line)
                            w = re.search(r'label:"([\d.]+)"', line)
                            nc = HospitalControl()
                            hospitalOrigen = nc._list().binary_search_models(int(o.group(1)), "_id")
                            hospitalDestino = nc._list().binary_search_models(int(d.group(1)), "_id")
                            self.__grafo.insert_edges_weight_E(hospitalOrigen._nombre, hospitalDestino._nombre, float(w.group(1)))
                            
                if origen != None and destino != None:
                    peso = Distancia().calcularDistancia(origen._longitud, origen._latitud, destino._longitud, destino._latitud)           
                    self.__grafo.insert_edges_weight_E(origen._nombre, destino._nombre, round(float(peso),3))
                
                
                self.__grafo.paint_graph()
                                
        else:
            list = self.__ndao._list()
            if list._length > 0:
                self.__grafo = GraphLabelNoManaged(list._length)
                arr = list.toArray
                for i in range(0, len(arr)):
                    self.__grafo.label_vertex(i, arr[i]._nombre)
                self.__grafo.paint_graph()


    