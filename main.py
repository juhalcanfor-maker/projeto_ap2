import streamlit as st
st.text("meu primeiro programa")













import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
df.columns 
# título do dashboard
st.header("Meu Dashboard 2.0")
menu = st.tabs(["Tabela", "Barra", "vertical"])
with menu[0]:
# Expondo o df no dashboard
       st.dataframe(df)
with menu[1]:
# Grafico de barras vertical
       fig = plt.figure(figsize=(10,6)) #tamanho do grafico
       sn.countplot(data=df, x="setor", order=df['setor'].value_counts().index)
       plt.title("Grafico de Barras por setor")
       plt.xlabel("Numero de empresas")
       plt.ylabel("Setor")
       plt.xticks(rotation=45)
       plt.show()
       st.pyplot(fig)
with menu[2]:
# # Grafico de barras horizontal
       fig = plt.figure(figsize=(10,6)) #tamanho do grafico
       sn.countplot(data=df, y="setor", order=df['setor'].value_counts().index)
       plt.title("Grafico de Barras por setor")
       plt.xlabel("Numero de empresas")
       plt.ylabel("Setor")
       plt.xticks(rotation=45)
       plt.show()
       st.pyplot(fig)

# # Grafico de pizza
# setor = df["setor"].value_counts()
# plt.figure(figsize=(10,6)) #tamanho do grafico
# plt.pie(setor, labels=setor.index
#  autopct= '%1.1f%%')


# # Histograma
# filtro = df["setor"]== 'agrícola'
# df_setor = df[filtro]
# sn.histplot(df["roe"], bins=20, kde=True, color='blue')



# import pandas as pd
# df = pd.read_excel("planilhao.xlsx", sheet_name="soja3")
# # Selecioando as colunas que tenha valor "EBIT"
# filtro = df["Conta"]=="EBIT"
# df.columns
# colunas = ['20254T', '20252T',
#        '20251T', '20244T', '20243T', '20242T', '20241T', '20234T', '20233T',
#        '20232T', '20231T', '20224T', '20223T', '20222T', '20221T', '20214T',
#        '20213T', '20212T', '20211T', '20204T', '20203T']
# colunas = sorted(colunas)
# # instalar a biblioteca matplotlib (uv add matplotlib)
# ebit = df[filtro][colunas].iloc[0]
# sn.lineplot(x=colunas, y=ebit.values)

# import seaborn as sn 
# sn.lineplot(ebit)
# sn.histplot(ebit)
# sn.boxplot(ebit)
# import matplotlib.pyplot as plt

# # Grafico do lucro liquido

# df = pd.read_excel("planilhao.xlsx", sheet_name="soja3")
# filtro_lucro_liquido = df["Conta"]=="Lucro Líquido"
# df.columns
# colunas = ['20254T', '20252T',
#        '20251T', '20244T', '20243T', '20242T', '20241T', '20234T', '20233T',
#        '20232T', '20231T', '20224T', '20223T', '20222T', '20221T', '20214T',
#        '20213T', '20212T', '20211T', '20204T', '20203T']
# colunas = sorted(colunas)
# lucro_liquido = df[filtro_lucro_liquido][colunas].iloc[0]
# sn.lineplot(x=colunas, y=lucro_liquido.values)

# sn.lineplot(lucro_liquido)
# sn.histplot(lucro_liquido)
# sn.boxplot(lucro_liquido)










import pandas as pd
df = pd.read_csv("study_performance.csv")
colunas = ["math_score","reading_score","writing_score"]
df



