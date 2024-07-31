from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List

import json
import os

T = TypeVar("T")
class DaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.lista = Linked_List()
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/data/"

        
    def _list(self):
        if os.path.isfile(self.URL + self.file):
            f = open(self.URL + self.file, "r")
            datos = json.load(f)
            self.lista.clear
            for data in datos:
                a = self.atype.deserializar(data)
                self.lista.add(a, self.lista._length)
        return self.lista
    
    def __transform__(self):
        aux = "["
        for i in range(0, self.lista._length):
            if i < self.lista._length - 1:
                aux += str(json.dumps(self.lista.get(i).serializable)) + ","
            else:
                aux += str(json.dumps(self.lista.get(i).serializable))
        aux += "]"
        return aux
    
    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._length):
            aux.append(self.lista.get(i).serializable)
        return aux
    
    def to_dict_lista(self, lista):
        aux = []
        for i in range(0, self.lista._length):
            aux.append(lista.get(i).serializable)
        return aux
    
    def paint_graph(self):
        self._list()
        for i in range(0, self.lista._length):
            print(self.lista.get(i).serializable)   

    
    def _get(self, id):
        list = self._list()
        array = list.toArray()
        for i in range(0, len(array)):
            if array[i]._id == id:
                return array[i]
        return None
    
    def _save(self, data: T) -> T:
        print(data)
        self._list()
        self.lista.add(data, self.lista._length)
        data._id = self.lista._length
        a = open(self.URL + self.file, "w")
        a.write(self.__transform__())
        a.close()

    def _merge(self, data: T, pos) -> T:
        self._list()
        self.lista.edit(data, pos)
        a = open(self.URL + self.file, "w")
        a.write(self.__transform__())
        a.close()

    def _delete(self, pos) -> T:
        self._list()
        self.lista.delete(pos)
        a = open(self.URL + self.file, "w")
        a.write(self.__transform__())
        a.close()
    # def _save_json(self, data):
    #     name = self.atype.__name__
    #     with open("../Files/"+ name + ".json", "w") as outfile:
    #         json.dump(data, outfile, indent=4)

    