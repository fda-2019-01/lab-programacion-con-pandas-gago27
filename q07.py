##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
tbl_0 = pd.read_csv('tbl0.tsv',
                sep = '\t',
                thousands = None,
                decimal = '.')
tbl_0['suma']= tbl_0['_c0']+ tbl_0['_c2']
tbl_0
