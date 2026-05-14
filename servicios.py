# servicios.py

from abc import ABC, abstractmethod
from excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ServicioSala(Servicio):

    def __init__(self, nombre, costo_base, horas):

        super().__init__(nombre, costo_base)
        self.horas = horas

    def calcular_costo(self):

        if self.horas <= 0:
            raise ServicioError("Las horas deben ser mayores a cero")

        return self.costo_base * self.horas

    def descripcion(self):

        return f"Reserva de sala por {self.horas} horas"


class ServicioEquipo(Servicio):

    def __init__(self, nombre, costo_base, cantidad):

        super().__init__(nombre, costo_base)
        self.cantidad = cantidad

    def calcular_costo(self):

        if self.cantidad <= 0:
            raise ServicioError("Cantidad inválida")

        return self.costo_base * self.cantidad

    def descripcion(self):

        return f"Alquiler de {self.cantidad} equipos"


class ServicioAsesoria(Servicio):

    def __init__(self, nombre, costo_base, horas):

        super().__init__(nombre, costo_base)
        self.horas = horas

    def calcular_costo(self, descuento=0):

        if self.horas <= 0:
            raise ServicioError("Horas inválidas")

        total = self.costo_base * self.horas

        return total - descuento

    def descripcion(self):

        return f"Asesoría especializada de {self.horas} horas"
