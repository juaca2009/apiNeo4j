from repository.CGroupRepository import CGroupRepository

class conceptoServicie():
    def __init__(self):
        self.__repositorio = CGroupRepository('bolt://52.207.60.220:33184', 'neo4j', 'heights-completions-preferences')
        self.__repositorio.conectar()

    def get_repositorio(self):
        return self.__repositorio

    def set_repositorio(self, _repo):
        self.__repositorio = _repo

    def crear_concepto(self, _datos):
        temp = self.__repositorio.verificar_concepto(_datos["nombreg"], _datos["nombrec"])
        if len(temp) == 0:
            self.__repositorio.agregar_concepto(_datos["nombreg"], _datos["nombrec"], _datos["descripcion"])
            return 200
        else:
            return 409
