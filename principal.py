import os
import time
import getpass
import sys
from beautifultable import BeautifulTable
from adminDao import AdminDao
from jefeventasDao import JefeVentasDao
from vendedorDao import VendedorDao
from admin import administrador
from jefeventas import JefeVentas
from vendedor import Vendedor

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_inicio_sesion():
    cls()
    print("*****************************")
    print("*      INICIO DE SESIÓN     *")
    print("*****LOS MONITOS DE LA NONA*****")
    print("*****************************")

def mostrar_menu_admin():
    cls()
    print("*****************************")
    print("*  Menú de Administrador     *")
    print("*****************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Opciones Jefe de Ventas"])
    table.rows.append(["2", "Opciones Vendedor"])
    table.rows.append(["3", "Administración de Inventario"])
    table.rows.append(["4", "Opciones de Ventas"])
    table.rows.append(["5", "Menú de Gestión: Informes y Control de Ventas"])
    table.rows.append(["6", "Volver al inicio de sesión"])
    print(table)

def mostrar_menu_jefe_ventas():
    cls()
    print("*****************************")
    print("*  Menú de Jefe de Ventas    *")
    print("*****************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Administración de Productos"])
    table.rows.append(["2", "Opciones de Ventas"])
    table.rows.append(["3", "Menú de Gestión: Informes y Control de Ventas"])
    table.rows.append(["4", "Volver al inicio de sesión"])
    print(table)

def mostrar_menu_vendedor():
    cls()
    print("*****************************")
    print("*   Menú de Vendedor         *")
    print("*****************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Opciones de Ventas"])
    table.rows.append(["2", "Salir"])
    print(table)

def mostrar_submenu_jefe_ventas():
    cls()
    print("*****************************")
    print("*   Opciones Jefe de Ventas  *")
    print("*****************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Crear Jefe de Ventas"])
    table.rows.append(["2", "Actualizar Jefe de Ventas"])
    table.rows.append(["3", "Mostrar Jefes de Ventas"])
    table.rows.append(["4", "Eliminar Jefe de Ventas"])
    table.rows.append(["5", "Volver al menú anterior"])
    print(table)

def mostrar_submenu_vendedor():
    cls()
    print("*****************************")
    print("*     Opciones Vendedor      *")
    print("*****************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Crear Vendedor"])
    table.rows.append(["2", "Actualizar Vendedor"])
    table.rows.append(["3", "Mostrar Vendedores"])
    table.rows.append(["4", "Eliminar Vendedor"])
    table.rows.append(["5", "Volver al menú anterior"])
    print(table)

def mostrar_submenu_admin_inventario():
    cls()
    print("************************************")
    print("*   Opciones Administración Inventario   *")
    print("************************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Agregar Producto"])
    table.rows.append(["2", "Buscar producto"])
    table.rows.append(["3", "Actualizar Productos"])
    table.rows.append(["4", "Eliminar Producto"])
    table.rows.append(["5", "Actualizar stock Producto"])
    table.rows.append(["6", "Visualizar Inventario"])
    table.rows.append(["7", "Volver al menú anterior"])
    print(table)

def mostrar_submenu_ventas():
    cls()
    print("************************************")
    print("*   Opciones de Ventas   *")
    print("************************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Realizar Venta con Boleta"])
    table.rows.append(["2", "Realizar Venta con Factura"])
    table.rows.append(["3", "Realizar Devolución con Factura"])
    table.rows.append(["4", "Realizar Devolución con Boleta"])
    table.rows.append(["5", "Mostrar datos vendedor"])
    table.rows.append(["6", "Buscar clientes"])
    table.rows.append(["7", "Volver al menú anterior"])
    print(table)

def mostrar_submenu_informes_admin():
    cls()
    print("************************************")
    print("*   Menú de Gestión: Informes y Control de Ventas   *")
    print("************************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Informe de Ventas"])
    table.rows.append(["2", "Productos con Caducidad Próxima"])
    table.rows.append(["3", "Abrir ventas"])
    table.rows.append(["4", "Cerrar ventas"])
    table.rows.append(["5", "Mostrar datos jefe ventas"])
    table.rows.append(["6", "Crear bodegas"])
    table.rows.append(["7", "Volver al menú anterior"])
    print(table)

def mostrar_submenu_informes_jefe_ventas():
    cls()
    print("************************************")
    print("*   Menú de Gestión: Informes y Control de Ventas   *")
    print("************************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Informe de Ventas"])
    table.rows.append(["2", "Productos con Caducidad Próxima"])
    table.rows.append(["3", "Abrir ventas"])
    table.rows.append(["4", "Cerrar ventas"])
    table.rows.append(["5", "Mostrar datos jefe ventas"])
    table.rows.append(["6", "Crear bodegas"])
    table.rows.append(["7", "Volver al menú anterior"])
    print(table)

