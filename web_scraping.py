import pandas as pd
from scraping import scraping_uf

# Receber informações de estados
estado = scraping_uf('sc')

for indicador in estado:
    if ']' in estado[indicador]:
        estado[indicador] = estado[indicador].split(']')[0][:-8]
    else:
        estado[indicador] = estado[indicador]

df = pd.DataFrame(estado.values(), index=estado.keys())

print (df)