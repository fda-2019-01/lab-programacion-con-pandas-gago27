##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
tbl2 = pd.read_csv('tbl2.tsv',
                  sep = '\t',
                  thousands = None,
                  decimal = '.')
tbl_2 = tbl2.groupby('_c0')
tbl = tbl_2.groups.keys()

lista = []
for num in tbl:
  info = tbl2.loc[tbl_2.groups[num]]
  c5a = list(info['_c5a'])
  c5b = list(info['_c5b'])
  ren = []
  for i in range(len(c5a)):
    m = list(c5a[i]) 
    m = ''.join(m) + ':'+ str(c5b[i])
    ren = ren + [m]
  ren = sorted(ren)
  lista= lista + [ren]
lista = [','.join(line) for line in lista]
respuesta = pd.DataFrame({'_c0' : list(tbl),
                         'lista' : lista})
respuesta
