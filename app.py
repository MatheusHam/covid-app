import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = pd.read_csv('covid.csv')
    page = st.sidebar.selectbox("Choose a page", ['Homepage'])
    filter = (df['Country/Region'] == 'Brazil') & (df['Confirmed'] > 4000)
    dfbrasil = df[filter].copy()

    fig, ax = plt.subplots()
    day = dfbrasil['Date']
    confirmed = dfbrasil['Confirmed']
    ax.plot(day, confirmed)
    ax.set(xlabel='Dias Corridos', ylabel='Casos Confirmados', title='Casos de Corona Virús no Brasil')
    ax.grid()
    fig.savefig('coronavairusbrasil.png')
    st.pyplot()

    if page == 'Homepage':
        st.title('Curva de Corona Virus Brasil')
        st.text('Implementing...')
        #st.dataframe(df)


if __name__ == '__main__':
    main()
