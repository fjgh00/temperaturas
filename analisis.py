# Calcular media
def calcular_media(lista):
    return sum(lista) / len(lista)

# Calcular máxima
def calcular_maxima(lista):
    return max(lista)

# Calcular mínima
def calcular_minima(lista):
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
