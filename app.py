import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = load_data()
    page = st.sidebar.selectbox("Work In Progress", ['Homepage'])

    if page == 'Homepage':
        country = st.selectbox("Choose a Country", df['Country/Region'].unique(), index=1)
        create_graph(df, country)

@st.cache
def load_data():
    df = pd.read_csv('covid.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df


def create_graph(df, country):
    st.title(f'Casos Confirmados no país: {country}')
    st.text('Aumento do número de casos confirmados por dia')
    st.text('Fonte: https://www.kaggle.com/imdevskp/corona-virus-report/data#')
    filter = (df['Country/Region'] == country) & (df['Date'] > '03/30/2020')
    dfcountry = df[filter].copy()
    fig, ax = plt.subplots()
    day = dfcountry['Date']
    confirmed = dfcountry['Confirmed']
    ax.plot(day, confirmed)
    ax.set(xlabel='Dias Corridos', ylabel='Casos Confirmados')
    ax.grid()
    st.pyplot()


if __name__ == '__main__':
    main()
