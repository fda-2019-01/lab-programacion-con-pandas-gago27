##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
tbl1 = pd.read_csv('tbl1.tsv',
                  sep = '\t',
                  thousands = None,
                  decimal = '.')
tbl_1 = tbl1.groupby('_c0')
tbl = tbl_1.groups.keys()

listas = []
for i in tbl:
  j = tbl1.loc[tbl_1.groups[i]]
  k = list(j['_c4'])
  listas = listas +[k]
lista = []
for j in listas:
  j = ','.join(j)
  lista = lista+[j]
lista

respuesta = pd.DataFrame({'_c0' : list(tbl),
                         'lista' : list(lista)})
respuesta
