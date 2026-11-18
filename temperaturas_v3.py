with open("datos_v3.csv", "r", encoding = "utf-8") as f:
    lineas = f.readlines()

for linea in lineas:
    print(linea.strip())

# Cabeceras
cabeceras = lineas[0].strip().split(",")
print("Cabeceras:", cabeceras)

# Resto de datos
registros = []
for lina in lineas[1:]:
    if not linea.strip():
        continue
    valores = linea.strip().split(",")
    registro = dict(zip(cabeceras, valores))
    registros.append(registro)

print(registros[0])
