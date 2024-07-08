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

    def realizarVentaConBoleta(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
        
            Conexion.cursor.execute("SELECT COUNT(*) FROM vendedor WHERE state_at = 'n'")
            vendedores_cerrados = Conexion.cursor.fetchone()[0]

            Conexion.cursor.execute("SELECT COUNT(*) FROM jefe_ventas WHERE state_at = 'n'")
            jefes_ventas_cerrados = Conexion.cursor.fetchone()[0]

            if vendedores_cerrados > 0 or jefes_ventas_cerrados > 0:
                print("Debe abrir ventas para poder continuar.")
                time.sleep(3)
                return

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
                
                    direccion_cliente = input("Ingrese la dirección del cliente: ")

                # Insertar nuevo cliente
                    Conexion.cursor.execute(
                        "INSERT INTO cliente (rut_cliente, nombre_cliente, direccion_cliente, CREATEDAT, UPDATEDAT) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                        (rut_cliente, nombre_cliente, direccion_cliente)
                    )
                    Conexion.connection.commit()
                    print("Cliente registrado correctamente.")

                # Solicitar teléfono del cliente
                    telefono_cliente = input("Ingrese el teléfono del cliente: ")

                # Insertar teléfono del cliente
                    Conexion.cursor.execute(
                        "INSERT INTO telefono_cliente (telefono, fk_rut_cliente, CREATEDAT, UPDATEDAT) VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                        (telefono_cliente, rut_cliente)
                    )
                    Conexion.connection.commit()
                    print("Teléfono registrado correctamente.")

                # Solicitar email del cliente
                    email_cliente = input("Ingrese el email del cliente: ")

                # Insertar email del cliente
                    Conexion.cursor.execute(
                        "INSERT INTO email_cliente (email, fk_rut_cliente, CREATEDAT, UPDATEDAT) VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                        (email_cliente, rut_cliente)
                    )
                    Conexion.connection.commit()
                    print("Email registrado correctamente.")

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
            print("Imprimiendo boleta")
            time.sleep(3)

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            print('Error de formato porfavor inicie nuevamente el proceso')
            time.sleep(3)
            return False


    def realizarVentaConFactura(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
        
            Conexion.cursor.execute("SELECT COUNT(*) FROM vendedor WHERE state_at = 'n'")
            vendedores_cerrados = Conexion.cursor.fetchone()[0]

            Conexion.cursor.execute("SELECT COUNT(*) FROM jefe_ventas WHERE state_at = 'n'")
            jefes_ventas_cerrados = Conexion.cursor.fetchone()[0]

            if vendedores_cerrados > 0 or jefes_ventas_cerrados > 0:
                print("Debe abrir ventas para poder continuar.")
                time.sleep(3)
                return

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
                
                    direccion_cliente = input("Ingrese la dirección del cliente: ")

                # Insertar nuevo cliente
                    Conexion.cursor.execute(
                        "INSERT INTO cliente (rut_cliente, nombre_cliente, direccion_cliente, CREATEDAT, UPDATEDAT) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                        (rut_cliente, nombre_cliente, direccion_cliente)
                    )
                    Conexion.connection.commit()
                    print("Cliente registrado correctamente.")

                    # Solicitar teléfono del cliente
                    telefono_cliente = input("Ingrese el teléfono del cliente: ")

                    # Insertar teléfono del cliente
                    Conexion.cursor.execute(
                        "INSERT INTO telefono_cliente (telefono, fk_rut_cliente, CREATEDAT, UPDATEDAT) VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                        (telefono_cliente, rut_cliente)
                    )
                    Conexion.connection.commit()
                    print("Teléfono registrado correctamente.")

                # Solicitar email del cliente
                    email_cliente = input("Ingrese el email del cliente: ")

                # Insertar email del cliente
                    Conexion.cursor.execute(
                        "INSERT INTO email_cliente (email, fk_rut_cliente, CREATEDAT, UPDATEDAT) VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                        (email_cliente, rut_cliente)
                    )
                    Conexion.connection.commit()
                    print("Email registrado correctamente.")

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
            print('Error de formato porfavor inicie nuevamente el proceso')
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
            print('Error de formato porfavor inicie nuevamente el proceso')
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
            print('Error de formato porfavor inicie nuevamente el proceso')
            time.sleep(3)
            return False
        

    def mostrar_mis_datos_vendedor(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
        
            nombre = input("Ingrese el nombre del vendedor: ")
        
        # Consulta para obtener datos del vendedor
            consulta = "SELECT id_vendedor, nombre FROM vendedor WHERE nombre=%s"
            Conexion.cursor.execute(consulta, (nombre,))
            vendedor = Conexion.cursor.fetchone()
        
            if vendedor:
                id_vendedor, nombre_vendedor = vendedor
                print(f"ID: {id_vendedor}, Nombre: {nombre_vendedor}")
                time.sleep(5)
            else:
                print("Vendedor no encontrado.")
                time.sleep(3)

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            print('Error de formato porfavor inicie nuevamente el proceso')
            time.sleep(3)
            return False


    def buscar_cliente_y_compras(self):
        try:
            Conexion.getConnection()
            if Conexion.cursor is None:
                raise Exception("Error en la conexión a la base de datos.")
        
        # Paso 1: Pedir al usuario que ingrese el rut del cliente
            rut_cliente = input("Ingrese el rut del cliente: ")
        
        # Buscar al cliente por su rut
            Conexion.cursor.execute("SELECT * FROM cliente WHERE rut_cliente = %s", (rut_cliente,))
            cliente = Conexion.cursor.fetchone()
        
            if not cliente:
                print(f"No se encontró ningún cliente con rut {rut_cliente}.")
                time.sleep(3)
                return False
        
            print(f"Cliente encontrado - Rut: {cliente[0]}, Nombre: {cliente[2]}, Dirección: {cliente[1]}")
        
        # Paso 2: Pedir al usuario que ingrese el id de la boleta o factura
            id_venta = input("Ingrese el ID de la boleta o factura: ")
        
        # Mostrar detalles de la compra (detalle_venta) con nombre del producto
            print("\nDetalles de la compra:")
            consulta = """
                SELECT dv.id_producto, p.nombre, dv.cantidad
                FROM detalle_venta dv
                INNER JOIN producto p ON dv.id_producto = p.id_producto
                WHERE dv.id_venta_boleta = %s OR dv.id_venta_factura = %s
            """
            Conexion.cursor.execute(consulta, (id_venta, id_venta))
            detalles_venta = Conexion.cursor.fetchall()
        
            if detalles_venta:
                print(f"{'ID Producto':<15}{'Nombre Producto':<30}{'Cantidad':<10}")
                print("="*55)
                for detalle in detalles_venta:
                    print(f"{detalle[0]:<15}{detalle[1]:<30}{detalle[2]:<10}")
            else:
                print("No se encontraron detalles de la compra.")
        
        # Esperar a que el usuario presione Enter para continuar
            input("\nPresione Enter para continuar...")
        
            return True

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
            print('Error de formato porfavor inicie nuevamente el proceso')
            time.sleep(3)
            return False



