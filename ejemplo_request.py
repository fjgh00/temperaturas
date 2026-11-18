# Primero instalaremos la librería
# pip install requests
import requests as rq
import pandas as pd

# /1 -> solo cogemos el primer elemento
url = "https://jsonplaceholder.typicode.com/posts/1" 
post = rq.get(url).json()
print(post)

# Con Pandas
print("# ----- con Pandas ----- #")
url = "https://jsonplaceholder.typicode.com/posts" 
df = pd.DataFrame(rq.get(url).json())
print(df)
