##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

tbl2 = pd.read_csv('tbl2.tsv',
                  sep = '\t',
                  thousands = None,
                  decimal = '.')
tbl_2 = tbl2.groupby('_c5a').sum()
suma = list(tbl_2['_c5b'])
suma = [str(line) for line in suma]
tbl = tbl2.groupby('_c5a')
c5a = tbl.groups.keys()

respuesta = pd.DataFrame({'_c5a' : list(c5a),
                         '' : list(suma)})

respuesta
