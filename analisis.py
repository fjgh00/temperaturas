# Calcular media
def calcular_media(lista):
    return sum(lista) / len(lista)

# Contador mayores de umbral
def contador_umbral(lista, umbral):
    contador = 0
    for t in lista:
        if t > umbral:
            contador += 1

    return contador

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
