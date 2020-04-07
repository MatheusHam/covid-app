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
    st.title(f'País de comparação: {country}')
    st.text('Compare o aumento de casos no Brasil em relação a outros paises a partir\n do primeiro caso confirmado.')
    st.text('Fonte: https://www.kaggle.com/imdevskp/corona-virus-report/data#')
    st.text('Dados atualizados em 07/04/2020')

    filter = (df['Country/Region'] == country) & (df['Confirmed'] > 0)
    filter2 = (df['Country/Region'] == 'Brazil') & (df['Confirmed'] > 0)
    dfcountry = df[filter].copy()
    dfbrazil = df[filter2].copy()

    qtd_dias_country = []
    qtd_dias_brazil = []
    for x in range(len(dfbrazil['Date'])):
        qtd_dias_brazil.append(x)
    for x in range(len(dfcountry['Date'])):
        qtd_dias_country.append(x)

    dfcountry.insert(0, "Dias", qtd_dias_country, True)
    dfbrazil.insert(0, "Dias", qtd_dias_brazil, True)

    fig, ax = plt.subplots()

    day_c = dfcountry['Dias']
    day_bra = dfbrazil['Dias']
    confirmed_br = dfbrazil['Confirmed']
    confirmed_c = dfcountry['Confirmed']

    ax.plot(day_bra, confirmed_br, color="C0", label='Brasil')
    ax.plot(day_c, confirmed_c, color="C1", label=f'{country}')

    ax.legend()
    ax.set(xlabel='Dias Corridos', ylabel='Casos Confirmados', title='Evolução de casos')
    ax.grid()
    ax.set_yscale('log')

    fig.savefig('graph')

    st.pyplot()


if __name__ == '__main__':
    main()
