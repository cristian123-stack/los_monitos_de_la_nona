import getpass
import sys
import time
from admin import administrador
from adminDao import adminDao

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def opcion1():
    print("Ejecutando opción 1...")
    # Añade la funcionalidad de la opción 1 aquí
    time.sleep(2)

def opcion2():
    print("Ejecutando opción 2...")
    # Añade la funcionalidad de la opción 2 aquí
    time.sleep(2)

def opcion3():
    print("Ejecutando opción 3...")
    # Añade la funcionalidad de la opción 3 aquí
    time.sleep(2)

def main():
    dao = adminDao(intentos=3)
    
    while dao._adminDao__intentos > 0:
        usuario = input("Ingrese su usuario: ")
        password = getpass.getpass("Ingrese su contraseña: ")
        
        admin = dao.conectar(usuario, password)
        
        if admin is not None:
            while True:
                mostrar_menu()
                opcion = input("Seleccione una opción: ")
                
                if opcion == '1':
                    opcion1()
                elif opcion == '2':
                    opcion2()
                elif opcion == '3':
                    opcion3()
                elif opcion == '4':
                    dao.desconectar(admin)
                    print("Saliendo...")
                    sys.exit()
                else:
                    print("Opción no válida. Intente nuevamente.")
        else:
            if dao._adminDao__intentos == 0:
                print("Ha excedido el número de intentos permitidos. Saliendo...")
                sys.exit()

if __name__ == "__main__":
    main()
