import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a Country", ['Brazil', 'Italy'])
    print(page)

    if page == 'Brazil':
        st.title('Casos Confirmados no Brasil')
        st.text('Implementing...')
        create_graph(df, 'Brazil')

    elif page == 'Italy':
        st.title('Casos confirmados na Itália')
        st.text('Implementing...')
        create_graph(df, 'Italy')


@st.cache
def load_data():
    df = pd.read_csv('covid.csv')
    return df


def create_graph(df, country):
    filter = (df['Country/Region'] == country) & (df['Confirmed'] > 4000)
    dfbrasil = df[filter].copy()
    fig, ax = plt.subplots()
    day = dfbrasil['Date']
    confirmed = dfbrasil['Confirmed']
    ax.plot(day, confirmed)
    ax.set(xlabel='Dias Corridos', ylabel='Casos Confirmados', title=f'Casos de Corona Virús no {country}')
    ax.grid()
    st.pyplot()


if __name__ == '__main__':
    main()
