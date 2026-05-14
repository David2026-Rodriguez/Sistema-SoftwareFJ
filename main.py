# main.py

from clientes import Cliente
from servicios import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)
from reservas import Reserva

from excepciones import (
    ClienteError,
    ServicioError,
    ReservaError
)

from datetime import datetime


# FUNCIÓN PARA GUARDAR LOGS
def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        fecha = datetime.now()

        archivo.write(
            f"[{fecha}] {mensaje}\n"
        )


print("\n=== SISTEMA SOFTWARE FJ ===\n")


# LISTAS
clientes = []
servicios = []
reservas = []


# OPERACIÓN 1
try:

    cliente1 = Cliente(
        "Carlos Perez",
        "carlos@gmail.com",
        "3214567890"
    )

    clientes.append(cliente1)

    registrar_log("Cliente válido registrado")

except ClienteError as e:

    registrar_log(e)


# OPERACIÓN 2
try:

    cliente2 = Cliente(
        "",
        "juan@gmail.com",
        "123456"
    )

    clientes.append(cliente2)

except ClienteError as e:

    registrar_log(e)


# OPERACIÓN 3
try:

    sala = ServicioSala(
        "Sala VIP",
        50000,
        3
    )

    servicios.append(sala)

    registrar_log("Servicio sala creado")

except ServicioError as e:

    registrar_log(e)


# OPERACIÓN 4
try:

    equipo = ServicioEquipo(
        "Computadores",
        20000,
        5
    )

    servicios.append(equipo)

    registrar_log("Servicio equipo creado")

except ServicioError as e:

    registrar_log(e)


# OPERACIÓN 5
try:

    asesoria = ServicioAsesoria(
        "Asesoría Python",
        100000,
        2
    )

    servicios.append(asesoria)

    registrar_log("Servicio asesoría creado")

except ServicioError as e:

    registrar_log(e)


# OPERACIÓN 6
try:

    servicio_error = ServicioSala(
        "Sala Error",
        50000,
        -1
    )

    servicio_error.calcular_costo()

except ServicioError as e:

    registrar_log(e)


# OPERACIÓN 7
try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    costo = reserva1.procesar()

    reservas.append(reserva1)

    registrar_log(
        f"Reserva exitosa. Costo: {costo}"
    )

except ReservaError as e:

    registrar_log(e)


# OPERACIÓN 8
try:

    reserva2 = Reserva(
        cliente1,
        equipo,
        -2
    )

    reserva2.procesar()

except ReservaError as e:

    registrar_log(e)


# OPERACIÓN 9
try:

    cliente3 = Cliente(
        "Maria",
        "correo-invalido",
        "987654"
    )

except ClienteError as e:

    registrar_log(e)


# OPERACIÓN 10
try:

    asesoria_error = ServicioAsesoria(
        "Asesoría Error",
        100000,
        -5
    )

    asesoria_error.calcular_costo()

except ServicioError as e:

    registrar_log(e)


print("\n=== CLIENTES REGISTRADOS ===\n")

for cliente in clientes:

    print(cliente.mostrar_informacion())


print("\n=== SERVICIOS REGISTRADOS ===\n")

for servicio in servicios:

    print(servicio.descripcion())

    try:

        print(
            "Costo:",
            servicio.calcular_costo()
        )

    except Exception as e:

        print("Error:", e)


print("\n=== RESERVAS ===\n")

for reserva in reservas:

    print(reserva.mostrar())


print("\nSistema ejecutado correctamente.")
