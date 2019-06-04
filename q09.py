##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
tbl0 = pd.read_csv('tbl0.tsv',
                  sep = '\t',
                  thousands = None,
                  decimal = '.')
tbl = tbl0[['_c1','_c2']].sort_values(by=['_c1'])
tbl_0 = tbl.groupby('_c1')
tabla = tbl_0.groups.keys()
lista = []
for i in tabla:
  Y = tbl.loc[tbl_0.groups[i]]
  y = list(Y['_c2'])
  y = sorted(y)
  y = [str(num) for num in y]
  y = ':'.join(y)
  lista = lista+[y]
lista
respuesta = pd.DataFrame({'_c1' : list(tabla),
                 'lista' : list(lista)})
respuesta
