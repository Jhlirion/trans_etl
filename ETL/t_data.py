import psycopg2
import numpy as np
import psycopg2.extras as extras
import pandas as pd
from datetime import date

df_bibli = pd.read_csv(r'data\bibliotecas\2022-October\bibliotecas-12-10-2022.csv')
df_cines = pd.read_csv(r'data\cines\2022-October\cines-12-10-2022.csv')
df_museos = pd.read_csv(r'data\museos\2022-October\museos-12-10-2022.csv')

colum_nor = ['cod_localidad', 'id_provincia', 'id_departamento', 'categoria',
            'provincia','localidad','nombre','domicilio','codi_postal','nume_de_telefono','mail','web']

df_bibli.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoria', 
                          'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'codi_postal', 
                          'Teléfono':'nume_de_telefono', 'Mail':'mail', 'Web':'web'}, inplace=True)

df_bibli_final = df_bibli[['cod_localidad', 'id_provincia', 'id_departamento', 'categoria',
            'provincia','localidad','nombre','domicilio','codi_postal','nume_de_telefono','mail','web']].copy()


df_cines.rename(columns={'direccion':'domicilio', 'cp':'codi_postal'}, inplace=True)

df_cines_final = df_cines[['cod_localidad', 'id_provincia', 'id_departamento', 'categoria',
            'provincia','localidad','nombre','domicilio','codi_postal','web']].copy()

df_cines_final[['nume_de_telefono','mail']] = 0, 0

df_museos.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'direccion':'domicilio', 'CP':'codi_postal', 
                          'telefono':'nume_de_telefono', 'Mail':'mail', 'Web':'web'}, inplace=True)

df_museos_final = df_museos[['cod_localidad', 'id_provincia', 'id_departamento', 'categoria',
            'provincia','localidad','nombre','domicilio','codi_postal','nume_de_telefono','mail','web']].copy()

df_principal=pd.concat([df_bibli_final, df_museos_final, df_cines_final] , join="inner" , ignore_index=True)

df_cine_principal=df_cines[["provincia","pantallas","butacas","espacio_incaa"]]
df_cine_principal=df_cine_principal.rename(columns={"pantallas":"cant_pantallas","butacas":"cant_butacas","espacio_incaa":"cant_espacio_incaa"})

today = date.today()

# Ingresamos la fecha de carga 
df_cine_principal["upload_date"]=today.strftime("%Y-%m-%d")
df_principal["upload_date"]=today.strftime("%Y-%m-%d")
print(df_bibli_final)







