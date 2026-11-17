# Calcular temperatura media
def calcular_media(lista):
    return sum(lista) / len(lista)

# Calcular temperatura máxima
def calcular_maxima(lista):
    return max(lista)

# Calcular temperatura mínima
def calcular_minima(lista):
    return min(lista)

# Calcular humedad media
def humedad_media(lista):
    return sum(lista) / len(lista)

# Calcular humedad máxima
def humedad_maxima(lista):
    return max(lista)

# Calcular humedad mínima
def humedad_minima(lista):
    return min(lista)

# Contador mayores de umbral
def contador_umbral(lista, umbral):
    contador = 0
    mayor20 = 0
    for t in lista:
        if t > umbral:
            contador += 1
            mayor20 += t

    if contador > 0:
        return contador, mayor20 / contador
    else:
        return contador, 999

def clasificar_temperatura(t):
    if t < 20:
        return "frio"
    elif t <= 25:
        return "templado"
    else:
        return "calor"

def resumen_temperaturas(lista):
    resumen = []
    for t in lista:
        cadena = (f"Temperatura: {t} -> {clasificar_temperatura(t)}")
        resumen.append(cadena)

    return resumen

def extraer_temperatura(registros):
    valores = []
    for r in registros:
        valores.append(r["temperatura"])
    return valores

def extraer_humedad(registros):
    valores = []
    for r in registros:
        valores.append(r["humedad"])
    return valores

def filtrar_por_ciudad(registros, ciudad):
    resultado = []
    for r in registros:
        if r["ciudad"] == ciudad:
            resultado.append(r)
    return resultado

def dia_mas_caluroso(registros):
    mas_caluroso = registros[0]
    for r in registros:
        if r["temperatura"] > mas_caluroso["temperatura"]:
            mas_caluroso = r
    return mas_caluroso

def agrupar_por_ciudad(registros):
    grupos = {}
    for r in registros:
        ciudad = r["ciudad"]
        if ciudad not in grupos:
            grupos[ciudad] = []
        grupos[ciudad].append(r["temperatura"])
    return grupos

def media_por_ciudad(registros):
    grupos = agrupar_por_ciudad(registros)
    resultado = {}
    for ciudad, valores in grupos.items():
        resultado[ciudad] = calcular_media(valores)
    return resultado

def maxima_por_ciudad(registros):
    grupos = agrupar_por_ciudad(registros)
    resultado = {}
    for ciudad, valores in grupos.items():
        resultado[ciudad] = calcular_maxima(valores)
    return resultado

def filtrar(registros, ciudad, umbral):
    resultado = []
    ciudad = filtrar_por_ciudad(registros, ciudad)
    for c in ciudad:
        if c["temperatura"] > umbral:
            resultado.append(c)
    return resultado

def ranking_temperaturas(registros):
    medias = media_por_ciudad(registros)
    ranking = sorted(medias.items(), key = lambda x: x[1], reverse = True)
    return ranking

def resumen_json(registros):
    resultado = {
        "n_registros": len(registros),
        "media_global": round(calcular_media(extraer_temperatura(registros)), 2),
        "media_por_ciudad": media_por_ciudad(registros)
    }
    return resultado
