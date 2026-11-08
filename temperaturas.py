from analisis import (
    calcular_media,
    contador_umbral,
    resumen_temperaturas
)

temperaturas = [30.1, 31.5, 29.8, 32.0, 33.4, 28.5]

# Informe de temperaturas
print("=== INFORME DE TEMPERATURAS ===")
print("Nº de registros:", len(temperaturas))

# Calcular media
# media = sum(temperaturas) / len(temperaturas)
media = calcular_media(temperaturas)
# Calcular máxima
maxima = max(temperaturas)
# Calcular mínima
minima = min(temperaturas)

# Mostrar temperaturas
print("Temperaturas:", temperaturas)
# Mostrar media
print("Temperatura media:", media)
# Mostrar máxima
print("Temperatura máxima:", maxima)
# Mostrar mínima
print("Temperatura mínima:", minima)

# Días de calor superior a 25º
umbral_calor = 25

if maxima > umbral_calor:
    print("Aviso: Se ha superado el umbral de calor:", umbral_calor)
else:
    print("Temperaturas correctas")

# Nº de días con temperaturas superiores a 20º
umbral_temperatura = 20
contador = contador_umbral(temperaturas, umbral_temperatura)
print ("Días por encima de 20 grados:", contador)

# Evolución diaria
for i in range(1, len(temperaturas)):
    diferencia = temperaturas[i] - temperaturas[i - 1]

    if diferencia > 0:
        tendencia = "🔺 sube"
    elif diferencia < 0:
        tendencia = "🔻 baja"
    else:
        tendencia = "➖ igual"

    print(f"Día {i} -> día {i + 1}: {tendencia} ({round(diferencia, 2)} ºC)")

print("----- Clasificación temperaturas ------")
print(resumen_temperaturas(temperaturas))
