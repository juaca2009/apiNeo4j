class createConceptoDto():
    def __init__(self, _idConcept, _coddeType, _desc) :
        self.__idConcept = _idConcept
        self.__codeType = _coddeType
        self.__desc = _desc

    def get_idConcept(self):
        return self.__idConcept

    def get_codeType(self):
        return self.__codeType

    def get_desc(self):
        return self.__desc

    def set_idConcept(self, _idConcept):
        self.__idConcept = _idConcept

    def set_codeType(self, _coddeType):
        self.__codeType = _coddeType
    
    def set_desc(self, _desc):
        self.__desc = _desc