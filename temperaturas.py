temperaturas = [18.5, 21.2, 19.8, 23.1, 25.4]

# Calcular media
media = sum(temperaturas) / len(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)

# Mostrar temperaturas
print("Temperaturas:", temperaturas)
# Mostrar media
print("Temperatura media:", media)
# Mostrar máxima
print("Temperatura máxima:", maxima)
# Mostrar mínima
print("Temperatura mínima:", minima)

umbral_calor = 25

if maxima > umbral_calor:
    print("Aviso: Se ha superado el umbral de calor:", umbral_calor)
else:
    print("Temperaturas correctas")

contador = 0

for t in temperaturas:
    if t > 20:
        contador += 1

print ("Día por encima de 20 grados:", contador)

for i in range(1, len(temperaturas)):
    diferencia = temperaturas[i] - temperaturas[i - 1]

    if diferencia > 0:
        tendencia = "sube"
    elif diferencia < 0:
        tendencia = "baja"
    else:
        tendencia = "igual"

    print(f"Día {i} -> día {i + 1} {tendencia} ({round(diferencia, 2)}) grados")
