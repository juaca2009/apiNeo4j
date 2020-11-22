class createGrupoDto():
    def __init__(self, _nombre, _desc, _id):
        self.__id = _id
        self.__nombre = _nombre
        self.__desc = _desc

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_desc(self):
        return self.__desc 

    def set_id(self, _id):
        self.__id = _id

    def set_nombre(self, _nombre):
        self.__nombre = _nombre

    def set_desc(self, _desc):
        self.__desc = _desc