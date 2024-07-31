from controls.dao.daoAdapter import DaoAdapter
from models.practica.hospital import Hospital


class HospitalControl(DaoAdapter):
    def __init__(self):
        super().__init__(Hospital)
        self.__hospital = None

    @property
    def _hospital(self):
        if self.__hospital == None:
            self.__hospital = Hospital()
        return self.__hospital

    @_hospital.setter
    def _hospital(self, value):
        self.__hospital = value

    def _lista(self):
        return self._list()

    @property
    def save(self):
        #self._hospital._id = self.lista._length + 1
        self._save(self._hospital)

    def merge(self, pos):
        self._merge(self._hospital, pos)
  

