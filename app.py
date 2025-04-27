import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
data = df = pd.read_csv('health_data.csv')

# Título e descrição
st.title('Análise de Dados de Saúde')
st.write('Este aplicativo analisa dados de saúde para fornecer insights sobre várias condições médicas.')

# Barra lateral para entrada do usuário
st.sidebar.header('Seleção de Características')
diagnostico_selecionado = st.sidebar.selectbox('Diagnóstico', data['Diagnosis'].unique())

# Filtrar dados com base na entrada do usuário
dados_filtrados = data[data['Diagnosis'] == diagnostico_selecionado]

# Exibir dados filtrados
st.subheader('Dados Filtrados')
st.write(dados_filtrados)

# Visualizações
st.subheader('Distribuição de Idade')
fig, ax = plt.subplots()
sns.histplot(dados_filtrados['Age'], kde=True, ax=ax)
st.pyplot(fig)

st.subheader('Pressão Sanguínea vs Nível de Colesterol')
fig, ax = plt.subplots()
sns.scatterplot(data=dados_filtrados, x='Blood_Pressure', y='Cholesterol_Level', hue='Gender', ax=ax)
st.pyplot(fig)

# Insights e conclusões
st.subheader('Insights e Conclusões')
st.write('Com base na análise, podemos observar os seguintes insights:')
st.write('- Insight 1')
st.write('- Insight 2')
st.write('- Insight 3')

# Possíveis soluções
st.subheader('Possíveis Soluções')
st.write('Com base nos insights, aqui estão algumas possíveis soluções:')
st.write('- Solução 1')
st.write('- Solução 2')
st.write('- Solução 3')

# Salvar este script como app.py e executar usando o comando: streamlit run app.py
