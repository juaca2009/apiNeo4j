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

    def crear_grupo(self, _nombre, _desc, _id):
        query  = "CREATE (p:Grupo"
        query = query + " {id:$id, nombre:$nom, descripcion:$des})"
        self.__sesion.run(query, parameters = {'id':_id, 'nom':_nombre, 'des':_desc})

    def eliminar_grupo(self, _id):
        query = "MATCH(n:Grupo {id:$id}) DETACH DELETE n"
        self.__sesion.run(query, parameters = {'id':_id})
        query = "MATCH (n) WHERE NOT (n)--() DELETE n"
        self.__sesion.run(query)

    def crear_concepto(self,  _codeType, _idConcept, _desc):
        query = "CREATE (p:Concepto"
        query = query + " {id_concepto:$id, id_type:$conid, descripcion:$des})"
        self.__sesion.run(query, parameters = {'id':_idConcept, 'conid':_idConcept, 'des':_desc})

    def agregar_concepto(self, _id, _codeType, _idConcept, _desc):
        self.crear_concepto(_codeType, _idConcept, _desc)
        query = "MATCH (g:Grupo {id:$id}), (c:Concepto {id_concepto:$idc}) CREATE (g)-[:contiene_a]->(c)"
        self.__sesion.run(query, parameters = {'id':_id, 'idc':_idConcept})

    def eliminar_concepto(self, _idConcept):
        query = "MATCH(n:Concepto {id_concepto:$idc}) DETACH DELETE n"
        self.__sesion.run(query, parameters = {'idc': _idConcept})

    def obtener_grupo(self, _id):
        query = "MATCH(n:Grupo) WHERE n.id = $id RETURN n.nombre"
        a = self.__sesion.run(query, parameters = {'id':_id})
        return a.single()
        

       
        




if __name__ == '__main__':
    a = CGroupRepository('bolt://100.26.171.12:33429', 'neo4j', 'verb-designation-abusers')
    a.conectar()
    #a.crear_grupo('grupo1', 'grupo_de_prueba', str(122234))
    #a.agregar_concepto(str(122234),'int', '1s3d4', 'primer concepto')
    #a.eliminar_grupo(str(122234))
    #a.eliminar_concepto('1s3d4')
    #a.obtener_grupo(str(122234))