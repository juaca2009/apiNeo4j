import pymysql


class conceptosRepository():
    def __init__(self, _host, _user, _password, _dbName):
        self.__host = _host
        self.__user = _user
        self.__password = _password
        self.__dbName = _dbName
        self.__conexion = None
        self.__cursor = None

    def conectar(self):
        self.__conexion = pymysql.Connect(host=self.__host, user=self.__user, password=self.__password, db=self.__dbName)
        self.__cursor = self.__conexion.cursor()

    def VerificarConceptoById(self, _id):
        self.__cursor.execute(
            """
            select idCODE from concepts 
            where idCODE = %s
            """,
            (_id)
        )
        return self.__cursor.fetchall()

    def conceptoByid(self, _id):
        self.__cursor.execute(
            """
            select idCODE, CODETYPE, SHORT_DESC from concepts
            where idCODE = %s
            """,
            (_id)
        )
        return self.__cursor.fetchall()