import getpass
import time
import hashlib
from conexion import Conexion
from admin import administrador

class AdminDao:
    def __init__(self):
        pass

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
                ad = administrador()
                ad.usuario = usuario
                ad.password = password
                ad.conectado = False
                return ad
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            print('Volviendo al menú principal, espere..')
            time.sleep(5)
            return None

    def conectar(self, usuario, password) -> administrador:
        admin = self.buscarAdmin(usuario, password)
        if admin is None:
            print('Usuario o contraseña incorrectos')
            time.sleep(3)
            return None
        elif admin.conectado:
            print('Ya está conectado')
            time.sleep(3)
            return admin
        else:
            print('Usuario y contraseña correctos')
            admin.conectado = True
            time.sleep(2)
            return admin

    def desconectar(self, ad) -> None:
        if ad is not None and ad.conectado:
            ad.conectado = False
            Conexion.closeConnection()
        else:
            print('Cerrando, gracias por usar nuestros servicios')
            time.sleep(3)

    def crearJefeVentas(self) -> bool:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            nombre = input("Ingrese el nombre del nuevo Jefe de Ventas: ")
            if self.existeJefeVentas(nombre):
                print(f'El jefe de ventas con nombre {nombre} ya existe.')
                return False
            password = getpass.getpass("Ingrese la contraseña del nuevo Jefe de Ventas: ")
            email = input("Ingrese el correo electrónico del nuevo Jefe de Ventas: ")
            telefono = input("Ingrese el número de teléfono del nuevo Jefe de Ventas: ")

            sentencia_jefe_ventas = """
                            INSERT INTO jefe_ventas
                            (nombre, password, fk_id_admin, CREATEDAT, UPDATEDAT, state_at) 
                            VALUES (%s, MD5(%s), '1', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'y')
                            """
            valores_jefe_ventas = (nombre, password)
            Conexion.cursor.execute(sentencia_jefe_ventas, valores_jefe_ventas)
            id_jefe_ventas = Conexion.cursor.lastrowid

            sentencia_email = """
                        INSERT INTO email_jefe_ventas
                        (email, fk_id_jefe_ventas, CREATEDAT, UPDATEDAT)
                        VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                        """
            valores_email = (email, id_jefe_ventas)
            Conexion.cursor.execute(sentencia_email, valores_email)

            sentencia_telefono = """
                            INSERT INTO telefono_jefe_ventas
                            (telefono, fk_id_jefe_ventas, CREATEDAT, UPDATEDAT)
                            VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                            """
            valores_telefono = (telefono, id_jefe_ventas)
            Conexion.cursor.execute(sentencia_telefono, valores_telefono)
            Conexion.connection.commit()

            print(f'Se ha creado el usuario jefe de ventas: {nombre}')
            return True
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False
        
    def existeJefeVentas(self, nombre):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            sentencia = "SELECT nombre FROM jefe_ventas WHERE nombre = %s"
            Conexion.cursor.execute(sentencia, (nombre,))
            resultado = Conexion.cursor.fetchone()
            return resultado is not None
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False

    def crearVendedor(self) -> bool:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            nombre = input("Ingrese el nombre del nuevo Vendedor: ")
            if self.existeVendedor(nombre):
                print(f'El vendedor con nombre {nombre} ya existe.')
                return False
            password = getpass.getpass("Ingrese la contraseña del nuevo Vendedor: ")
            email = input("Ingrese el correo electrónico del nuevo Vendedor: ")
            telefono = input("Ingrese el número de teléfono del nuevo Vendedor: ")
            sentencia_vendedor = """
                            INSERT INTO vendedor
                            (nombre, password, fk_id_admin, CREATEDAT, UPDATEDAT, state_at) 
                            VALUES (%s, MD5(%s), '1', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'y')
                            """
            valores_vendedor = (nombre, password)
            Conexion.cursor.execute(sentencia_vendedor, valores_vendedor)
            id_vendedor = Conexion.cursor.lastrowid
            sentencia_email = """
                        INSERT INTO email_vendedor
                        (email, fk_id_vendedor, CREATEDAT, UPDATEDAT)
                        VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                        """
            valores_email = (email, id_vendedor)
            Conexion.cursor.execute(sentencia_email, valores_email)
            sentencia_telefono = """
                            INSERT INTO telefono_vendedor
                            (telefono, fk_id_vendedor, CREATEDAT, UPDATEDAT)
                            VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                            """
            valores_telefono = (telefono, id_vendedor)
            Conexion.cursor.execute(sentencia_telefono, valores_telefono)
            Conexion.connection.commit()
            print(f'Se ha creado el usuario vendedor: {nombre}')
            return True
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False

    def existeVendedor(self, nombre):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            sentencia = "SELECT nombre FROM vendedor WHERE nombre = %s"
            Conexion.cursor.execute(sentencia, (nombre,))
            resultado = Conexion.cursor.fetchone()
            return resultado is not None
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False

    def actualizarJefeVentas(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

            nombre_actual = input("Ingrese el nombre del Jefe de Ventas cuya información desea actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del Jefe de Ventas (Presione Enter para mantener el mismo): ")
            nueva_password = getpass.getpass("Ingrese la nueva contraseña del Jefe de Ventas (Presione Enter para mantener la misma): ")
            nuevo_email = input("Ingrese el nuevo correo electrónico del Jefe de Ventas (Presione Enter para mantener el mismo): ")
            nuevo_telefono = input("Ingrese el nuevo número de teléfono del Jefe de Ventas (Presione Enter para mantener el mismo): ")

            if not self.existeJefeVentas(nombre_actual):
                print("El usuario no existe.")
                return False

        # Actualizar tabla jefe_ventas
            sentencia_jefe_ventas = "UPDATE jefe_ventas SET"
            valores_jefe_ventas = []
            if nuevo_nombre:
                sentencia_jefe_ventas += " nombre=%s,"
                valores_jefe_ventas.append(nuevo_nombre)
            if nueva_password:
                sentencia_jefe_ventas += " password=MD5(%s),"
                valores_jefe_ventas.append(nueva_password)
            sentencia_jefe_ventas += " UPDATEDAT=current_timestamp() WHERE nombre=%s"
            valores_jefe_ventas.append(nombre_actual)
            Conexion.cursor.execute(sentencia_jefe_ventas, valores_jefe_ventas)

        # Obtener el id del jefe de ventas
            sentencia_id = "SELECT id_jefe_ventas FROM jefe_ventas WHERE nombre=%s"
            Conexion.cursor.execute(sentencia_id, (nuevo_nombre if nuevo_nombre else nombre_actual,))
            id_jefe_ventas = Conexion.cursor.fetchone()[0]

        # Actualizar tabla email_jefe_ventas
            if nuevo_email:
                sentencia_email = "UPDATE email_jefe_ventas SET email=%s, UPDATEDAT=current_timestamp() WHERE fk_id_jefe_ventas=%s"
                valores_email = (nuevo_email, id_jefe_ventas)
                Conexion.cursor.execute(sentencia_email, valores_email)

        # Actualizar tabla telefono_jefe_ventas
            if nuevo_telefono:
                sentencia_telefono = "UPDATE telefono_jefe_ventas SET telefono=%s, UPDATEDAT=current_timestamp() WHERE fk_id_jefe_ventas=%s"
                valores_telefono = (nuevo_telefono, id_jefe_ventas)
                Conexion.cursor.execute(sentencia_telefono, valores_telefono)

            Conexion.connection.commit()

            print("Información del Jefe de Ventas actualizada exitosamente.")
            return True
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False



    def actualizarVendedor(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
        
            nombre_actual = input("Ingrese el nombre del Vendedor cuya información desea actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del Vendedor (Presione Enter para mantener el mismo): ")
            nueva_password = getpass.getpass("Ingrese la nueva contraseña del Vendedor (Presione Enter para mantener la misma): ")
            nuevo_email = input("Ingrese el nuevo correo electrónico del Vendedor (Presione Enter para mantener el mismo): ")
            nuevo_telefono = input("Ingrese el nuevo número de teléfono del Vendedor (Presione Enter para mantener el mismo): ")
        
            if not self.existeVendedor(nombre_actual):
                print("El usuario no existe.")
                return False
        
        # Actualizar tabla vendedor
            sentencia_vendedor = "UPDATE vendedor SET"
            valores_vendedor = []
            if nuevo_nombre:
                sentencia_vendedor += " nombre=%s,"
                valores_vendedor.append(nuevo_nombre)
            if nueva_password:
                sentencia_vendedor += " password=MD5(%s),"
                valores_vendedor.append(nueva_password)
            sentencia_vendedor += " UPDATEDAT=current_timestamp() WHERE nombre=%s"
            valores_vendedor.append(nombre_actual)
            Conexion.cursor.execute(sentencia_vendedor, valores_vendedor)
        
        # Obtener el id del vendedor
            sentencia_id = "SELECT id_vendedor FROM vendedor WHERE nombre=%s"
            Conexion.cursor.execute(sentencia_id, (nuevo_nombre if nuevo_nombre else nombre_actual,))
            id_vendedor = Conexion.cursor.fetchone()[0]
        
        # Actualizar tabla email_vendedor
            if nuevo_email:
                sentencia_email = "UPDATE email_vendedor SET email=%s, UPDATEDAT=current_timestamp() WHERE fk_id_vendedor=%s"
                valores_email = (nuevo_email, id_vendedor)
                Conexion.cursor.execute(sentencia_email, valores_email)
        
        # Actualizar tabla telefono_vendedor
            if nuevo_telefono:
                sentencia_telefono = "UPDATE telefono_vendedor SET telefono=%s, UPDATEDAT=current_timestamp() WHERE fk_id_vendedor=%s"
                valores_telefono = (nuevo_telefono, id_vendedor)
                Conexion.cursor.execute(sentencia_telefono, valores_telefono)
        
            Conexion.connection.commit()
        
            print("Información del Vendedor actualizada exitosamente.")
            return True
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False



    def eliminarVendedor(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            nombre = input("Ingrese el nombre del Vendedor que desea eliminar: ")
            if not self.existeVendedor(nombre):
                print("El vendedor no existe.")
                return False
            # Obtener el id del vendedor
            sentencia_id = "SELECT id_vendedor FROM vendedor WHERE nombre=%s"
            Conexion.cursor.execute(sentencia_id, (nombre,))
            id_vendedor = Conexion.cursor.fetchone()[0]
            # Eliminar registros de email_vendedor y telefono_vendedor
            sentencia_email = "DELETE FROM email_vendedor WHERE fk_id_vendedor=%s"
            Conexion.cursor.execute(sentencia_email, (id_vendedor,))
            sentencia_telefono = "DELETE FROM telefono_vendedor WHERE fk_id_vendedor=%s"
            Conexion.cursor.execute(sentencia_telefono, (id_vendedor,))
            # Eliminar registro de vendedor
            sentencia_vendedor = "DELETE FROM vendedor WHERE id_vendedor=%s"
            Conexion.cursor.execute(sentencia_vendedor, (id_vendedor,))
            Conexion.connection.commit()
            print("Vendedor eliminado exitosamente.")
            return True
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False

    def eliminarJefeVentas(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            nombre = input("Ingrese el nombre del Jefe de Ventas que desea eliminar: ")
            if not self.existeJefeVentas(nombre):
                print("El jefe de ventas no existe.")
                return False
            # Obtener el id del jefe de ventas
            sentencia_id = "SELECT id_jefe_ventas FROM jefe_ventas WHERE nombre=%s"
            Conexion.cursor.execute(sentencia_id, (nombre,))
            id_jefe_ventas = Conexion.cursor.fetchone()[0]
            # Eliminar registros de email_jefe_ventas y telefono_jefe_ventas
            sentencia_email = "DELETE FROM email_jefe_ventas WHERE fk_id_jefe_ventas=%s"
            Conexion.cursor.execute(sentencia_email, (id_jefe_ventas,))
            sentencia_telefono = "DELETE FROM telefono_jefe_ventas WHERE fk_id_jefe_ventas=%s"
            Conexion.cursor.execute(sentencia_telefono, (id_jefe_ventas,))
            # Eliminar registro de jefe de ventas
            sentencia_jefe_ventas = "DELETE FROM jefe_ventas WHERE id_jefe_ventas=%s"
            Conexion.cursor.execute(sentencia_jefe_ventas, (id_jefe_ventas,))
            Conexion.connection.commit()
            print("Jefe de ventas eliminado exitosamente.")
            return True
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False


    def mostrarJefesVentas(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
            sentencia = """
                        SELECT jv.nombre, ev.email, tv.telefono
                        FROM jefe_ventas jv
                        JOIN email_jefe_ventas ev ON jv.id_jefe_ventas = ev.fk_id_jefe_ventas
                        JOIN telefono_jefe_ventas tv ON jv.id_jefe_ventas = tv.fk_id_jefe_ventas;
                        """
            Conexion.cursor.execute(sentencia)
            jefes_ventas = Conexion.cursor.fetchall()
            return jefes_ventas
        except Exception as e:
            print(f'Ha ocurrido el siguiente error al mostrar jefes de ventas: {e}')
            return []

    def mostrarVendedores(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
        
            sentencia = """
                        SELECT v.nombre, ev.email, tv.telefono
                        FROM vendedor v
                        JOIN email_vendedor ev ON v.id_vendedor = ev.fk_id_vendedor
                        JOIN telefono_vendedor tv ON v.id_vendedor = tv.fk_id_vendedor;
                        """
            Conexion.cursor.execute(sentencia)
            vendedores = Conexion.cursor.fetchall()
            return vendedores
        except Exception as e:
            print(f'Ha ocurrido el siguiente error al mostrar vendedores: {e}')
            return []
