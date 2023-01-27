"""A intenção do código é criar um aplicativo simples onde o usuário
selecione uma opção para o x, outra para o y e o gráfico seja montado.
A biblioteca streamlit é para montar a página, plotly para o gráfico e
pandas para ler o csv"""

import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
option_x = st.selectbox("Select the data for the X-axis",
                      ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select the data for the Y-axis",
                      ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")

x_array = None
match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

y_array = None
match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

st.subheader(f"{option_x} and {option_y}")

figure1 = px.scatter(x=x_array, y=y_array, labels={"x": option_x, "y": option_y})
st.plotly_chart(figure1)
