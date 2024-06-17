class Vendedor:
    def __init__(self) -> None:
        self.__nombre = ''
        self.__password = ''
        self.__conectado = False

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor) -> None:
        self.__nombre = valor

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, valor) -> None:
        self.__password = valor

    @property
    def conectado(self) -> bool:
        return self.__conectado

    @conectado.setter
    def conectado(self, valor) -> None:
        self.__conectado = valor

    def __str__(self) -> str:
        estado = 'conectado' if self.__conectado else 'desconectado'
        return f'Mi usuario es {self.__nombre}, mi pass es {self.__password} y estoy {estado}'