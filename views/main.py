import sys
sys.path.append('../')
import random
import time
from controls.tda.linked.linkedList import Linked_List
from controls.tda.linked.node import Node
from controls.tda.queque.queque import Queque
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.graphManaged import GraphManaged
from controls.tda.graph.graphNoManaged import GraphNoManaged
from controls.tda.graph.graphLabelManaged import GraphLabelManaged
from controls.tda.graph.graphLabelNoManaged import GraphLabelNoManaged
from controls.practica.hospitalControl import HospitalControl
from controls.tda.tree.treeNumber import TreeNumber
from controls.tda.tree.jug.modelo.node import Node as JugNode
from controls.tda.tree.jug.modelo.rules import Rules
from controls.practica.hospitalGrafo import HospitalGrafo
from controls.practica.hospitalControl import HospitalControl


hc = HospitalControl()
try:

   hc._hospital._nombre = "Hospital Isidro Ayora"
   hc._hospital._direccion = "San Juan de Dios, Loja"
   hc._hospital._horario = "24H"
   hc._hospital._latitud = "00"
   hc._hospital._longitud = "00"
   hc.save

except Exception as error:
    print("Errores durante la creación o inserción de aristas:")
    print(error)
