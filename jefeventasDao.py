from jefeventas import JefeVentas  # Importa la clase JefeVentas
from conexion import Conexion
import time
import hashlib

class JefeVentasDao:
    def __init__(self):
        pass

    def encriptarPass(self, password):
        hashObject = hashlib.md5(password.encode('utf-8'))
        password = hashObject.hexdigest()
        return password

    def buscarJefeVentas(self, nombre, password) -> JefeVentas:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            sentencia = 'SELECT password FROM jefe_ventas WHERE nombre=%s and password=%s'
            valores = (nombre, self.encriptarPass(password))
            Conexion.cursor.execute(sentencia, valores)
            registro = Conexion.cursor.fetchone()
            if registro is None:
                return None
            else:
                jefe_ventas = JefeVentas()
                jefe_ventas.nombre = nombre
                jefe_ventas.password = password
                jefe_ventas.conectado = False
                return jefe_ventas
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            print('Volviendo al menú principal, espere..')
            time.sleep(5)
            return None

    def conectar(self, nombre, password) -> JefeVentas:
        jefe_ventas = self.buscar_jefe_ventas(nombre, password)
        if jefe_ventas is None:
            print('Usuario o contraseña incorrectos')
            time.sleep(3)
            return None
        elif jefe_ventas.conectado:
            print('Ya está conectado')
            time.sleep(3)
            return jefe_ventas
        else:
            print('Usuario y contraseña correctos')
            jefe_ventas.conectado = True
            time.sleep(2)
            return jefe_ventas

    def desconectar(self, jefe_ventas) -> None:
        if jefe_ventas is not None and jefe_ventas.conectado:
            jefe_ventas.conectado = False
            Conexion.closeConnection()
        else:
            print('Cerrando, gracias por usar nuestros servicios')
            time.sleep(3)
