import random
from datetime import datetime, timedelta

# Definiendo parámetros de la simulación
FECHA_INICIO = datetime(2025, 12, 1, 2, 0, 0)   # 2025-12-01 02:00:00
FECHA_FIN = datetime(2025, 12, 3, 2, 0, 0)      # 2025-12-03 02:00:00

# Eligiendo cantidad de eventos de forma aleatoria entre 500 y 999
cantidad_eventos = random.randint(500, 999)

# Calculando la cantidad total de segundos en la ventana de tiempo
delta_total = FECHA_FIN - FECHA_INICIO
total_segundos = int(delta_total.total_seconds())

# Generando segundos aleatorios únicos dentro de la ventana
segundos_aleatorios = random.sample(range(total_segundos), cantidad_eventos)

# Ordenando los segundos para mantener el orden cronológico
segundos_aleatorios.sort()

# Recorriendo los eventos y generando los archivos
contador = 1

for segundos_offset in segundos_aleatorios:
    # Calculando la fecha y hora del evento a partir del inicio
    instante_evento = FECHA_INICIO + timedelta(seconds=segundos_offset)

    fecha_str = instante_evento.strftime("%Y-%m-%d")
    hora_str = instante_evento.strftime("%H:%M:%S")

    # Generando los otros campos del evento
    duracion_seg = random.uniform(0.1, 5.0)        # duración en segundos
    altura_grados = random.uniform(10.0, 90.0)     # altura en grados
    azimut_grados = random.uniform(0.0, 359.0)     # azimut en grados (el phi)

    # Redondeando valores para dejarlos más legibles
    duracion_seg = round(duracion_seg, 2)
    altura_grados = round(altura_grados, 1)
    azimut_grados = round(azimut_grados, 1)

    # Formando el nombre del archivo meteor_XXX.txt
    numero_str = ("00" + str(contador))[-3:]
    nombre_archivo = "meteor_" + numero_str + ".txt"

    # Construyendo el contenido de la línea con el formato solicitado
    linea = (
        fecha_str + ", "
        + hora_str + ", "
        + str(duracion_seg) + ", "
        + str(altura_grados) + ", "
        + str(azimut_grados)
    )

    # Abriendo el archivo y escribiendo la línea
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(linea + "\n")

    # Incrementando el contador del número de archivo
    contador += 1

# Imprimiendo al finalizar
print("Generando archivos de meteoros en la carpeta actual")
print("Cantidad de eventos generados:", cantidad_eventos)
print("Usando ventana de tiempo desde", FECHA_INICIO, "hasta", FECHA_FIN)
