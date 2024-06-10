class administrador:
    def __init__(self) -> None:
        self.__usuario=''
        self.__password=''
        self.__conectado = False

    @property
    def usuario(self)->str:
        return self.__usuario
    @usuario.setter
    def usuario(self,valor)->None:
        self.__usuario = valor
    @property
    def password(self)->str:
        return self.__password
    @password.setter
    def password(self,valor)->None:
        self.__password = valor
    @property
    def conectado(self)->bool:
        return self.__conectado
    @conectado.setter
    def conectado(self,valor)->None:
        self.__conectado = valor

    def __str__(self) -> str:
        if self.__conectado:
            estado= 'conectado'
        else:
            estado = 'desconectado'
        return f'mi usuario es {self.__usuario}, mi pass es {self.__password} y estoy {estado}'

