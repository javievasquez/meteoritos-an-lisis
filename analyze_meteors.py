import os
from datetime import datetime

# Buscando archivos que comienzan con "meteor_" y terminan en ".txt"
archivos_meteor = []

for nombre in os.listdir("."):
    if nombre.startswith("meteor_") and nombre.endswith(".txt"):
        archivos_meteor.append(nombre)

# Ordenando los nombres de archivo para procesarlos de forma ordenada
archivos_meteor.sort()

# Leyendo las marcas de tiempo (fecha + hora) de cada archivo
marcas_tiempo = []

for nombre in archivos_meteor:
    with open(nombre, "r", encoding="utf-8") as f:
        linea = f.readline().strip()

    # Separando la línea en partes: fecha, hora, duracion, altura, azimut
    partes = linea.split(",")
    if len(partes) >= 2:
        fecha_str = partes[0].strip()
        hora_str = partes[1].strip()

        # Uniéndo fecha y hora en un solo string
        fecha_hora_str = fecha_str + " " + hora_str

        # Convirtiendo el string a objeto datetime
        instante = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")

        # Agregando la marca de tiempo a la lista
        marcas_tiempo.append(instante)

# Calculando el total de eventos
total_eventos = len(marcas_tiempo)

# Ordenando las marcas de tiempo por seguridad
marcas_tiempo.sort()

# Calculando los intervalos entre meteoros en segundos
intervalos = []

if total_eventos > 1:
    indice = 1
    while indice < total_eventos:
        # Restando dos marcas de tiempo consecutivas
        diferencia = marcas_tiempo[indice] - marcas_tiempo[indice - 1]

        # Obteniendo la diferencia en segundos
        segundos = diferencia.total_seconds()

        # Agregando el intervalo a la lista
        intervalos.append(segundos)

        # Avanzando al siguiente par de eventos
        indice = indice + 1

# Calculando el intervalo promedio
if len(intervalos) > 0:
    suma_intervalos = 0.0

    for valor in intervalos:
        suma_intervalos = suma_intervalos + valor

    promedio_segundos = suma_intervalos / len(intervalos)
else:
    promedio_segundos = 0.0

# Guardando el resultado en stats.txt
with open("stats.txt", "w", encoding="utf-8") as f:
    f.write("Total events: " + str(total_eventos) + "\n")
    f.write(
        "Average time between meteors: "
        + str(round(promedio_segundos, 1))
        + " seconds\n"
    )

# Imprimiendo en pantalla
print("Analizando archivos de meteoros en la carpeta actual")
print("Total de eventos encontrados:", total_eventos)
print("Intervalo promedio entre meteoros (segundos):", round(promedio_segundos, 1))
