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
