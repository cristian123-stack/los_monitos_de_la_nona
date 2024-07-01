from jefeventas import JefeVentas 
from conexion import Conexion
import time
import hashlib
from datetime import datetime

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

        # Mostrar los proveedores existentes
            Conexion.cursor.execute("SELECT rut_prov, nombre FROM proveedor")
            proveedores = Conexion.cursor.fetchall()

            if proveedores:
                print("Proveedores registrados:")
                for proveedor in proveedores:
                    print(f"RUT: {proveedor[0]}, Nombre: {proveedor[1]}")
                usar_proveedor_existente = input("¿Desea usar un proveedor existente? (si/no): ")
            else:
                print("No hay proveedores registrados. Debe crear uno.")
                usar_proveedor_existente = 'no'

            if usar_proveedor_existente.lower() == 'si':
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

        # Selección de la bodega
            Conexion.cursor.execute("SELECT id_bodega, nombre FROM bodega")
            bodegas = Conexion.cursor.fetchall()

            if bodegas:
                print("Bodegas disponibles:")
                for bodega in bodegas:
                    print(f"ID: {bodega[0]}, Nombre: {bodega[1]}")
                id_bodega = int(input("Ingrese el ID de la bodega donde se almacenará el producto: "))
            else:
                print("No hay bodegas registradas. Debe crear una.")
                nombre_bodega = input("Ingrese el nombre de la nueva bodega: ")
                direccion_bodega = input("Ingrese la dirección de la nueva bodega: ")

            # Inserción de la nueva bodega en la tabla bodega
                sentencia_bodega = """
                    INSERT INTO bodega
                    (nombre, direccion, CREATEDAT, UPDATEDAT)
                    VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """
                valores_bodega = (nombre_bodega, direccion_bodega)
                Conexion.cursor.execute(sentencia_bodega, valores_bodega)
                Conexion.connection.commit()

                print(f'Se ha registrado la nueva bodega: {nombre_bodega}')

            # Obtener el id de la bodega recién insertada
                Conexion.cursor.execute("SELECT id_bodega FROM bodega WHERE nombre=%s ORDER BY CREATEDAT DESC LIMIT 1", (nombre_bodega,))
                id_bodega = Conexion.cursor.fetchone()[0]

        # Inserción en la tabla bodega_producto
            sentencia_bodega_producto = """
                INSERT INTO bodega_producto
                (fk_id_bodega, fk_id_producto, cantidad)
                VALUES (%s, %s, %s)
            """
            valores_bodega_producto = (id_bodega, id_producto, cantidad)
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

            while True:
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

            # Ejecutar la actualización del producto
                Conexion.cursor.execute(sentencia_actualizacion, tuple(valores_a_actualizar))
                Conexion.connection.commit()

            # Actualizar la bodega
                actualizar_bodega = input("¿Desea actualizar la bodega del producto? (si/no): ")
                if actualizar_bodega.lower() == 'si':
                    Conexion.cursor.execute("SELECT id_bodega, nombre FROM bodega")
                    bodegas = Conexion.cursor.fetchall()

                    if not bodegas:
                        print("No hay bodegas registradas.")
                        return False

                    print("Bodegas registradas:")
                    for bodega in bodegas:
                        print(f"ID: {bodega[0]}, Nombre: {bodega[1]}")

                    id_bodega = int(input("Ingrese el ID de la nueva bodega para el producto: "))

                # Actualizar la bodega con el producto
                    sentencia_bodega = """
                        UPDATE bodega
                        SET fk_id_producto=%s, UPDATEDAT=CURRENT_TIMESTAMP
                        WHERE id_bodega=%s
                    """
                    valores_bodega = (id_producto, id_bodega)
                    Conexion.cursor.execute(sentencia_bodega, valores_bodega)
                    Conexion.connection.commit()

                    print(f'El producto con ID {id_producto} ha sido actualizado y asignado a la bodega con ID: {id_bodega}')
                    time.sleep(5)
                else:
                    print(f'El producto con ID {id_producto} ha sido actualizado correctamente.')
                    time.sleep(5)

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

        # Consulta para obtener productos con sus bodegas
            consulta = """
                SELECT p.id_producto, p.nombre, p.cantidad, p.valor_unitario, 
                   IFNULL(b.nombre, 'Sin asignar') as bodega
                    FROM producto p
                    LEFT JOIN bodega_producto bp ON p.id_producto = bp.fk_id_producto
                    LEFT JOIN bodega b ON bp.fk_id_bodega = b.id_bodega
                """
            Conexion.cursor.execute(consulta)
            productos = Conexion.cursor.fetchall()

            if not productos:
                print("No hay productos registrados.")
                time.sleep(3)
                return False

        # Mostrar productos en una tabla simple
            print(f"{'Nombre':<30}{'Cantidad':<10}{'Precio':<10}{'Bodega':<20}")
            print("="*70)
            for producto in productos:
                print(f"{producto[1]:<30}{producto[2]:<10}{producto[3]:<10}{producto[4]:<20}")

        # Pausa para que el usuario pueda ver los productos
            input("Presione cualquier tecla para salir.")
            return True

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            return False



    def eliminarProducto(self) -> bool:
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

        # Mostrar productos existentes
            Conexion.cursor.execute("""
                SELECT p.id_producto, p.nombre, p.cantidad, p.valor_unitario, b.nombre AS bodega
                FROM producto p
                LEFT JOIN bodega_producto bp ON p.id_producto = bp.fk_id_producto
                LEFT JOIN bodega b ON bp.fk_id_bodega = b.id_bodega
            """)
            productos = Conexion.cursor.fetchall()

            if not productos:
                print("No hay productos registrados.")
                return False

            print("Productos registrados:")
            print(f"{'ID':<10}{'Nombre':<30}{'Cantidad':<10}{'Precio':<10}{'Bodega':<15}")
            print("="*75)
            for producto in productos:
                bodega = producto[4] if producto[4] else "Sin asignar"
                print(f"{producto[0]:<10}{producto[1]:<30}{producto[2]:<10}{producto[3]:<10}{bodega:<15}")

            id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))

        # Verificar si el producto existe
            Conexion.cursor.execute("SELECT COUNT(*) FROM producto WHERE id_producto=%s", (id_producto,))
            producto_existe = Conexion.cursor.fetchone()[0] > 0

            if not producto_existe:
                print("El producto no existe.")
                return False

            confirmar = input("¿Está seguro de que desea eliminar el producto? (si/no): ")
            if confirmar.lower() != 'si':
                print("Proceso cancelado, volviendo al menú.")
                return False

        # Eliminar registros de la tabla bodega_producto
            Conexion.cursor.execute("DELETE FROM bodega_producto WHERE fk_id_producto=%s", (id_producto,))
            Conexion.connection.commit()

        # Eliminar el producto
            Conexion.cursor.execute("DELETE FROM producto WHERE id_producto=%s", (id_producto,))
            Conexion.connection.commit()

            print(f'El producto con ID {id_producto} ha sido eliminado correctamente.')
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


    def realizarVentaConBoleta(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

            # Solicitar ID del vendedor
            id_vendedor = input("Ingrese el ID del vendedor que realiza la venta: ")
            
            # Verificar si el vendedor existe
            Conexion.cursor.execute("SELECT COUNT(*) FROM vendedor WHERE id_vendedor=%s", (id_vendedor,))
            if Conexion.cursor.fetchone()[0] == 0:
                print("ID de vendedor no válido.")
                time.sleep(3)
                return

            # Solicitar RUT del cliente
            rut_cliente = input("Ingrese el Rut del cliente (dejar en blanco si no tiene): ")
            if rut_cliente:
                # Verificar si el cliente existe
                Conexion.cursor.execute("SELECT nombre_cliente FROM cliente WHERE rut_cliente=%s", (rut_cliente,))
                cliente = Conexion.cursor.fetchone()
                if cliente:
                    print(f"Cliente encontrado: {cliente[0]}")
                else:
                    # Solicitar datos del nuevo cliente
                    nombre_cliente = input("Ingrese el nombre del cliente: ")
                    if len(rut_cliente) > 10:
                        print("El RUT no debe tener más de 10 caracteres.")
                        time.sleep(3)
                        return

                    # Insertar nuevo cliente
                    Conexion.cursor.execute(
                        "INSERT INTO cliente (rut_cliente, nombre_cliente, CREATEDAT, UPDATEDAT) VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                        (rut_cliente, nombre_cliente)
                    )
                    Conexion.connection.commit()
                    print("Cliente registrado correctamente.")
                    time.sleep(3)
            else:
                rut_cliente = None

            # Mostrar productos disponibles
            Conexion.cursor.execute("SELECT id_producto, nombre, valor_unitario, cantidad FROM producto WHERE cantidad > 0")
            productos = Conexion.cursor.fetchall()
            print("Productos disponibles:")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad disponible: {producto[3]}")

            # Solicitar productos a vender
            detalle_venta = []
            while True:
                id_producto = input("Ingrese el ID del producto a vender (fin para terminar): ")
                if id_producto.lower() == 'fin':
                    break

                # Verificar si el producto existe y tiene stock suficiente
                Conexion.cursor.execute("SELECT nombre, valor_unitario, cantidad FROM producto WHERE id_producto=%s", (id_producto,))
                producto = Conexion.cursor.fetchone()
                if producto:
                    nombre_producto, valor_unitario, stock = producto
                    cantidad = int(input(f"Ingrese la cantidad de '{nombre_producto}' a vender: "))
                    if cantidad > stock:
                        print("Cantidad insuficiente en el stock.")
                        continue

                    detalle_venta.append((id_producto, cantidad))
                else:
                    print("ID de producto no válido.")

            # Confirmar venta
            confirmar = input("¿Desea confirmar la venta? (si/no): ").lower()
            if confirmar != 'si':
                print("Venta cancelada.")
                time.sleep(3)
                return

            # Calcular totales
            subtotal = 0
            for id_producto, cantidad in detalle_venta:
                Conexion.cursor.execute("SELECT valor_unitario FROM producto WHERE id_producto=%s", (id_producto,))
                valor_unitario = Conexion.cursor.fetchone()[0]
                subtotal += valor_unitario * cantidad
            iva = int(subtotal * 0.19)
            total = subtotal + iva
            fecha_venta = time.strftime('%Y-%m-%d')

            # Insertar boleta
            Conexion.cursor.execute(
                "INSERT INTO boleta (fk_id_vendedor, fk_id_cliente, subtotal, iva, total, fecha, CREATEDAT, UPDATEDAT) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (id_vendedor, rut_cliente, subtotal, iva, total, fecha_venta)
            )
            Conexion.connection.commit()

            # Obtener el ID de la boleta insertada
            id_boleta = Conexion.cursor.lastrowid

            # Insertar detalles de la venta
            for id_producto, cantidad in detalle_venta:
                Conexion.cursor.execute(
                    "INSERT INTO detalle_venta (id_venta_boleta, id_producto, cantidad, CREATEDAT, UPDATEDAT) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                    (id_boleta, id_producto, cantidad)
                )
            Conexion.connection.commit()

            # Descontar productos del stock
            for id_producto, cantidad in detalle_venta:
                Conexion.cursor.execute(
                    "UPDATE producto SET cantidad = cantidad - %s WHERE id_producto = %s",
                    (cantidad, id_producto)
                )
            Conexion.connection.commit()

            # Mostrar boleta detallada
            print("\nBoleta Detallada:")
            print("===================================")
            for id_producto, cantidad in detalle_venta:
                Conexion.cursor.execute("SELECT nombre, valor_unitario FROM producto WHERE id_producto=%s", (id_producto,))
                producto = Conexion.cursor.fetchone()
                nombre_producto, valor_unitario = producto
                subtotal_producto = cantidad * valor_unitario
                print(f"Producto ID: {id_producto}, Nombre: {nombre_producto}")
                print(f"Cantidad: {cantidad}")
                print(f"Subtotal Producto: ${subtotal_producto}")
                print("-----------------------------------")
            print(f"Subtotal: ${subtotal}")
            print(f"IVA (19.0%): ${iva}")
            print(f"Total: ${total}")
            print("===================================")
            input("Presione Enter para imprimir...")
            print("Impriendo boleta")
            time.sleep(3)

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            time.sleep(3)
            return False
        
    def realizarVentaConFactura(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

            # Solicitar ID del vendedor
            id_vendedor = input("Ingrese el ID del vendedor que realiza la venta: ")
            
            # Verificar si el vendedor existe
            Conexion.cursor.execute("SELECT COUNT(*) FROM vendedor WHERE id_vendedor=%s", (id_vendedor,))
            if Conexion.cursor.fetchone()[0] == 0:
                print("ID de vendedor no válido.")
                time.sleep(3)
                return

            # Solicitar RUT del cliente
            rut_cliente = input("Ingrese el Rut del cliente (dejar en blanco si no tiene): ")
            if rut_cliente:
                # Verificar si el cliente existe
                Conexion.cursor.execute("SELECT nombre_cliente FROM cliente WHERE rut_cliente=%s", (rut_cliente,))
                cliente = Conexion.cursor.fetchone()
                if cliente:
                    print(f"Cliente encontrado: {cliente[0]}")
                else:
                    # Solicitar datos del nuevo cliente
                    nombre_cliente = input("Ingrese el nombre del cliente: ")
                    if len(rut_cliente) > 10:
                        print("El RUT no debe tener más de 10 caracteres.")
                        time.sleep(3)
                        return

                    # Insertar nuevo cliente
                    Conexion.cursor.execute(
                        "INSERT INTO cliente (rut_cliente, nombre_cliente, CREATEDAT, UPDATEDAT) VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                        (rut_cliente, nombre_cliente)
                    )
                    Conexion.connection.commit()
                    print("Cliente registrado correctamente.")
                    time.sleep(3)
            else:
                rut_cliente = None

            # Mostrar productos disponibles
            Conexion.cursor.execute("SELECT id_producto, nombre, valor_unitario, cantidad FROM producto WHERE cantidad > 0")
            productos = Conexion.cursor.fetchall()
            print("Productos disponibles:")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad disponible: {producto[3]}")

            # Solicitar productos a vender
            detalle_venta = []
            while True:
                id_producto = input("Ingrese el ID del producto a vender (fin para terminar): ")
                if id_producto.lower() == 'fin':
                    break

                # Verificar si el producto existe y tiene stock suficiente
                Conexion.cursor.execute("SELECT nombre, valor_unitario, cantidad FROM producto WHERE id_producto=%s", (id_producto,))
                producto = Conexion.cursor.fetchone()
                if producto:
                    nombre_producto, valor_unitario, stock = producto
                    cantidad = int(input(f"Ingrese la cantidad de '{nombre_producto}' a vender: "))
                    if cantidad > stock:
                        print("Cantidad insuficiente en el stock.")
                        continue

                    detalle_venta.append((id_producto, cantidad))
                else:
                    print("ID de producto no válido.")

            # Confirmar venta
            confirmar = input("¿Desea confirmar la venta? (si/no): ").lower()
            if confirmar != 'si':
                print("Venta cancelada.")
                time.sleep(3)
                return

            # Calcular totales
            subtotal = 0
            for id_producto, cantidad in detalle_venta:
                Conexion.cursor.execute("SELECT valor_unitario FROM producto WHERE id_producto=%s", (id_producto,))
                valor_unitario = Conexion.cursor.fetchone()[0]
                subtotal += valor_unitario * cantidad
            iva = int(subtotal * 0.19)
            total = subtotal + iva
            fecha_venta = time.strftime('%Y-%m-%d')

            # Insertar factura
            Conexion.cursor.execute(
                "INSERT INTO factura (fk_id_vendedor, fk_id_cliente, subtotal, iva, total, fecha, CREATEDAT, UPDATEDAT) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (id_vendedor, rut_cliente, subtotal, iva, total, fecha_venta)
            )
            Conexion.connection.commit()

            # Obtener el ID de la factura insertada
            id_factura = Conexion.cursor.lastrowid

            # Insertar detalles de la venta
            for id_producto, cantidad in detalle_venta:
                Conexion.cursor.execute(
                    "INSERT INTO detalle_venta (id_venta_factura, id_producto, cantidad, CREATEDAT, UPDATEDAT) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                    (id_factura, id_producto, cantidad)
                )
            Conexion.connection.commit()

            # Descontar productos del stock
            for id_producto, cantidad in detalle_venta:
                Conexion.cursor.execute(
                    "UPDATE producto SET cantidad = cantidad - %s WHERE id_producto = %s",
                    (cantidad, id_producto)
                )
            Conexion.connection.commit()

            # Mostrar factura detallada
            print("\nFactura Detallada:")
            print("===================================")
            for id_producto, cantidad in detalle_venta:
                Conexion.cursor.execute("SELECT nombre, valor_unitario FROM producto WHERE id_producto=%s", (id_producto,))
                producto = Conexion.cursor.fetchone()
                nombre_producto, valor_unitario = producto
                subtotal_producto = cantidad * valor_unitario
                print(f"Producto ID: {id_producto}, Nombre: {nombre_producto}")
                print(f"Cantidad: {cantidad}")
                print(f"Subtotal Producto: ${subtotal_producto}")
                print("-----------------------------------")
            print(f"Subtotal: ${subtotal}")
            print(f"IVA (19.0%): ${iva}")
            print(f"Total: ${total}")
            print("===================================")
            input("Presione Enter para imprimir...")
            print("Imprimiendo factura")
            time.sleep(3)

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            time.sleep(3)
            return False


    def realizarDevolucionBoleta(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

        # Solicitar ID del vendedor
            id_vendedor = input("Ingrese el ID del vendedor que realiza la devolución: ")
        
        # Verificar si el vendedor existe
            Conexion.cursor.execute("SELECT COUNT(*) FROM vendedor WHERE id_vendedor=%s", (id_vendedor,))
            if Conexion.cursor.fetchone()[0] == 0:
                print("ID de vendedor no válido.")
                time.sleep(3)
                return

        # Solicitar RUT del cliente
            rut_cliente = input("Ingrese el Rut del cliente (dejar en blanco si no tiene): ")
            if rut_cliente:
            # Verificar si el cliente existe
                Conexion.cursor.execute("SELECT nombre_cliente FROM cliente WHERE rut_cliente=%s", (rut_cliente,))
                cliente = Conexion.cursor.fetchone()
                if cliente:
                    print(f"Cliente encontrado: {cliente[0]}")
                else:
                    print("Cliente no encontrado.")
                    time.sleep(3)
                    return
            else:
                rut_cliente = None

        # Mostrar productos vendidos por el cliente mediante boleta
            Conexion.cursor.execute(
                "SELECT dv.id_detalle_venta, dv.id_producto, p.nombre, dv.cantidad, b.id_venta_boleta "
                "FROM detalle_venta dv "
                "JOIN producto p ON dv.id_producto = p.id_producto "
                "JOIN boleta b ON dv.id_venta_boleta = b.id_venta_boleta "
                "WHERE b.fk_id_vendedor = %s AND b.fk_id_cliente = %s",
                (id_vendedor, rut_cliente)
            )
            detalle_venta = Conexion.cursor.fetchall()
            if not detalle_venta:
                print("No se encontraron productos vendidos por este cliente mediante boleta.")
                time.sleep(3)
                return

        # Mostrar detalle de productos vendidos por boleta
            print("Productos vendidos por el cliente mediante boleta:")
            for detalle in detalle_venta:
                print(f"ID Detalle Venta: {detalle[0]}, ID Producto: {detalle[1]}, Nombre Producto: {detalle[2]}, Cantidad: {detalle[3]}, Boleta ID: {detalle[4]}")

        # Solicitar detalles de la devolución de boleta
            detalle_devolucion = []
            while True:
                id_detalle_venta = input("Ingrese el ID del detalle de venta a devolver (fin para terminar): ")
                if id_detalle_venta.lower() == 'fin':
                    break

            # Verificar si el detalle de venta existe y pertenece al cliente
                Conexion.cursor.execute(
                    "SELECT dv.id_producto, p.nombre, dv.cantidad, b.id_venta_boleta "
                    "FROM detalle_venta dv "
                    "JOIN producto p ON dv.id_producto = p.id_producto "
                    "JOIN boleta b ON dv.id_venta_boleta = b.id_venta_boleta "
                    "WHERE dv.id_detalle_venta = %s AND b.fk_id_vendedor = %s AND b.fk_id_cliente = %s",
                    (id_detalle_venta, id_vendedor, rut_cliente)
                )
                detalle = Conexion.cursor.fetchone()
                if detalle:
                    id_producto, nombre_producto, cantidad, id_boleta = detalle
                    detalle_devolucion.append((id_detalle_venta, id_producto, nombre_producto, cantidad, id_boleta))
                else:
                    print("ID de detalle de venta no válido o no pertenece al cliente seleccionado.")

        # Solicitar motivo de la devolución de boleta
            motivo = input("Ingrese el motivo de la devolución: ")

        # Confirmar devolución
            confirmar = input("¿Desea confirmar la devolución? (si/no): ").lower()
            if confirmar != 'si':
                print("Devolución cancelada.")
                time.sleep(3)
                return

        # Calcular subtotal y total de la devolución de boleta
            subtotal_devolucion = 0
            for detalle in detalle_devolucion:
                id_detalle_venta, id_producto, nombre_producto, cantidad, id_boleta = detalle
                Conexion.cursor.execute("SELECT valor_unitario FROM producto WHERE id_producto = %s", (id_producto,))
                valor_unitario = Conexion.cursor.fetchone()[0]
                subtotal_producto = valor_unitario * cantidad
                subtotal_devolucion += subtotal_producto

            # Devolver productos al inventario
                Conexion.cursor.execute(
                    "UPDATE producto SET cantidad = cantidad + %s WHERE id_producto = %s",
                    (cantidad, id_producto)
                )
                Conexion.connection.commit()

            iva_devolucion = subtotal_devolucion * 0.19
            total_devolucion = subtotal_devolucion + iva_devolucion

        # Insertar nota de crédito de boleta
            fecha_devolucion = time.strftime('%Y-%m-%d')
            insert_nota_credito = (
                "INSERT INTO nota_credito (fk_id_vendedor, fk_id_cliente, fk_id_boleta, subtotal, iva, total, motivo, fecha) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            )
            Conexion.cursor.execute(insert_nota_credito, (id_vendedor, rut_cliente, id_boleta, subtotal_devolucion, iva_devolucion, total_devolucion, motivo, fecha_devolucion))
            Conexion.connection.commit()

        # Obtener el ID de la nota de crédito insertada
            id_nota_credito = Conexion.cursor.lastrowid

        # Insertar detalles de la devolución de boleta en detalle_venta
            for id_detalle_venta, id_producto, nombre_producto, cantidad, id_boleta in detalle_devolucion:
                Conexion.cursor.execute(
                    "INSERT INTO detalle_venta (id_nota_credito, id_venta_boleta, id_producto, cantidad, CREATEDAT, UPDATEDAT) "
                    "VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                    (id_nota_credito, id_boleta, id_producto, cantidad)
                )
            Conexion.connection.commit()

        # Mostrar nota de crédito detallada de boleta
            print("\nNota de Crédito Detallada de Boleta:")
            print("===================================")
            print(f"Subtotal de Devolución: ${subtotal_devolucion}")
            print(f"IVA de Devolución (19.0%): ${iva_devolucion}")
            print(f"Total de Devolución: ${total_devolucion}")
            print(f"Motivo de la devolución: {motivo}")
            print("===================================")
            input("Presione Enter para imprimir...")
            print("Imprimiendo nota de crédito de boleta")
            time.sleep(3)

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            time.sleep(3)
            return False
        
        

    def realizarDevolucionFactura(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

        # Solicitar ID del vendedor
            id_vendedor = input("Ingrese el ID del vendedor que realiza la devolución: ")
        
        # Verificar si el vendedor existe
            Conexion.cursor.execute("SELECT COUNT(*) FROM vendedor WHERE id_vendedor=%s", (id_vendedor,))
            if Conexion.cursor.fetchone()[0] == 0:
                print("ID de vendedor no válido.")
                time.sleep(3)
                return

        # Solicitar RUT del cliente
            rut_cliente = input("Ingrese el Rut del cliente (dejar en blanco si no tiene): ")
            if rut_cliente:
            # Verificar si el cliente existe
                Conexion.cursor.execute("SELECT nombre_cliente FROM cliente WHERE rut_cliente=%s", (rut_cliente,))
                cliente = Conexion.cursor.fetchone()
                if cliente:
                    print(f"Cliente encontrado: {cliente[0]}")
                else:
                    print("Cliente no encontrado.")
                    time.sleep(3)
                    return
            else:
                rut_cliente = None

        # Mostrar productos vendidos por el cliente mediante factura
            Conexion.cursor.execute(
                "SELECT dv.id_detalle_venta, dv.id_producto, p.nombre, dv.cantidad, f.id_venta_factura "
                "FROM detalle_venta dv "
                "JOIN producto p ON dv.id_producto = p.id_producto "
                "JOIN factura f ON dv.id_venta_factura = f.id_venta_factura "
                "WHERE f.fk_id_vendedor = %s AND f.fk_id_cliente = %s",
                (id_vendedor, rut_cliente)
            )
            detalle_venta = Conexion.cursor.fetchall()
            if not detalle_venta:
                print("No se encontraron productos vendidos por este cliente mediante factura.")
                time.sleep(3)
                return

        # Mostrar detalle de productos vendidos por factura
            print("Productos vendidos por el cliente mediante factura:")
            for detalle in detalle_venta:
                print(f"ID Detalle Venta: {detalle[0]}, ID Producto: {detalle[1]}, Nombre Producto: {detalle[2]}, Cantidad: {detalle[3]}, Factura ID: {detalle[4]}")

        # Solicitar detalles de la devolución de factura
            detalle_devolucion = []
            while True:
                id_detalle_venta = input("Ingrese el ID del detalle de venta a devolver (fin para terminar): ")
                if id_detalle_venta.lower() == 'fin':
                    break

            # Verificar si el detalle de venta existe y pertenece al cliente
                Conexion.cursor.execute(
                    "SELECT dv.id_producto, p.nombre, dv.cantidad, f.id_venta_factura "
                    "FROM detalle_venta dv "
                    "JOIN producto p ON dv.id_producto = p.id_producto "
                    "JOIN factura f ON dv.id_venta_factura = f.id_venta_factura "
                    "WHERE dv.id_detalle_venta = %s AND f.fk_id_vendedor = %s AND f.fk_id_cliente = %s",
                    (id_detalle_venta, id_vendedor, rut_cliente)
                )
                detalle = Conexion.cursor.fetchone()
                if detalle:
                    id_producto, nombre_producto, cantidad, id_factura = detalle
                    detalle_devolucion.append((id_detalle_venta, id_producto, nombre_producto, cantidad, id_factura))
                else:
                    print("ID de detalle de venta no válido o no pertenece al cliente seleccionado.")

        # Solicitar motivo de la devolución de factura
            motivo = input("Ingrese el motivo de la devolución: ")

        # Confirmar devolución
            confirmar = input("¿Desea confirmar la devolución? (si/no): ").lower()
            if confirmar != 'si':
                print("Devolución cancelada.")
                time.sleep(3)
                return

        # Calcular subtotal y total de la devolución de factura
            subtotal_devolucion = 0
            for detalle in detalle_devolucion:
                id_detalle_venta, id_producto, nombre_producto, cantidad, id_factura = detalle
                Conexion.cursor.execute("SELECT valor_unitario FROM producto WHERE id_producto = %s", (id_producto,))
                valor_unitario = Conexion.cursor.fetchone()[0]
                subtotal_producto = valor_unitario * cantidad
                subtotal_devolucion += subtotal_producto

            # Devolver productos al inventario
                Conexion.cursor.execute(
                    "UPDATE producto SET cantidad = cantidad + %s WHERE id_producto = %s",
                    (cantidad, id_producto)
                )
                Conexion.connection.commit()

            iva_devolucion = subtotal_devolucion * 0.19
            total_devolucion = subtotal_devolucion + iva_devolucion

        # Insertar nota de crédito de factura
            fecha_devolucion = time.strftime('%Y-%m-%d')
            insert_nota_credito = (
                "INSERT INTO nota_credito (fk_id_vendedor, fk_id_cliente, fk_id_factura, subtotal, iva, total, motivo, fecha) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            )
            Conexion.cursor.execute(insert_nota_credito, (id_vendedor, rut_cliente, id_factura, subtotal_devolucion, iva_devolucion, total_devolucion, motivo, fecha_devolucion))
            Conexion.connection.commit()

        # Obtener el ID de la nota de crédito insertada
            id_nota_credito = Conexion.cursor.lastrowid

        # Insertar detalles de la devolución de factura en detalle_venta
            for id_detalle_venta, id_producto, nombre_producto, cantidad, id_factura in detalle_devolucion:
                Conexion.cursor.execute(
                    "INSERT INTO detalle_venta (id_nota_credito, id_venta_factura, id_producto, cantidad, CREATEDAT, UPDATEDAT) "
                    "VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                    (id_nota_credito, id_factura, id_producto, cantidad)
                )
            Conexion.connection.commit()

        # Mostrar nota de crédito detallada de factura
            print("\nNota de Crédito Detallada de Factura:")
            print("===================================")
            print(f"Subtotal de Devolución: ${subtotal_devolucion}")
            print(f"IVA de Devolución (19.0%): ${iva_devolucion}")
            print(f"Total de Devolución: ${total_devolucion}")
            print(f"Motivo de la devolución: {motivo}")
            print("===================================")
            input("Presione Enter para imprimir...")
            print("Imprimiendo nota de crédito de factura")
            time.sleep(3)

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            time.sleep(3)
            return False


    def mostrar_productos_caducidad_proxima(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

        # Fecha actual
            fecha_actual = datetime.now().date()

        # Consulta para obtener los productos con sus fechas de elaboración y caducidad
            Conexion.cursor.execute("SELECT id_producto, nombre, fecha_elaboracion, fecha_caducidad FROM producto")
            productos = Conexion.cursor.fetchall()

        # Lista para almacenar los productos con caducidad próxima
            productos_caducidad_proxima = []

        # Calcular los días restantes para cada producto
            for producto in productos:
                id_producto, nombre, fecha_elaboracion, fecha_caducidad = producto
                dias_restantes = (fecha_caducidad - fecha_elaboracion).days

                if dias_restantes <= 30:
                    productos_caducidad_proxima.append({
                        'id_producto': id_producto,
                        'nombre': nombre,
                        'dias_restantes': dias_restantes
                    })

        # Verificar si hay productos próximos a caducar
            if productos_caducidad_proxima:
                print("\nProductos con caducidad próxima:")
                print("===================================")
                for producto in productos_caducidad_proxima:
                    print(f"ID: {producto['id_producto']}, Nombre: {producto['nombre']}, Días restantes: {producto['dias_restantes']}")
                print("===================================")
            else:
                print("No hay productos que vayan a caducar en los próximos 30 días.")

            input("Presione Enter para continuar...")

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            time.sleep(3)
            return False
        
    def informe_ventas(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")

            # Solicitar fechas de inicio y fin
            fecha_inicio_str = input("Indique fecha de inicio (YYYY-MM-DD): ")
            fecha_final_str = input("Indique fecha final (YYYY-MM-DD): ")

            # Convertir cadenas a objetos de fecha
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
            fecha_final = datetime.strptime(fecha_final_str, '%Y-%m-%d').date()

            # Consulta para obtener el total de ventas con boletas y facturas
            Conexion.cursor.execute(
                "SELECT 'Boleta' AS tipo, COUNT(*) AS cantidad, SUM(total) AS total "
                "FROM boleta "
                "WHERE fecha BETWEEN %s AND %s "
                "UNION ALL "
                "SELECT 'Factura' AS tipo, COUNT(*) AS cantidad, SUM(total) AS total "
                "FROM factura "
                "WHERE fecha BETWEEN %s AND %s ",
                (fecha_inicio, fecha_final, fecha_inicio, fecha_final)
            )
            ventas = Conexion.cursor.fetchall()

            # Consulta para obtener el total de notas de crédito
            Conexion.cursor.execute(
                "SELECT COUNT(*) AS cantidad, SUM(total) AS total "
                "FROM nota_credito "
                "WHERE fecha BETWEEN %s AND %s",
                (fecha_inicio, fecha_final)
            )
            notas_credito = Conexion.cursor.fetchone()

            # Mostrar el informe de ventas
            print("\nInforme de Ventas:")
            print("===================")
            total_ventas = 0
            total_notas_credito = 0
            for venta in ventas:
                tipo, cantidad, total = venta
                if total is None:
                    total = 0
                print(f"{tipo}: Cantidad: {cantidad}, Total: {total}")
                total_ventas += total

            # Mostrar el total de notas de crédito
            if notas_credito:
                cantidad_nc, total_nc = notas_credito
                if total_nc is None:
                    total_nc = 0
                print(f"Notas de Crédito: Cantidad: {cantidad_nc}, Total: {total_nc}")
                total_notas_credito = total_nc
            else:
                print("Notas de Crédito: Cantidad: 0, Total: 0")

            neto_ventas = total_ventas - total_notas_credito
            print("===================")
            print(f"Total Ventas (con notas de crédito aplicadas): {neto_ventas}")

            # Preguntar si quiere desglosar
            desglose = input("¿Quiere desglosar? (si/no): ").lower()
            if desglose == 'si':
                print("\nDesglose de Ventas y Notas de Crédito:")
                print("=========================================")

                # Desglose de boletas
                Conexion.cursor.execute(
                    "SELECT id_venta_boleta, total, fecha "
                    "FROM boleta "
                    "WHERE fecha BETWEEN %s AND %s",
                    (fecha_inicio, fecha_final)
                )
                boletas = Conexion.cursor.fetchall()
                print("\nBoletas:")
                for boleta in boletas:
                    id_venta_boleta, total, fecha = boleta
                    print(f"ID: {id_venta_boleta}, Total: {total}, Fecha: {fecha}")

                # Desglose de facturas
                Conexion.cursor.execute(
                    "SELECT id_venta_factura, total, fecha "
                    "FROM factura "
                    "WHERE fecha BETWEEN %s AND %s",
                    (fecha_inicio, fecha_final)
                )
                facturas = Conexion.cursor.fetchall()
                print("\nFacturas:")
                for factura in facturas:
                    id_venta_factura, total, fecha = factura
                    print(f"ID: {id_venta_factura}, Total: {total}, Fecha: {fecha}")

                # Desglose de notas de crédito
                Conexion.cursor.execute(
                    "SELECT id_nota_credito, total, fecha, motivo "
                    "FROM nota_credito "
                    "WHERE fecha BETWEEN %s AND %s",
                    (fecha_inicio, fecha_final)
                )
                notas_credito_desglose = Conexion.cursor.fetchall()
                print("\nNotas de Crédito:")
                for nota_credito in notas_credito_desglose:
                    id_nota_credito, total, fecha, motivo = nota_credito
                    print(f"ID: {id_nota_credito}, Total: {total}, Fecha: {fecha}, Motivo: {motivo}")

                print("=========================================")
                input("Presione Enter para salir...")

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            print('Ingresa fechas validas')
            time.sleep(3)
            return False
