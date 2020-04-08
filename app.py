import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = load_data()
    page = st.sidebar.selectbox("Visualizações", ['Evolução dos casos'])

    if page == 'Evolução dos casos':
        st.title('')
        st.text('Compare o aumento de casos em relação a outros paises a partir\n do primeiro caso confirmado.')
        st.text('Fonte: https://www.kaggle.com/imdevskp/corona-virus-report/data#')
        st.text('Dados atualizados em 08/04/2020')
        countries = [st.selectbox("Country - 1", df['Country/Region'].unique(), index=21),
                     st.selectbox("Country - 2", df['Country/Region'].unique(), index=138),
                     st.selectbox("Country - 3", df['Country/Region'].unique(), index=156)]
        create_graph(df, countries)


@st.cache
def load_data():
    df = pd.read_csv('covid.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df


def create_graph(df, countries):
    fig, ax = plt.subplots()
    color = 0
    for country in countries:
        filter = (df['Country/Region'] == country) & (df['Confirmed'] > 0)
        dfcountry = df[filter].copy()
        qtd_dias_country = []
        for x in range(len(dfcountry['Date'])):
            qtd_dias_country.append(x)
        dfcountry.insert(0, "Dias", qtd_dias_country, True)
        day_c = dfcountry['Dias']
        confirmed_c = dfcountry['Confirmed']
        color += 1
        color_text = 'C'+str(color)
        ax.plot(day_c, confirmed_c, color=color_text, label=f'{country}')

    ax.legend()
    ax.set(xlabel='Dias Corridos', ylabel='Casos Confirmados', title='Evolução de casos')
    ax.grid()
    ax.set_yscale('log')

    st.pyplot()


if __name__ == '__main__':
    main()
