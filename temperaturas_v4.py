import seaborn as sns
import pandas as pd

# Creamos un entorno virtual en Python para no mezclar librerías de proyectos
# $>python -m venv .venv
# $>source .venv/bin/activate
# (.venv)$>

# Lectura con pandas
# Primero se tiene que instalar la librería Pandas
# (.venv)$>pip install pandas
print("# ----- LECTURA CON PANDAS ----- #")
df = pd.read_csv("datos_v3.csv")

# 5 primeros registros
print("\n5 primeros registros")
print(df.head())

# 5 últimos registros
print("\n5 últimros registros")
print(df.tail())

# Estructura del dataframe
print("\nEstructura del dataframe")
print(df.info())

# Estadísticas del dataframe
print("\nEstadísticas del dataframe")
print(df.describe())

# Filtrar el dataframe
print("\nFiltrar el dataframe")
print(df[df["temperatura"] > 20])

# Media por ciudad
print("\nMedia por ciudad")
print(df.groupby("ciudad")["temperatura"].mean())

# Datasets con Seaborn
# Primero se tiene que instalar la librería
# (.venv)$>pip install seaborn
print("# ----- DATASETS CON SEABORN ----- #")
print("# ----- DATASET: Titanic ----- #")
titanic = sns.load_dataset("titanic")
print(titanic.head())
# print("# ----- DATASET: Iris ----- #")
# iris = sns.load_dataset("iris")
# print(iris.head())
# print("# ----- DATASET: Penguins ----- #")
# penguins = sns.load_dataset("penguins")
# print(penguins.head())
# print("# ----- DATASET: Tips ----- #")
# tips = sns.load_dataset("tips")
# print(tips.head())
print("Nº de pasajeros:", len(titanic))
print("Edad media:", titanic["age"].mean())
print("Nº de supervivientes:", titanic["survived"].value_counts())
print("Tasa de supervivencia por clase")
print(round(titanic.groupby("class")["survived"].mean() * 100, 2))
