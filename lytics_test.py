import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def create():
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
    df = pd.read_csv(url)
    return df

def casesperday():
    df = create()
    auxlist = df['cases'].to_list()
    daycases = []
    for i in range(len(auxlist)):
        if i == 0:
            daycases.append(auxlist[i])
        else:
            daycases.append(auxlist[i] - auxlist[i-1])
    df['daycases'] = daycases
    return df

def showtable():
    df = casesperday()
    df_res = df[['date', 'daycases']].copy()
    print(df_res.to_string(index=False))

def displaychart(show):
    df = casesperday()
    df_aux = df.sort_values('daycases', ascending=False)
    datelist = df_aux.head(10)['date'].tolist()
    caseslist = df_aux.head(10)['daycases'].tolist()
    datelist.reverse()
    caseslist.reverse()
    x = np.array(datelist)
    y = np.array(caseslist)
    plt.barh(x, y, height = 0.5, color = "magenta")
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5, axis = 'x')
    plt.title("Top ten of days with the most COVID-19 cases in USA", loc = 'right')
    if show:
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
        plt.show()
    else:
        fig = plt.gcf()
        fig.savefig("top10.png")


showtable()
displaychart(True)
displaychart(False)