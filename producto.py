class Producto:
    def __init__(self) -> None:
        self.__nombre = ''
        self.__cantidad = ''
        self.__valor_unitario = ''
        self.__fk_rut_prov = ''
        self.__fecha_elaboracion = ''
        self.__fecha_caducidad = ''

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor) -> None:
        self.__nombre = valor

    @property
    def cantidad(self) -> str:
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, valor) -> None:
        self.__cantidad = valor

    @property
    def valor_unitario(self) -> str:
        return self.__valor_unitario
    
    @valor_unitario.setter
    def valor_unitario(self, valor) -> None:
        self.__valor_unitario = valor

    @property
    def fk_rut_prov(self) -> str:
        return self.__fk_rut_prov
    
    @fk_rut_prov.setter
    def fk_rut_prov(self, valor) -> None:
        self.__fk_rut_prov = valor

    @property
    def fecha_elaboracion(self) -> str:
        return self.__fecha_elaboracion
    
    @fecha_elaboracion.setter
    def fecha_elaboracion(self, valor) -> None:
        self.__fecha_elaboracion = valor

    @property
    def fecha_caducidad(self) -> str:
        return self.__fecha_caducidad
    
    @fecha_caducidad.setter
    def fecha_caducidad(self, valor) -> None:
        self.__fecha_caducidad = valor

    def __str__(self) -> str:
        return f'Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Valor Unitario: {self.__valor_unitario}, Rut Proveedor: {self.__fk_rut_prov}, Fecha Elaboracion: {self.__fecha_elaboracion}, Fecha Caducidad: {self.__fecha_caducidad}'