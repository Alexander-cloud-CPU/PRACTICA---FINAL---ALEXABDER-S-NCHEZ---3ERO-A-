class Hospital():
    def __init__(self) -> None:
        self.__id = 0
        self.__nombre = ''
        self.__direccion = 's/n'
        self.__horario = 's/n'
        self.__longitud = "0.0" 
        self.__latitud = "0.0"

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _horario(self):
        return self.__horario

    @_horario.setter
    def _horario(self, value):
        self.__horario = value

    @property
    def _longitud(self):
        return self.__longitud

    @_longitud.setter
    def _longitud(self, value):
        self.__longitud = value

    @property
    def _latitud(self):
        return self.__latitud

    @_latitud.setter
    def _latitud(self, value):
        self.__latitud = value

    @property
    def serializable(self):
        
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "direccion": self.__direccion,
            "horario": self.__horario,
            "longitud": self.__longitud,
            "latitud": self.__latitud
            
        }
    
    def deserializar(data):
        hospital = Hospital()
        hospital._id = data["id"]
        hospital._nombre = data["nombre"]
        hospital._direccion = data["direccion"]
        hospital._horario = data["horario"]
        hospital._longitud = data["longitud"]
        hospital._latitud = data["latitud"]

        return hospital
    def __str__(self) -> str:
        return str(self.__id) + "" + self.__nombre






