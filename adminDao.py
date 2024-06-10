from admin import administrador
from conexion import Conexion
import time
import hashlib

class adminDao:
    def __init__(self, intentos):  
        self.__intentos = intentos

    def encriptarPass(self, password):
        hashObject = hashlib.md5(password.encode('utf-8'))
        password = hashObject.hexdigest()
        return password

    def buscarAdmin(self, usuario, password) -> administrador:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            sentencia = 'SELECT password FROM administrador WHERE usuario=%s'
            valores = (usuario,)
            Conexion.cursor.execute(sentencia, valores)
            registro = Conexion.cursor.fetchone()
            if registro is None:
                return None
            else:
                if registro[0]:
                    ad = administrador()
                    ad.usuario = usuario
                    ad.password = password
                    ad.conectado = False
                    ad.intentos = 3
                    return ad
                else:
                    return None
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            print('Volviendo al menú principal, espere..')
            time.sleep(5)
            return None

    def conectar(self, usuario, password) -> administrador:
        admin = self.buscarAdmin(usuario, password)
        if admin is None:
            print('Usuario o clave incorrecta')
            self.__intentos -= 1 
            print(f'Intentos restantes: {self.__intentos}')
            time.sleep(3)
            return None
        elif admin.conectado:
            print('Ya está conectado')
            time.sleep(3)
            return admin
        else:
            print('Email y contraseña correctos')
            admin.conectado = True
            time.sleep(2)
            return admin
        
    def desconectar(self, ad) -> None:
        if ad is not None and ad.conectado:
            ad.conectado = False
            Conexion.closeConnection()
        else:
            print('Error no se ha iniciado sesión previamente...')
            time.sleep(3)