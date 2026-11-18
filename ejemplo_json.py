import json
with open("ejemplo_json.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

print(datos["ciudad"])
print(datos["temperatura"])

# Con Pandas
print("# ----- Con Pandas ----- #")
import pandas as pd

df = pd.DataFrame([datos])
print(df)

