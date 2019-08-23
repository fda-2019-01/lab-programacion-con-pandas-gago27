##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
tbl_1 = pd.read_csv('tbl1.tsv',
                   sep = '\t',
                   thousands = None,
                   decimal = '.')
tbl_1 = tbl_1.sort_values(by=['_c4'])
tbl_1['_c4'] = tbl_1['_c4'].map(lambda x: x.upper())

c = tbl_1._c4.unique()
ans = list(c)
ans
