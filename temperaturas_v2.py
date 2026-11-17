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
    maxima_por_ciudad
)

# Variable para ajustar cadenas en print
maxlen = 0
for i in range(len(temperaturas)):
    temperatura = temperaturas[i]
    if maxlen < len(temperatura["ciudad"]):
        maxlen = len(temperatura["ciudad"])

# Extraemos la columna de temperaturas
solo_temperatura = extraer_temperatura(temperaturas)
print("#---------- TEMPERATURAS ----------#")
print("Número de registros:", len(solo_temperatura))
print("Día\t\tCiudad\t\t Temperatura")
for i in range(len(temperaturas)):
    temperatura = temperaturas[i]
    print(temperatura["dia"], end="\t\t")
    print(temperatura["ciudad"].ljust(maxlen), end="\t\t")
    print(temperatura["temperatura"])
print()

# Media
print("\nTemperatura media.:", calcular_media(solo_temperatura))
# Máxima
print("Temperatura máxima:", calcular_maxima(solo_temperatura))
# Mínima
print("Temperatura mínima:", calcular_minima(solo_temperatura))

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
# Máxima por ciudad
print("\n# ----- Temperatura máxima por ciudad ----- #")
maximas = maxima_por_ciudad(temperaturas)
for ciudad, maxima in maximas.items():
    print("Ciudad:", ciudad, "-->", round(maxima, 2))
