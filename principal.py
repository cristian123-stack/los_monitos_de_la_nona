import getpass
import sys
import time
from admin import administrador
from jefeventas import JefeVentas
from vendedor import Vendedor
from beautifultable import BeautifulTable
from adminDao import AdminDao
from jefeventasDao import JefeVentasDao
from vendedorDao import VendedorDao

def mostrar_inicio_sesion():
    print("*****************************")
    print("*      Inicio de Sesión     *")
    print("*****************************")

def mostrar_menu_admin():
    print("*****************************")
    print("* Bienvenido al Menú de Administrador *")
    print("*****************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Crear Jefe de Ventas"])
    table.rows.append(["2", "Crear Vendedor"])
    table.rows.append(["3", "Actualizar Jefe de Ventas"])
    table.rows.append(["4", "Actualizar Vendedor"])
    table.rows.append(["5", "Mostrar Jefes de Ventas"])
    table.rows.append(["6", "Mostrar Vendedores"])
    table.rows.append(["7", "Eliminar Jefe de Ventas"])
    table.rows.append(["8", "Eliminar Vendedor"])
    table.rows.append(["9", "Volver al inicio de sesión"])
    print(table)

def mostrar_menu_jefe_ventas():
    print("*****************************")
    print("* Bienvenido al Menú de Jefe de Ventas *")
    print("*****************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Opción 1"])
    table.rows.append(["2", "Opción 2"])
    table.rows.append(["3", "Salir"])
    print(table)

def mostrar_menu_vendedor():
    print("*****************************")
    print("* Bienvenido al Menú de Vendedor *")
    print("*****************************")
    table = BeautifulTable()
    table.columns.header = ["Opción", "Descripción"]
    table.rows.append(["1", "Opción 1"])
    table.rows.append(["2", "Opción 2"])
    table.rows.append(["3", "Salir"])
    print(table)

def opcion_ficticia():
    print("Ejecutando opción ficticia...")
    time.sleep(2)

def main():
    dao = None
    usuario_obj = None

    while usuario_obj is None:
        mostrar_inicio_sesion()
        table = BeautifulTable()
        table.columns.header = ["Campo", "Descripción"]
        table.rows.append(["Usuario", "Ingrese su nombre de usuario"])
        table.rows.append(["Contraseña", "Ingrese su contraseña"])
        print(table)

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
            print("Usuario o contraseña incorrectos. Por favor, inténtelo nuevamente.")
            time.sleep(3)

    if isinstance(usuario_obj, administrador):
        while True:
            mostrar_menu_admin()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                if dao.crearJefeVentas():
                    print("Jefe de ventas creado exitosamente.")
                else:
                    print("Error al crear el Jefe de ventas.")
            elif opcion == '2':
                if dao.crearVendedor():
                    print("Vendedor creado exitosamente.")
                else:
                    print("Error al crear el Vendedor.")
            elif opcion == '3':
                if dao.actualizarJefeVentas():
                    print("Jefe de ventas actualizado exitosamente.")
                else:
                    print("Error al actualizar el Jefe de ventas.")
            elif opcion == '4':
                if dao.actualizarVendedor():
                    print("Vendedor actualizado exitosamente.")
                else:
                    print("Error al actualizar el Vendedor.")
            elif opcion == '5':
                jefes_ventas = dao.mostrarJefesVentas()
                if jefes_ventas:
                    print("Lista de Jefes de Ventas:")
                    for jefe in jefes_ventas:
                        print(jefe)  # Imprime cada jefe de ventas
                else:
                    print("No se encontraron Jefes de Ventas.")
            elif opcion == '6':
                vendedores = dao.mostrarVendedores()
                if vendedores:
                    print("Lista de Vendedores:")
                    for vendedor in vendedores:
                        print(vendedor)  # Imprime cada vendedor
                else:
                    print("No se encontraron Vendedores.")
            elif opcion == '7':
                if dao.eliminarJefeVentas():
                    print("Jefe de ventas eliminado exitosamente.")
                else:
                    print("Error al eliminar el Jefe de ventas.")
            elif opcion == '8':
                if dao.eliminarVendedor():
                    print("Vendedor eliminado exitosamente.")
                else:
                    print("Error al eliminar el Vendedor.")
            elif opcion == '9':
                print("Volviendo al inicio de sesión...")
                time.sleep(2)
                return main()  # Volver al inicio de sesión
            else:
                print("Opción no válida. Intente nuevamente.")

    elif isinstance(usuario_obj, JefeVentas):
        while True:
            mostrar_menu_jefe_ventas()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                opcion_ficticia()
            elif opcion == '2':
                opcion_ficticia()
            elif opcion == '3':
                dao.desconectar(usuario_obj)
                print("Saliendo...")
                sys.exit()
            else:
                print("Opción no válida. Intente nuevamente.")

    elif isinstance(usuario_obj, Vendedor):
        while True:
            mostrar_menu_vendedor()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                opcion_ficticia()
            elif opcion == '2':
                opcion_ficticia()
            elif opcion == '3':
                dao.desconectar(usuario_obj)
                print("Saliendo...")
                sys.exit()
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
