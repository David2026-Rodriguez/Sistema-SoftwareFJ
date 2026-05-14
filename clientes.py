# clientes.py

from excepciones import ClienteError


class Cliente:

    def __init__(self, nombre, correo, telefono):

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):

        if not self.__nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        if "@" not in self.__correo:
            raise ClienteError("Correo inválido")

        if not self.__telefono.isdigit():
            raise ClienteError("El teléfono debe contener números")

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    def mostrar_informacion(self):

        return f"""
Cliente:
Nombre: {self.__nombre}
Correo: {self.__correo}
Teléfono: {self.__telefono}
"""
