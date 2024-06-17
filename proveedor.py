class Proveedor:
    def __init__(self) -> None:
        self.__nombre = ''
        self.__rut = ''
        self.__direccion = ''
        self.__conectado = False

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor) -> None:
        self.__nombre = valor

    @property
    def rut(self) -> str:
        return self.__rut

    @rut.setter
    def rut(self, valor) -> None:
        self.__rut = valor

    @property
    def direccion(self) -> str:
        return self.__direccion
    
    @direccion.setter
    def direccion(self, valor) -> None:
        self.__direccion = valor
    
    @property
    def conectado(self) -> bool:
        return self.__conectado

    @conectado.setter
    def conectado(self, valor) -> None:
        self.__conectado = valor

    def __str__(self) -> str:
        estado = 'conectado' if self.__conectado else 'desconectado'
        return f'Mi usuario es {self.__nombre}, mi pass es {self.__password} y estoy {estado}'