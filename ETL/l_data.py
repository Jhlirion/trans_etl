from tkinter import E
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import t_data as tra     

df = tra.df_bibli_final


try:
    conex = create_engine("postgresql+psycopg2://{}:{}@{}/{}".format("admin","admin","172.17.0.1:3333", "alkemy"))
    conexpostgres = conex.connect()
    metadatas = sqlalchemy.MetaData()
    df.to_sql("df", conexpostgres, if_exists="append", index=False)
    print("Vamo Loco")
except Exception as e:
    print(e)