from datos import temperaturas
from analisis_v2 import (
    calcular_media,
    calcular_maxima,
    calcular_minima,
    contador_umbral,
    resumen_temperaturas,
    extraer_temperatura,
    filtrar_por_ciudad,
    dia_mas_caluroso,
    media_por_ciudad,
    maxima_por_ciudad,
    extraer_humedad,
    humedad_maxima,
    humedad_media,
    humedad_minima,
    filtrar,
    ranking_temperaturas,
    resumen_json
)

# Variable para ajustar cadenas en print
maxlen = 0
for i in range(len(temperaturas)):
    temperatura = temperaturas[i]
    if maxlen < len(temperatura["ciudad"]):
        maxlen = len(temperatura["ciudad"])

print("#---------- TEMPERATURAS ----------#")
print("Número de registros:", len(temperaturas))
print("Día\tCiudad\t    Temperatura\t      Humedad")
for i in range(len(temperaturas)):
    temperatura = temperaturas[i]
    print(temperatura["dia"], end = "\t")
    print(temperatura["ciudad"].ljust(maxlen), end = "\t")
    print(temperatura["temperatura"], end = "\t\t")
    print(temperatura["humedad"])
print()

# Extraemos la columna de temperaturas
solo_temperatura = extraer_temperatura(temperaturas)
# Media
print("\nTemperatura media.:", calcular_media(solo_temperatura))
# Máxima
print("Temperatura máxima:", calcular_maxima(solo_temperatura))
# Mínima
print("Temperatura mínima:", calcular_minima(solo_temperatura))

print("\n#---------- HUMEDAD ----------#")
# Extraemos la columna de humedad
solo_humedad = extraer_humedad(temperaturas)
# Media
print("Humedad media.:", humedad_media(solo_humedad))
# Máxima
print("Humedad máxima:", humedad_maxima(solo_humedad))
# Mínima
print("Humedad mínima:", humedad_minima(solo_humedad))

# Día más caluroso
mas_caluroso = dia_mas_caluroso(temperaturas)
print("\n# ----- Día más caluroso ----- #")
print("Día:", mas_caluroso["dia"], "Ciudad:", mas_caluroso["ciudad"], 
     "Tª:", mas_caluroso["temperatura"])

# Filtrar por ciudad
ciudad = filtrar_por_ciudad(temperaturas, "Huesca")
# Media por ciudad
print("\n# ----- Temperatura media por ciudad ----- #")
medias = media_por_ciudad(temperaturas)
for ciudad, media in medias.items():
    print("Ciudad:", ciudad, "-->", round(media, 2))
# Media por ciudad
print("\n# ----- Temperatura media por ciudad ordenado ----- #")
medias = ranking_temperaturas(temperaturas)
for c in medias:
    print("Ciudad:", c[0].ljust(maxlen), "-->", round(c[1], 2))
# Máxima por ciudad
print("\n# ----- Temperatura máxima por ciudad ----- #")
maximas = maxima_por_ciudad(temperaturas)
for ciudad, maxima in maximas.items():
    print("Ciudad:", ciudad, "-->", round(maxima, 2))

print("\n#----- TEMPERATURAS UMBRAL -----#")
ciudad = filtrar(temperaturas, "Huesca", 20)
print("Número de registros:", len(ciudad))
print("Día\tCiudad\t    Temperatura\t      Humedad")
for i in range(len(ciudad)):
    temperatura = ciudad[i]
    print(temperatura["dia"], end = "\t")
    print(temperatura["ciudad"].ljust(maxlen), end = "\t")
    print(temperatura["temperatura"], end = "\t\t")
    print(temperatura["humedad"])
print()

print("# ----- Resumen JSON ----- #")
print(resumen_json(temperaturas))
