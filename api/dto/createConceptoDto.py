class createConceptoDto():
    def __init__(self, _nombre, _desc) :
        self.__nombre = _nombre
        self.__desc = _desc


    def get_nombre(self):
        return self.__nombre

    def get_desc(self):
        return self.__desc

    def set_nombre(self, _nombre):
        self.__codeType = _nombre
    
    def set_desc(self, _desc):
        self.__desc = _desc