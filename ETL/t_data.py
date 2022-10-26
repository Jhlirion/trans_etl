import psycopg2
import numpy as np
import psycopg2.extras as extras
import pandas as pd
from datetime import date

df_bibli = pd.read_csv(r'data\bibliotecas\2022-October\bibliotecas-12-10-2022.csv')
df_cines = pd.read_csv(r'data\cines\2022-October\cines-12-10-2022.csv')
df_museos = pd.read_csv(r'data\museos\2022-October\museos-12-10-2022.csv')