def opcion_ficticia():
    cls()
    print("Ejecutando opción ficticia...")
    time.sleep(2)

def main():
    dao = None
    usuario_obj = None

    while usuario_obj is None:
        mostrar_inicio_sesion()

        usuario = input("Ingrese su usuario: ")
        password = getpass.getpass("Ingrese su contraseña: ")

        dao = AdminDao()
        usuario_obj = dao.buscarAdmin(usuario, password)

        if usuario_obj is None:
            dao = JefeVentasDao()
            usuario_obj = dao.buscarJefeVentas(usuario, password)

        if usuario_obj is None:
            dao = VendedorDao()
            usuario_obj = dao.buscarVendedor(usuario, password)

        if usuario_obj is None:
            cls()
            print("Usuario o contraseña incorrectos. Por favor, inténtelo nuevamente.")
            time.sleep(3)

    if isinstance(usuario_obj, administrador):
        while True:
            mostrar_menu_admin()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                while True:
                    mostrar_submenu_jefe_ventas()
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == '1':
                        if dao.crearJefeVentas():
                            cls()
                            print("Jefe de ventas creado exitosamente.")
                        else:
                            cls()
                            print("Proceso cancelado, volviendo al menú.")
                        time.sleep(2)
                    elif subopcion == '2':
                        if dao.actualizarJefeVentas():
                            cls()
                            print("Jefe de ventas actualizado exitosamente.")
                        else:
                            cls()
                            print("Proceso cancelado, volviendo al menú.")
                        time.sleep(2)
                    elif subopcion == '3':
                        jefes_ventas = dao.mostrarJefesVentas()
                        cls()
                        if jefes_ventas:
                            table = BeautifulTable()
                            table.columns.header = ['Nombre', 'Email', 'Teléfono']
                            for jefe_ventas in jefes_ventas:
                                table.rows.append(jefe_ventas)
                            print("Lista de Jefes de Ventas:")
                            print(table)
                        else:
                            print("No hay jefes de ventas registrados.")
                        salir = input("Presione cualquier tecla para salir")
                        if salir:
                            break
                    elif subopcion == '4':
                        if dao.eliminarJefeVentas():
                            cls()
                            print("Jefe de ventas eliminado exitosamente.")
                        else:
                            cls()
                            print("Proceso cancelado, volviendo al menú.")
                        time.sleep(2)
                    elif subopcion == '5':
                        break
                    else:
                        cls()
                        print("Opción no válida. Intente nuevamente.")
                        time.sleep(2)
            elif opcion == '2':
                while True:
                    mostrar_submenu_vendedor()
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == '1':
                        if dao.crearVendedor():
                            cls()
                            print("Vendedor creado exitosamente.")
                        else:
                            cls()
                            print("Proceso cancelado, volviendo al menú.")
                        time.sleep(2)
                    elif subopcion == '2':
                        if dao.actualizarVendedor():
                            cls()
                            print("Vendedor actualizado exitosamente.")
                        else:
                            cls()
                            print("Proceso cancelado, volviendo al menú.")
                        time.sleep(2)
                    elif subopcion == '3':
                        vendedor = dao.mostrarVendedores()
                        cls()
                        if vendedor:
                            table = BeautifulTable()
                            table.columns.header = ['Nombre', 'Email', 'Teléfono']
                            for vendedor in vendedor:
                                table.rows.append(vendedor)
                            print("Lista de vendedores:")
                            print(table)
                        else:
                            print("No hay vendedores registrados.")
                        salir = input("Presione cualquier tecla para salir")
                        if salir:
                            break
                    elif subopcion == '4':
                        if dao.eliminarVendedor():
                            cls()
                            print("Vendedor eliminado exitosamente.")
                        else:
                            cls()
                            print("Proceso cancelado, volviendo al menú.")
                        time.sleep(2)
                    elif subopcion == '5':
                        break
                    else:
                        cls()
                        print("Opción no válida. Intente nuevamente.")
                        time.sleep(2)
            elif opcion == '3':
                while True:
                    mostrar_submenu_admin_inventario()
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == '1':
                        dao.insertarProducto()
                    elif subopcion == '2':
                        dao.mostrarProductos()
                    elif subopcion == '3':
                        dao.actualizarProducto()
                    elif subopcion == '4':
                        dao.eliminarProducto()
                    elif subopcion == '5':
                        dao.actualizarStockProducto()
                    elif subopcion == '6':
                        dao.visualizarProductos()
                    elif subopcion == '7':
                        break
                    else:
                        cls()
                        print("Opción no válida. Intente nuevamente.")
                        time.sleep(2)
            elif opcion == '4':
                while True:
                    mostrar_submenu_ventas()
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == '1':
                        dao.realizarVentaConBoleta()
                    elif subopcion == '2':
                        dao.realizarVentaConFactura()
                    elif subopcion == '3':
                        dao.realizarDevolucionFactura()
                    elif subopcion == '4':
                        dao.realizarDevolucionBoleta()
                    elif subopcion == '5':
                        dao.mostrar_mis_datos_vendedor()
                    elif subopcion == '6':
                        dao.buscar_cliente_y_compras()
                    elif subopcion == '7':
                        break
                    else:
                        cls()
                        print("Opción no válida. Intente nuevamente.")
                        time.sleep(2)
            elif opcion == '5':
                while True:
                    mostrar_submenu_informes_admin()
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == '1':
                        dao.informe_ventas()
                    elif subopcion == '2':
                        dao.mostrar_productos_caducidad_proxima()
                    elif subopcion == '3':
                        dao.abrir_ventas()
                    elif subopcion == '4':
                        dao.cerrar_ventas()
                    elif subopcion == '5':
                        dao.mostrar_mis_datos_jefe_ventas()
                    elif subopcion == '6':
                        dao.crear_bodega()
                    elif subopcion == '7':
                        break
                    else:
                        cls()
                        print("Opción no válida. Intente nuevamente.")
                        time.sleep(2)
            elif opcion == '6':
                print("Volviendo al inicio de sesión...")
                time.sleep(2)
                return main()
            else:
                cls()
                print("Opción no válida. Intente nuevamente.")
                time.sleep(2)

    elif isinstance(usuario_obj, JefeVentas):
        while True:
            mostrar_menu_jefe_ventas()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                while True:
                    mostrar_submenu_admin_inventario()
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == '1':
                        dao.insertarProducto()
                    elif subopcion == '2':
                        dao.mostrarProductos()
                    elif subopcion == '3':
                        dao.actualizarProducto()
                    elif subopcion == '4':
                        dao.eliminarProducto()
                    elif subopcion == '5':
                        dao.actualizarStockProducto()
                    elif subopcion == '6':
                        dao.visualizarProductos()
                    elif subopcion == '7':
                        break
                    else:
                        cls()
                        print("Opción no válida. Intente nuevamente.")
                        time.sleep(2)
            elif opcion == '2':
                while True:
                    mostrar_submenu_ventas()
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == '1':
                        dao.realizarVentaConBoleta()
                    elif subopcion == '2':
                        dao.realizarVentaConFactura()
                    elif subopcion == '3':
                        dao.realizarDevolucionFactura()
                    elif subopcion == '4':
                        dao.realizarDevolucionBoleta()
                    elif subopcion == '5':
                        dao.mostrar_mis_datos_vendedor()
                    elif subopcion == '6':
                        dao.buscar_cliente_y_compras()
                    elif subopcion == '7':
                        break
                    else:
                        cls()
                        print("Opción no válida. Intente nuevamente.")
                        time.sleep(2)
            elif opcion == '3':
                while True:
                    mostrar_submenu_informes_jefe_ventas()
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == '1':
                        dao.informe_ventas()
                    elif subopcion == '2':
                        dao.mostrar_productos_caducidad_proxima()
                    elif subopcion == '3':
                        dao.abrir_ventas()
                    elif subopcion == '4':
                        dao.cerrar_ventas()
                    elif subopcion == '5':
                        dao.mostrar_mis_datos_jefe_ventas()
                    elif subopcion == '6':
                        dao.crear_bodega()
                    elif subopcion == '7':
                        break
                    else:
                        cls()
                        print("Opción no válida. Intente nuevamente.")
                        time.sleep(2)
            elif opcion == '4':
                print("Volviendo al inicio de sesión...")
                time.sleep(2)
                return main()
            else:
                cls()
                print("Opción no válida. Intente nuevamente.")
                time.sleep(2)

    elif isinstance(usuario_obj, Vendedor):
        while True:
            mostrar_menu_vendedor()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                while True:
                    mostrar_submenu_ventas()
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == '1':
                        dao.realizarVentaConBoleta()
                    elif subopcion == '2':
                        dao.realizarVentaConFactura()
                    elif subopcion == '3':
                        dao.realizarDevolucionFactura()
                    elif subopcion == '4':
                        dao.realizarDevolucionBoleta()
                    elif subopcion == '5':
                        dao.mostrar_mis_datos_vendedor()
                    elif subopcion == '6':
                        dao.buscar_cliente_y_compras()
                    elif subopcion == '7':
                        break
                    else:
                        cls()
                        print("Opción no válida. Intente nuevamente.")
                        time.sleep(2)
            elif opcion == '2':
                print("Volviendo al inicio de sesión...")
                time.sleep(2)
                return main()
            else:
                cls()
                print("Opción no válida. Intente nuevamente.")
                time.sleep(2)

if __name__ == "__main__":
    main()

