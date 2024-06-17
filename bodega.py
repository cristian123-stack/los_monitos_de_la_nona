class Bodega:
    def __init__(self) -> None:
        self.__nombre = ''
        self.__direccion = ''

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor) -> None:
        self.__nombre = valor

    @property
    def direccion(self) -> str:
        return self.__direccion

    @direccion.setter
    def direccion(self, valor) -> None:
        self.__direccion = valor

    def __str__(self) -> str:
        return f'La bodega es {self.__nombre}, mi direccion es {self.__direccion}'