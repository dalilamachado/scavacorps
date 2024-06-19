import streamlit as st
import pandas as pd
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Nome do arquivo CSV para armazenar os dados
CSV_FILE = 'matriz_swot.csv'

# Função para carregar a matriz SWOT do arquivo CSV
def load_swot():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE).to_dict(orient='list')
    else:
        return create_swot()

# Função para criar a estrutura inicial da matriz SWOT
def create_swot():
    return {
        'Forças': [],
        'Fraquezas': [],
        'Oportunidades': [],
        'Ameaças': []
    }

# Função para adicionar um item na matriz SWOT
def add_item(swot, category, item):
    if category in swot:
        swot[category].append(item)

# Função para converter a matriz SWOT em um DataFrame
def swot_to_df(swot):
    data = []
    for category, items in swot.items():
        for item in items:
            data.append([category, item])
    return pd.DataFrame(data, columns=['Categoria', 'Item'])

# Função para salvar a matriz SWOT no arquivo CSV
def save_swot(swot):
    df = swot_to_df(swot)
    df.to_csv(CSV_FILE, index=False)

# Função para gerar o PDF da matriz SWOT
def generate_pdf(swot):
    pdf_file = 'matriz_swot.pdf'
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 40, "Matriz SWOT")
    
    y = height - 60
    for category, items in swot.items():
        c.drawString(50, y, category + ":")
        y -= 20
        for item in items:
            c.drawString(70, y, "- " + item)
            y -= 20
        y -= 10
    
    c.save()
    return pdf_file

# Carregar ou inicializar a matriz SWOT
swot = load_swot()

# Título da aplicação
st.title('Matriz SWOT Online')

# Layout para entrada de dados
st.header('Adicionar Item na Matriz SWOT')
col1, col2 = st.columns(2)

with col1:
    with st.form(key='swot_form'):
        category = st.selectbox('Categoria', ['Forças', 'Fraquezas', 'Oportunidades', 'Ameaças'])
        item = st.text_area('Descrição do Item')
        submit_button = st.form_submit_button(label='Adicionar')

if submit_button:
    if item:
        add_item(swot, category, item)
        save_swot(swot)
        st.success(f'Item adicionado à categoria {category}.')
    else:
        st.error('Por favor, insira uma descrição para o item.')

# Mostrar a matriz SWOT
st.header('Matriz SWOT Atual')
df = swot_to_df(swot)
st.dataframe(df)

# Exportar a matriz SWOT como PDF
st.header('Exportar Matriz SWOT')
if st.button('Exportar como PDF'):
    pdf_file = generate_pdf(swot)
    with open(pdf_file, 'rb') as f:
        st.download_button('Baixar PDF', f, file_name=pdf_file)
        st.success('Matriz SWOT exportada como PDF.')

# Instruções para rodar a aplicação
st.write('Para rodar esta aplicação, salve este código em um arquivo Python (por exemplo, `app.py`) e execute o comando:')
st.code('streamlit run app.py')
