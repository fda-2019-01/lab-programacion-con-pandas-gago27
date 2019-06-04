##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
tbl_0 = pd.read_csv('tbl0.tsv',
                   sep = '\t',
                   thousands = None,
                   decimal = '.')
tbl_0.groupby('_c1').mean()[['_c2']]
