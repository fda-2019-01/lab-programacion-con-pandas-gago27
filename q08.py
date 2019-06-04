##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
tbl_0= pd.read_csv('tbl0.tsv',
                  sep = '\t',
                  thousands = None,
                  decimal = '.')
tbl_0['ano'] = tbl_0['_c3'].map(lambda x : x[0:4])
tbl_0
