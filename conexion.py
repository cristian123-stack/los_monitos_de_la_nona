import pymysql

class Conexion:
    connection=None
    cursor= None

    def __init__(self) -> None:
        pass
    @classmethod
    def getConnection(cls):
        if cls.connection is None:
            conex = pymysql.connect(host='localhost',port=3308,user='root',password='',db='los_monitos_de_la_nona')
            cls.cursor = conex.cursor()
            cls.connection = conex
    @classmethod
    def closeConnection(cls):
        try:
            if cls.connection is not None:
                if cls.connection.open:
                    cls.connection.close
                    print('se cerro con exito la conexion')
                else:
                    print('la conexion no esta abierta')
            else:
                print('no hay ninguna conexion establecida')
        except pymysql.Error as e:
            print (f'error al cerrar la conexion {e}')
        finally:
            cls.connection = None
            cls.cursor = None
