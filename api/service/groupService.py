from repository.CGroupRepository import CGroupRepository


class groupServicie():
    def __init__(self):
        self.__repositorio = CGroupRepository('bolt://52.207.60.220:33184', 'neo4j', 'heights-completions-preferences')
        self.__repositorio.conectar()

    def get_repositorio(self):
        return self.__repositorio

    def set_repositorio(self, _repo):
        self.__repositorio = _repo

    def crear_grupo(self, _datos):
        temp = self.__repositorio.verificar_grupo(_datos["nombre"])
        if len(temp) == 0:
            self.__repositorio.crear_grupo(_datos["nombre"], _datos["descripcion"])
            return 200
        else:
            return 409

    def asociar_grupogrupo(self, _datos):
        temp = self.__repositorio.verificar_grupo(_datos["nombreg1"])
        temp2 = self.__repositorio.verificar_grupo(_datos["nombreg2"])
        if len(temp) == 0 and len(temp2) == 0:
            self.__repositorio.unir_grupo(_datos["nombreg1"], _datos["nombreg2"])
            return 200
        else:
            return 409

    def obtener_infoGrupo(self, _nombre):
        temp = self.__repositorio.verificar_grupo(_nombre)
        if len(temp) > 0:
            grupo = self.__repositorio.obtener_grupo(_nombre)
            dic = {"nombre": 0, "descripcion": 0, "conceptos": 0}
            concep = list()
            dic["nombre"] = grupo[0]["Grupo.nombre"]
            dic["descripcion"] = grupo[0]["Grupo.descripcion"]
            for i in grupo:
                concep.append(i["Concepto.nombre"])
            dic["conceptos"] = concep
            return dic
        else:
            return {}



if __name__ == '__main__':
    a = groupServicie()
    a.crear_grupo('sida', 'terrible_cochino')
    a.asociar_grupogrupo('sida', 'medicamentos_corona')
    print(a.obtener_infoGrupo('sida'))
