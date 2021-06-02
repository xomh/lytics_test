import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Obtener desde url el registro de casos por Covid en Estados Unidos.
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'

#Guardar los datos en un Dataframe de Pandas.
df = pd.read_csv(url)

#Generar una tabla con el resumen total de casos por día.
df_res = df[['date', 'cases']].copy()
print(df_res.to_string(index=False))

#Generar gráfica con el top 10 de días con más casos.
auxlist = df['cases'].to_list()
daycases = []
for i in range(len(auxlist)):
    if i == 0:
        daycases.append(auxlist[i])
    else:
        daycases.append(auxlist[i] - auxlist[i-1])
df['daycases'] = daycases
df_aux = df.sort_values('daycases', ascending=False)
datelist = df_aux.head(10)['date'].tolist()
caseslist = df_aux.head(10)['daycases'].tolist()
datelist.reverse()
caseslist.reverse()
x = np.array(datelist)
y = np.array(caseslist)
plt.barh(x, y, height = 0.5, color = "magenta")
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5, axis = 'x')
plt.title("Top 10 de días con más casos de COVID en Estados Unidos.", loc = 'right')
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
fig = plt.gcf()
plt.show()

#Guardar la gráfica en un archivo local.
fig.savefig("top10.png")