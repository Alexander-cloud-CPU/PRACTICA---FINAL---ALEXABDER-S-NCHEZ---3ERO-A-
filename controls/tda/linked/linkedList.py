from controls.tda.linked.node import Node
from controls.exception.linkedEmpty import LinkedEmpty
from controls.exception.arrayPositionException import ArrayPositionException
#from controls.tdaArray import TDAArray
from numbers import Number
from controls.tda.linked.burbuja import Burbuja
from controls.tda.linked.insercion import Insercion
from controls.tda.linked.quicksort import QuickSort
from controls.tda.linked.mergesort import MergeSort
from controls.tda.linked.shellsort import ShellSort

from datetime import datetime

class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0
    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node            
        else:
            headOld = self.__head
            node = Node(data, headOld)
            self.__head = node
        
        self.__length += 1

    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)            
        else:            
            node = Node(data)
            self.__last._next = node
            self.__last = node        
            self.__length += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:            
            self.__addLast__(data)
        else:            
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1
    
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:            
            self.__last._data = data
        else:                        
            node = self.getNode(pos)            
            node._data = data
    
    def deleteFirst(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self.__length == 1:
                self.__last = None
            self._length = self._length - 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__last._data
            aux = self.getNode(self._length - 2)

            #self.__head = aux
            if aux == None:
                self.__last = None
                if self.__length == 2:
                    self.__last = self.__head
                else:
                    self.__head = None
            else:
                self.__last = None
                self.__last = aux
                self.__last._next = None
            self._length = self._length - 1
            return element
    
    def delete(self, pos = 0):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Position out range")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == (self.__length - 1):
            return self.deleteLast()
        else:
            preview = self.getNode(pos - 1)
            actually = self.getNode(pos)
            element = preview._data
            next = actually._next
            actually = None
            preview._next = next
            self._length = self._length - 1
            return element

    """Obtiene el objeto nodo"""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    """Obtiene el objeto nodo"""
    def get(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__length - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data

    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data)+ "\t"
                node = node._next
        return out
    @property
    def print(self):
        node = self.__head
        data = ""    
        while node != None:
            data += str(node._data)+"    "            
            node = node._next
        print("Lista de datos")
        print(data)
    
    @property
    def toArray(self):
        array = []               
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self._length:
                array.append(node._data)
                cont += 1
                node = node._next
        return array
    
    @property
    def to_dict(self):
        data = []
        node = self.__head
        while node != None:
            data.append(node._data)
            node = node._next
        return data
    
    def serializable(self):
        data = []
        node = self.__head
        while node != None:
            data.append(node._data)
            node = node._next
        return data
    
    def deserializar(data):
        linked = Linked_List()
        for i in data:
            linked.add(i)
        return linked
    
    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])
    
    def sort(self, type = 1, method = 3):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            self.clear
            #datos primitivos
            if isinstance(array[0], Number) or isinstance(array[0], str):
                if type == 1:
                    if method == 1:
                        order = Burbuja()
                        array = order.sort_burbuja_number_ascent(array)
                    elif method == 2:
                        order = Insercion()
                        array = order.sort_primitive_ascent(array)
                    elif method == 3:
                        order = QuickSort()
                        array = order.quicksort_numbers_ascent(array, 0, len(array) - 1)
                    elif method == 4:
                        order = MergeSort()
                        array = order.mergeSort_number_ascent(array)
                    elif method == 5:
                        order = ShellSort()
                        array = order.shell_number_ascent(array)

                else:
                    if method == 1:
                        order = Burbuja()
                        array = order.sort_burbuja_number_descent(array)
                    elif method == 2:
                        order = Insercion()
                        array = order.sort_primitive_descent(array)
                    elif method == 3:
                        order = QuickSort()
                        array = order.quicksort_numbers_descent(array, 0, len(array) - 1)
                    elif method == 4:
                        order = MergeSort()
                        array = order.mergeSort_number_descent(array)
                    elif method == 5:
                        order = ShellSort()
                        array = order.shell_number_descent(array)
          
            self.toList(array)

            
    def  sort_models(self, atribute ,type = 1, method = 3):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            self.clear
            if isinstance(array[0], object): 
                if type == 1:
                    if method == 1:
                        order = Burbuja()
                        array = order.sort_burbuja_atribute_ascent(array, atribute)                  
                    elif method == 2:
                        order = Insercion()
                        array = order.sort_models_ascent(array, atribute)
                    elif method == 3:
                        order = QuickSort()
                        array = order.quicksort_models_ascent(array, 0, len(array) - 1, atribute)
                    elif method == 4:
                        order = MergeSort()
                        array = order.mergeSort_models_ascent(array, atribute)
                    elif method == 5:
                        order = ShellSort()
                        array = order.shell_models_ascent(array, atribute)
                else:
                    if method == 1:
                        order = Burbuja()
                        array = order.sort_burbuja_atribute_descent(array, atribute)
                    elif method == 2:
                        order = Insercion()
                        array = order.sort_models_descent(array, atribute)
                    elif method == 3:
                        order = QuickSort()
                        array = order.quicksort_models_descent(array, 0, len(array) - 1, atribute)
                    elif method == 4:
                        print("entro en merge descent")
                        order = MergeSort()
                        array = order.mergeSort_models_descent(array, atribute)
                    elif method == 5:
                        order = ShellSort()
                        array = order.shell_models_descent(array, atribute)
            self.toList(array)
       
      
    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            for i in range(0, len(array)):
                if array[i].lower().__contains__(data.lower()):  # < > <= >= !=  == startswith() endswith()
                    list.addNode(array[i], list._length)
        return list  
    
    
    def binary_search_number(self, data):
        self.sort()
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == data:
                return arr[mid] 
            elif arr[mid] < data:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def lineal_binary_search_number(self, data):
        self.sort()
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        list = Linked_List()
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == data:
                for i in range(left, len(arr)):
                    if arr[i] == data:
                        list.addNode(arr[i], list._length)
                break
            elif arr[mid] < data:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    
    #busqueda binaria
    def binary_search_models(self, data, atribute):
        self.sort_models(atribute)
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = getattr(arr[mid], atribute)
            
            if mid_value == data:
                return arr[mid]
            elif mid_value < data:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    
    #busqueda lineal-binaria
    def lineal_binary_search_models(self, data, atribute):       
        self.sort_models(atribute)
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        list = Linked_List()
        
        
        while left <= right:
            mid = (left + right) // 2
            if str(getattr(arr[mid], atribute)).lower() == str(data).lower():  
                for i in range(left, len(arr)):
                    if str(getattr(arr[i], atribute)).lower() == str(data).lower():  
                        list.addNode(arr[i], list._length)         
                break                  
            elif str(getattr(arr[mid], atribute)).lower() < data.lower():
                left = mid + 1
            else:
                right = mid - 1
        return list
    