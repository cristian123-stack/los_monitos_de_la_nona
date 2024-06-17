import time
import hashlib
from conexion import Conexion
from vendedor import Vendedor

class VendedorDao:
    def __init__(self):
        pass

    def encriptarPass(self, password):
        hashObject = hashlib.md5(password.encode('utf-8'))
        return hashObject.hexdigest()

    def buscarVendedor(self, nombre, password) -> Vendedor:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            sentencia = 'SELECT password FROM vendedor WHERE nombre=%s and password=%s'
            valores = (nombre, self.encriptarPass(password))
            Conexion.cursor.execute(sentencia, valores)
            registro = Conexion.cursor.fetchone()
            if registro is None:
                return None
            else:
                vend = Vendedor()
                vend.nombre = nombre
                vend.password = password
                vend.conectado = False
                return vend
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            print('Volviendo al menú principal, espere..')
            time.sleep(5)
            return None

    def conectar(self, nombre, password) -> Vendedor:
        vendedor = self.buscarVendedor(nombre, password)
        if vendedor is None:
            print('Usuario o contraseña incorrecta')
            time.sleep(3)
            return None
        elif vendedor.conectado:
            print('Ya está conectado')
            time.sleep(3)
            return vendedor
        else:
            print('Email y contraseña correctos')
            vendedor.conectado = True
            time.sleep(2)
            return vendedor

    def desconectar(self, vendedor) -> None:
        if vendedor is not None and vendedor.conectado:
            vendedor.conectado = False
            Conexion.closeConnection()
        else:
            print('Cerrando, gracias por usar nuestros servicios')
            time.sleep(3)
