from jefeventas import JefeVentas 
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
            
            # Encriptar la contraseña ingresada
            password_encriptada = self.encriptarPass(password)
            
            # Buscar jefe de ventas con la contraseña encriptada
            sentencia = 'SELECT nombre FROM jefe_ventas WHERE nombre=%s AND password=%s'
            valores = (nombre, password_encriptada)
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
        jefe_ventas = self.buscarJefeVentas(nombre, password)
        if jefe_ventas is None:
            print('Usuario o contraseña incorrectos. Por favor, inténtelo nuevamente.')
            time.sleep(3)
            return None
        elif jefe_ventas.conectado:
            print('Ya está conectado.')
            time.sleep(3)
            return jefe_ventas
        else:
            print('Usuario y contraseña correctos. Conectando...')
            jefe_ventas.conectado = True
            time.sleep(2)
            return jefe_ventas

    def desconectar(self, jefe_ventas) -> None:
        if jefe_ventas is not None and jefe_ventas.conectado:
            jefe_ventas.conectado = False
            Conexion.closeConnection()
            print('Desconectado correctamente.')
        else:
            print('Cerrando, gracias por usar nuestros servicios.')
            time.sleep(3)


    def insertarProducto(self) -> bool:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
        
            continuar = input("¿Desea agregar un producto? (si/no): ")
            if continuar.lower() != 'si':
                print("Proceso cancelado, volviendo al menú.")
                time.sleep(3)
                return False

        # Verificar si hay proveedores existentes
            Conexion.cursor.execute("SELECT COUNT(*) FROM proveedor")
            proveedores_existen = Conexion.cursor.fetchone()[0] > 0

            if proveedores_existen:
                print("Proveedores registrados encontrados.")

                opcion = input("¿Desea usar un proveedor existente? (si/no): ")
                if opcion.lower() == 'si':
                # Mostrar proveedores existentes
                    Conexion.cursor.execute("SELECT rut_prov, nombre FROM proveedor")
                    proveedores = Conexion.cursor.fetchall()

                    print("Proveedores registrados:")
                    for proveedor in proveedores:
                        print(f"RUT: {proveedor[0]}, Nombre: {proveedor[1]}")

                    rut_prov = input("Ingrese el RUT del proveedor que desea usar: ")

                else:
                # Solicitar datos para crear un nuevo proveedor
                    rut_prov = input("Ingrese el RUT del nuevo proveedor: ")
                    nombre_prov = input("Ingrese el nombre del nuevo proveedor: ")
                    direccion_prov = input("Ingrese la dirección del nuevo proveedor: ")

                # Inserción del proveedor en la tabla proveedor
                    sentencia_proveedor = """
                        INSERT INTO proveedor
                        (rut_prov, nombre, direccion_prov, CREATEDAT, UPDATEDAT)
                        VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    """
                    valores_proveedor = (rut_prov, nombre_prov, direccion_prov)
                    Conexion.cursor.execute(sentencia_proveedor, valores_proveedor)
                    Conexion.connection.commit()

                    print(f'Se ha registrado el nuevo proveedor: {nombre_prov}')

                    # Inserción del email del proveedor
                    email_prov = input("Ingrese el email del proveedor: ")
                    sentencia_email = """
                        INSERT INTO email_proveedor
                        (email, fk_rut_prov, CREATEDAT, UPDATEDAT)
                        VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    """
                    valores_email = (email_prov, rut_prov)
                    Conexion.cursor.execute(sentencia_email, valores_email)
                    Conexion.connection.commit()

                # Inserción del teléfono del proveedor
                    telefono_prov = input("Ingrese el teléfono del proveedor: ")
                    sentencia_telefono = """
                        INSERT INTO telefono_proveedor
                        (telefono, fk_rut_prov, CREATEDAT, UPDATEDAT)
                        VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    """
                    valores_telefono = (telefono_prov, rut_prov)
                    Conexion.cursor.execute(sentencia_telefono, valores_telefono)
                    Conexion.connection.commit()

            else:
                # No hay proveedores registrados, crear uno nuevo
                print("No hay proveedores registrados. Vamos a registrar uno nuevo.")

                rut_prov = input("Ingrese el RUT del nuevo proveedor: ")
                nombre_prov = input("Ingrese el nombre del nuevo proveedor: ")
                direccion_prov = input("Ingrese la dirección del nuevo proveedor: ")

            # Inserción del proveedor en la tabla proveedor
                sentencia_proveedor = """
                    INSERT INTO proveedor
                    (rut_prov, nombre, direccion_prov, CREATEDAT, UPDATEDAT)
                    VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """
                valores_proveedor = (rut_prov, nombre_prov, direccion_prov)
                Conexion.cursor.execute(sentencia_proveedor, valores_proveedor)
                Conexion.connection.commit()

                print(f'Se ha registrado el nuevo proveedor: {nombre_prov}')

            # Inserción del email del proveedor
                email_prov = input("Ingrese el email del proveedor: ")
                sentencia_email = """
                    INSERT INTO email_proveedor
                    (email, fk_rut_prov, CREATEDAT, UPDATEDAT)
                    VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """
                valores_email = (email_prov, rut_prov)
                Conexion.cursor.execute(sentencia_email, valores_email)
                Conexion.connection.commit()

            # Inserción del teléfono del proveedor
                telefono_prov = input("Ingrese el teléfono del proveedor: ")
                sentencia_telefono = """
                    INSERT INTO telefono_proveedor
                    (telefono, fk_rut_prov, CREATEDAT, UPDATEDAT)
                    VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """
                valores_telefono = (telefono_prov, rut_prov)
                Conexion.cursor.execute(sentencia_telefono, valores_telefono)
                Conexion.connection.commit()

        # Verificar si hay bodegas existentes
            Conexion.cursor.execute("SELECT COUNT(*) FROM bodega")
            bodegas_existen = Conexion.cursor.fetchone()[0] > 0

            if bodegas_existen:
                print("Bodegas registradas encontradas.")

                opcion_bodega = input("¿Desea usar una bodega existente? (si/no): ")
                if opcion_bodega.lower() == 'si':
                # Mostrar bodegas existentes
                    Conexion.cursor.execute("SELECT id_bodega, nombre FROM bodega")
                    bodegas = Conexion.cursor.fetchall()

                    print("Bodegas registradas:")
                    for bodega in bodegas:
                        print(f"ID: {bodega[0]}, Nombre: {bodega[1]}")

                    id_bodega = input("Ingrese el ID de la bodega que desea usar: ")

                else:
                # Solicitar datos para crear una nueva bodega
                    nombre_bodega = input("Ingrese el nombre de la nueva bodega: ")
                    direccion_bodega = input("Ingrese la dirección de la nueva bodega: ")

                # Inserción de la bodega en la tabla bodega
                    sentencia_bodega = """
                        INSERT INTO bodega
                        (nombre, direccion, CREATEDAT, UPDATEDAT)
                        VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    """
                    valores_bodega = (nombre_bodega, direccion_bodega)
                    Conexion.cursor.execute(sentencia_bodega, valores_bodega)
                    Conexion.connection.commit()

                    print(f'Se ha registrado la nueva bodega: {nombre_bodega}')

                # Obtener el ID de la bodega recién insertada
                    Conexion.cursor.execute("SELECT id_bodega FROM bodega WHERE nombre=%s ORDER BY CREATEDAT DESC LIMIT 1", (nombre_bodega,))
                    id_bodega = Conexion.cursor.fetchone()[0]

            else:
            # No hay bodegas registradas, crear una nueva
                print("No hay bodegas registradas. Vamos a registrar una nueva.")

                nombre_bodega = input("Ingrese el nombre de la nueva bodega: ")
                direccion_bodega = input("Ingrese la dirección de la nueva bodega: ")

            # Inserción de la bodega en la tabla bodega
                sentencia_bodega = """
                    INSERT INTO bodega
                    (nombre, direccion, CREATEDAT, UPDATEDAT)
                    VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """
                valores_bodega = (nombre_bodega, direccion_bodega)
                Conexion.cursor.execute(sentencia_bodega, valores_bodega)
                Conexion.connection.commit()

                print(f'Se ha registrado la nueva bodega: {nombre_bodega}')

            # Obtener el ID de la bodega recién insertada
                Conexion.cursor.execute("SELECT id_bodega FROM bodega WHERE nombre=%s ORDER BY CREATEDAT DESC LIMIT 1", (nombre_bodega,))
                id_bodega = Conexion.cursor.fetchone()[0]

        # Inserción del producto
            nombre_producto = input("Ingrese el nombre del nuevo producto: ")
            cantidad = int(input("Ingrese la cantidad del nuevo producto: "))
            valor_unitario = float(input("Ingrese el valor unitario del nuevo producto: "))
            fecha_elaboracion = input("Ingrese la fecha de elaboración del nuevo producto (YYYY-MM-DD): ")
            fecha_caducidad = input("Ingrese la fecha de caducidad del nuevo producto (YYYY-MM-DD): ")

            print("\nDatos ingresados:")
            print(f"Nombre del Producto: {nombre_producto}")
            print(f"Cantidad: {cantidad}")
            print(f"Valor Unitario: {valor_unitario}")
            print(f"RUT del Proveedor: {rut_prov}")
            print(f"Fecha de Elaboración: {fecha_elaboracion}")
            print(f"Fecha de Caducidad: {fecha_caducidad}")
            print(f"ID de la Bodega: {id_bodega}")

            confirmar = input("Estos son los datos. ¿Desea ingresar el nuevo producto? (si/no): ")
            if confirmar.lower() != 'si':
                print("Proceso cancelado, volviendo al menú.")
                return False

        # Inserción del producto en la tabla producto
            sentencia_producto = """
                INSERT INTO producto
                (nombre, cantidad, valor_unitario, fk_rut_prov, fecha_elaboracion, fecha_caducidad, CREATEDAT, UPDATEDAT) 
                VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """
            valores_producto = (nombre_producto, cantidad, valor_unitario, rut_prov, fecha_elaboracion, fecha_caducidad)
            Conexion.cursor.execute(sentencia_producto, valores_producto)
            Conexion.connection.commit()

            print(f'Se ha creado el producto: {nombre_producto}')

        # Obtener el id del producto recién insertado
            Conexion.cursor.execute("SELECT id_producto FROM producto WHERE nombre=%s AND fk_rut_prov=%s ORDER BY CREATEDAT DESC LIMIT 1", (nombre_producto, rut_prov))
            id_producto = Conexion.cursor.fetchone()[0]

        # Actualización de la bodega con el producto
            sentencia_bodega_producto = """
                UPDATE bodega
                SET fk_id_producto=%s, UPDATEDAT=CURRENT_TIMESTAMP
                WHERE id_bodega=%s
            """
            valores_bodega_producto = (id_producto, id_bodega)
            Conexion.cursor.execute(sentencia_bodega_producto, valores_bodega_producto)
            Conexion.connection.commit()

            print(f'El producto {nombre_producto} ha sido almacenado en la bodega con ID: {id_bodega}')
            time.sleep(5)
            return True

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False
        


    def actualizarProducto(self) -> bool:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

            continuar = input("¿Desea actualizar la información de un Producto? (si/no): ")
            if continuar.lower() != 'si':
                print("Proceso cancelado, volviendo al menú.")
                return False

        # Mostrar productos existentes
            Conexion.cursor.execute("SELECT id_producto, nombre FROM producto")
            productos = Conexion.cursor.fetchall()

            if not productos:
                print("No hay productos registrados.")
                return False

            print("Productos registrados:")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}")

            id_producto = int(input("Ingrese el ID del producto que desea actualizar: "))

        # Verificar si el producto existe
            Conexion.cursor.execute("SELECT COUNT(*) FROM producto WHERE id_producto=%s", (id_producto,))
            producto_existe = Conexion.cursor.fetchone()[0] > 0

            if not producto_existe:
                print("El producto no existe.")
                return False

        # Solicitar nuevos datos del producto
            nombre_producto = input("Ingrese el nuevo nombre del producto (dejar en blanco para no cambiar): ")
            cantidad = input("Ingrese la nueva cantidad del producto (dejar en blanco para no cambiar): ")
            valor_unitario = input("Ingrese el nuevo valor unitario del producto (dejar en blanco para no cambiar): ")
            fecha_elaboracion = input("Ingrese la nueva fecha de elaboración del producto (YYYY-MM-DD, dejar en blanco para no cambiar): ")
            fecha_caducidad = input("Ingrese la nueva fecha de caducidad del producto (YYYY-MM-DD, dejar en blanco para no cambiar): ")

        # Preparar la sentencia SQL de actualización
            campos_a_actualizar = []
            valores_a_actualizar = []

            if nombre_producto:
                campos_a_actualizar.append("nombre=%s")
                valores_a_actualizar.append(nombre_producto)

            if cantidad:
                campos_a_actualizar.append("cantidad=%s")
                valores_a_actualizar.append(cantidad)

            if valor_unitario:
                campos_a_actualizar.append("valor_unitario=%s")
                valores_a_actualizar.append(valor_unitario)

            if fecha_elaboracion:
                campos_a_actualizar.append("fecha_elaboracion=%s")
                valores_a_actualizar.append(fecha_elaboracion)

            if fecha_caducidad:
                campos_a_actualizar.append("fecha_caducidad=%s")
                valores_a_actualizar.append(fecha_caducidad)

            if not campos_a_actualizar:
                print("No se ha ingresado ningún dato para actualizar.")
                return False

            valores_a_actualizar.append(id_producto)
            sentencia_actualizacion = f"""
                UPDATE producto
                SET {', '.join(campos_a_actualizar)}, UPDATEDAT=CURRENT_TIMESTAMP
                WHERE id_producto=%s
            """

        # Ejecutar la actualización
            Conexion.cursor.execute(sentencia_actualizacion, tuple(valores_a_actualizar))
            Conexion.connection.commit()

            print(f'El producto con ID {id_producto} ha sido actualizado correctamente.')

            continuar = input("¿Desea continuar con la actualización de otro Producto? (si/no): ")
            if continuar.lower() != 'si':
                print("Proceso cancelado, volviendo al menú.")
                return False

            return True

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False

    def actualizarStockProducto(self) -> bool:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

            continuar = input("¿Desea actualizar el stock de un Producto? (si/no): ")
            if continuar.lower() != 'si':
                print("Proceso cancelado, volviendo al menú.")
                return False

        # Mostrar productos existentes
            Conexion.cursor.execute("SELECT id_producto, nombre, cantidad FROM producto")
            productos = Conexion.cursor.fetchall()

            if not productos:
                print("No hay productos registrados.")
                return False

            print("Productos registrados:")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad actual: {producto[2]}")

            id_producto = int(input("Ingrese el ID del producto cuyo stock desea actualizar: "))

            # Verificar si el producto existe
            Conexion.cursor.execute("SELECT COUNT(*) FROM producto WHERE id_producto=%s", (id_producto,))
            producto_existe = Conexion.cursor.fetchone()[0] > 0

            if not producto_existe:
                print("El producto no existe.")
                return False

            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))

        # Actualización del stock del producto
            sentencia_actualizacion = """
                UPDATE producto
                SET cantidad=%s, UPDATEDAT=CURRENT_TIMESTAMP
                WHERE id_producto=%s
            """
            valores_actualizacion = (nueva_cantidad, id_producto)
            Conexion.cursor.execute(sentencia_actualizacion, valores_actualizacion)
            Conexion.connection.commit()

            print(f'El stock del producto con ID {id_producto} ha sido actualizado a {nueva_cantidad} unidades.')

            continuar = input("¿Desea continuar con la actualización de otro Producto? (si/no): ")
            if continuar.lower() != 'si':
                print("Proceso cancelado, volviendo al menú.")
                return False

            return True

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False

    def visualizarProductos(self) -> bool:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

        # Mostrar productos existentes con cantidad, precio y bodega
            consulta = """
                SELECT p.nombre, p.cantidad, p.valor_unitario, b.nombre AS nombre_bodega
                FROM producto p
                LEFT JOIN bodega b ON p.id_producto = b.fk_id_producto
            """
            Conexion.cursor.execute(consulta)
            productos = Conexion.cursor.fetchall()

            if not productos:
                print("No hay productos registrados.")
                time.sleep(3)
                return False

        # Mostrar productos en una tabla simple
            print(f"{'Nombre':<30} {'Cantidad':<10} {'Precio':<10} {'Bodega':<20}")
            print("=" * 80)
            for producto in productos:
                nombre_producto = producto[0]
                cantidad = producto[1]
                precio = producto[2]
                bodega = producto[3] if producto[3] else "Sin asignar"
                print(f"{nombre_producto:<30} {cantidad:<10} {precio:<10} {bodega:<20}")

            input("\nPresione cualquier tecla para salir.")

            return True

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False


    def eliminarProducto(self) -> bool:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

        # Solicitar al usuario el ID del producto a eliminar
            id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))

        # Verificar si el producto existe
            Conexion.cursor.execute("SELECT COUNT(*) FROM producto WHERE id_producto = %s", (id_producto,))
            if Conexion.cursor.fetchone()[0] == 0:
                print("El producto no existe.")
                return False

            # Eliminar las referencias en la tabla bodega
            Conexion.cursor.execute("DELETE FROM bodega WHERE fk_id_producto = %s", (id_producto,))
            Conexion.connection.commit()

        # Eliminar el producto
            Conexion.cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))
            Conexion.connection.commit()

            print(f"El producto con ID {id_producto} ha sido eliminado correctamente.")
            return True

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False
        

    def mostrarProductos(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
        
        # Solicitar al usuario el nombre del producto a buscar
            nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")

        # Consulta para obtener nombre, cantidad, precio y bodega del producto
            consulta = """
                SELECT p.nombre, p.cantidad, p.valor_unitario, b.nombre AS nombre_bodega
                FROM producto p
                LEFT JOIN bodega b ON p.id_producto = b.fk_id_producto
                WHERE p.nombre LIKE %s
            """
            Conexion.cursor.execute(consulta, ('%' + nombre_buscar + '%',))
            productos = Conexion.cursor.fetchall()

            if not productos:
                print("\nNo se encontraron productos con ese nombre.")
            else:
                print("\nProductos encontrados:")
                print(f"{'Nombre':<30} {'Cantidad':<10} {'Precio':<10} {'Bodega':<20}")
                print("="*80)
                for producto in productos:
                    nombre_producto = producto[0]
                    cantidad = producto[1]
                    precio = producto[2]
                    bodega = producto[3] if producto[3] else "Sin asignar"
                    print(f"{nombre_producto:<30} {cantidad:<10} {precio:<10} {bodega:<20}")

            input("\nPresione cualquier tecla para continuar...")

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False



    def eliminarProducto(self) -> bool:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

        # Mostrar los productos
            Conexion.cursor.execute("SELECT id_producto, nombre, cantidad FROM producto")
            productos = Conexion.cursor.fetchall()

            print("\nProductos disponibles:")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}")

            input("\nPresione cualquier tecla para continuar...")

        # Solicitar al usuario el ID del producto a eliminar
            id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))

        # Verificar si el producto existe
            Conexion.cursor.execute("SELECT COUNT(*) FROM producto WHERE id_producto = %s", (id_producto,))
            if Conexion.cursor.fetchone()[0] == 0:
                print("El producto no existe.")
                return False

        # Confirmación de eliminación
            confirmar = input(f"¿Está seguro de que desea eliminar el producto con ID {id_producto}? (si/no): ")
            if confirmar.lower() != 'si':
                print("Proceso cancelado, volviendo al menú.")
                return False

        # Eliminar las referencias en la tabla bodega
            Conexion.cursor.execute("DELETE FROM bodega WHERE fk_id_producto = %s", (id_producto,))
            Conexion.connection.commit()

        # Eliminar el producto
            Conexion.cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))
            Conexion.connection.commit()

            print(f"El producto con ID {id_producto} ha sido eliminado correctamente.")
            time.sleep(3)
            return True

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False
