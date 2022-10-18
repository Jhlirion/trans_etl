import pandas as pd
import requests 
import csv
import os
from datetime import date
from bs4 import BeautifulSoup

#declaramos la web de donde extraeremos los datos
web_cine = 'https://datos.cultura.gob.ar/dataset/espacios-culturales-argentina-sinca/archivo/f7a8edb8-9208-41b0-8f19-d72811dcea97'
web_museo = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d'
web_bibli = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7'

#listamos las webs
lis_web = [web_cine, web_museo, web_bibli]
datos = ['cines', 'museos', 'bibliotecas']

for i in range(0,3):
    result = requests.get(lis_web[i])
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find(class_='btn btn-green btn-block')
    link = box.get('href')
    # Descargamos datos
    data=requests.get(link)
    # Convertimos todo a csv
    data_cv = csv.reader(data.content.decode('utf-8').splitlines(),delimiter=',')
    # Convertimos en dataframes de pandas, para poder manejarlos mejor
    df = pd.DataFrame(data_cv)
    # Colocamos como nombre de columna la primera fila y borramos el duplicado
    df=df.set_axis(df.iloc[0], axis = 1)
    df=df.drop(0 , axis = 0)
    # Declaramos una variable para iterar la fecha de hoy
    today = date.today()
    # Creamos las carpetas y colocamos los archivos en los mismos convirtiendo a csv
    os.makedirs(
    "data/{i}/{anio}-{mes}".format(
        i = datos[i] , anio = today.strftime("%Y"), mes = today.strftime("%B")
        ),
        exist_ok=True
        )
    df.to_csv(
        "data/{i}/{anio}-{mes}/{i}-{nombre}.csv".format(
        i = datos[i] , anio = today.strftime("%Y"), mes = today.strftime("%B") , nombre = today.strftime("%d-%m-%Y")
        ), index = False
        )
    
    print(link)