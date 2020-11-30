from neo4j import GraphDatabase

class CGroupRepository():
    def __init__(self, _host, _usuario, _password):
        self.__host = _host
        self.__usuario = _usuario
        self.__password = _password
        self.__driver = None
        self.__sesion = None

    def conectar(self):
        self.__driver = GraphDatabase.driver(self.__host, auth=(self.__usuario, self.__password))
        self.__sesion = self.__driver.session()

    def crear_grupo(self, _nombre, _desc):
        query  = "CREATE (p:Grupo"
        query = query + " {nombre:$nom, descripcion:$des})"
        self.__sesion.run(query, parameters = {'nom':_nombre, 'des':_desc})

    def eliminar_grupo(self, _nombre):
        query = "MATCH(n:Grupo {nombre:$nom}) DETACH DELETE n"
        self.__sesion.run(query, parameters = {'nom':_nombre})
        query = "MATCH (n) WHERE NOT (n)--() DELETE n"
        self.__sesion.run(query)

    def crear_concepto(self,  _nombre, _desc):
        query = "CREATE (p:Concepto"
        query = query + " {nombre:$nom, descripcion:$des})"
        self.__sesion.run(query, parameters = {'nom':_nombre, 'des':_desc})

    def agregar_concepto(self, _nombreg, _nombrec, _desc):
        self.crear_concepto(_nombrec, _desc)
        query = "MATCH (g:Grupo {nombre:$nomg}), (c:Concepto {nombre:$nomc}) CREATE (g)-[:contiene_a]->(c)"
        self.__sesion.run(query, parameters = {'nomg':_nombreg, 'nomc':_nombrec})

    def eliminar_concepto(self, _nombre):
        query = "MATCH(n:Concepto {nombre:$nom}) DETACH DELETE n"
        self.__sesion.run(query, parameters = {'nom': _nombre})


    def unir_grupo(self, _nombreg1, _nombreg2):
        query = "MATCH (g:Grupo {nombre:$nomg1}), (c:Grupo {nombre:$nomg2}) CREATE (g)-[:contiene_m]->(c)"
        self.__sesion.run(query, parameters = {'nomg1':_nombreg1, 'nomg2':_nombreg2})

    def obtener_grupo(self, _nombre):
        query = "MATCH (Grupo)-[:contiene_a]->(Concepto) WHERE Grupo.nombre=$nom RETURN Grupo.nombre, Grupo.descripcion, Concepto.nombre"
        a = self.__sesion.run(query, parameters = {'nom':_nombre})
        temp = list()
        for i in a:
            temp.append(i)
        return temp

    def verificar_grupo(self, _nombre):
        query = "MATCH (g:Grupo {nombre:$nom}) RETURN g"
        a = self.__sesion.run(query, parameters = {'nom':_nombre})
        print(type(a))
        temp = list()
        for i in a:
            temp.append(i)
        return temp

    def verificar_concepto(self, _nombreg, _nombrec):
        query = "MATCH (Grupo)-[:contiene_a]->(Concepto) WHERE Grupo.nombre=$nom and Concepto.nombre =$nomc RETURN Grupo.nombre"
        a = self.__sesion.run(query, parameters = {'nom':_nombreg, 'nomc':_nombrec})
        temp = list()
        for i in a:
            temp.append(i)
        return temp
        

       
        
if __name__ == '__main__':
    a = CGroupRepository('bolt://52.207.60.220:33184', 'neo4j', 'heights-completions-preferences')
    a.conectar()
    #a.crear_grupo('corona_virus', 'muerte_inminente')
    #a.agregar_concepto('corona_virus', 'fiebre', 'sintoma')
    #a.crear_grupo('medicamentos_corona', 'tratamiento')
    #a.agregar_concepto('medicamentos_corona', 'acetaminofen', 'medicamento_efectivo')
    #a.unir_grupo('corona_virus', 'medicamentos_corona')
    #a.agregar_concepto('corona_virus', 'tos', 'sintoma2')
    b = a.obtener_grupo('corona_virus')
    print(b[0]["Grupo.nombre"])
    #a.eliminar_grupo(str(122234))
    #a.eliminar_concepto('1s3d4')
    #a.obtener_grupo(str(122234))
