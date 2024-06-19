{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "db7d82b0-d9d9-449c-9072-c0eab8f7323b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting reportlab\n",
      "  Downloading reportlab-4.2.0-py3-none-any.whl (1.9 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.9/1.9 MB\u001b[0m \u001b[31m2.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m[36m0:00:01\u001b[0mm eta \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: chardet in /Users/dalilamachado/anaconda3/lib/python3.10/site-packages (from reportlab) (5.2.0)\n",
      "Requirement already satisfied: pillow>=9.0.0 in /Users/dalilamachado/anaconda3/lib/python3.10/site-packages (from reportlab) (10.1.0)\n",
      "Installing collected packages: reportlab\n",
      "Successfully installed reportlab-4.2.0\n"
     ]
    }
   ],
   "source": [
    "!pip install reportlab"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "94db5d29-7499-45a6-90f7-fcd46e72b0bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import os\n",
    "from reportlab.lib.pagesizes import letter\n",
    "from reportlab.pdfgen import canvas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c68068ca-a901-4b0d-b2df-6233c3f6e406",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Nome do arquivo CSV para armazenar os dados\n",
    "CSV_FILE = 'matriz_swot.csv'\n",
    "\n",
    "# Função para carregar a matriz SWOT do arquivo CSV\n",
    "def load_swot():\n",
    "    if os.path.exists(CSV_FILE):\n",
    "        return pd.read_csv(CSV_FILE).to_dict(orient='list')\n",
    "    else:\n",
    "        return create_swot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c0f27206-beb6-4222-8378-bac864f466e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Função para criar a estrutura inicial da matriz SWOT\n",
    "def create_swot():\n",
    "    return {\n",
    "        'Forças': [],\n",
    "        'Fraquezas': [],\n",
    "        'Oportunidades': [],\n",
    "        'Ameaças': []\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f7746e97-0616-4d98-bf28-caddf0204d44",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Função para adicionar um item na matriz SWOT\n",
    "def add_item(swot, category, item):\n",
    "    if category in swot:\n",
    "        swot[category].append(item)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c9cac78c-83e2-414b-b9d1-f4c3d3501445",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Função para converter a matriz SWOT em um DataFrame\n",
    "def swot_to_df(swot):\n",
    "    data = []\n",
    "    for category, items in swot.items():\n",
    "        for item in items:\n",
    "            data.append([category, item])\n",
    "    return pd.DataFrame(data, columns=['Categoria', 'Item'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fada98b4-4c93-4f5d-b7b8-3dae360bf5ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Função para salvar a matriz SWOT no arquivo CSV\n",
    "def save_swot(swot):\n",
    "    df = swot_to_df(swot)\n",
    "    df.to_csv(CSV_FILE, index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ba3f89c2-bb0b-4ba4-9d0e-10075ea63cd1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Função para gerar o PDF da matriz SWOT\n",
    "def generate_pdf(swot):\n",
    "    pdf_file = 'matriz_swot.pdf'\n",
    "    c = canvas.Canvas(pdf_file, pagesize=letter)\n",
    "    width, height = letter\n",
    "    c.drawString(100, height - 40, \"Matriz SWOT\")\n",
    "    \n",
    "    y = height - 60\n",
    "    for category, items in swot.items():\n",
    "        c.drawString(50, y, category + \":\")\n",
    "        y -= 20\n",
    "        for item in items:\n",
    "            c.drawString(70, y, \"- \" + item)\n",
    "            y -= 20\n",
    "        y -= 10\n",
    "    \n",
    "    c.save()\n",
    "    return pdf_file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "61437cbc-2364-4c00-8ac8-fa5260171458",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Carregar ou inicializar a matriz SWOT\n",
    "swot = load_swot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "778c087e-9da8-485a-acc5-b5624ccff802",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Título da aplicação\n",
    "st.title('Matriz SWOT Online')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f0fbcde9-6e8f-4c8f-8c70-6893c7026795",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Entrada de dados\n",
    "st.header('Adicionar Item na Matriz SWOT')\n",
    "category = st.selectbox('Categoria', ['Forças', 'Fraquezas', 'Oportunidades', 'Ameaças'])\n",
    "item = st.text_input('Descrição do Item')\n",
    "\n",
    "if st.button('Adicionar'):\n",
    "    if item:\n",
    "        add_item(swot, category, item)\n",
    "        save_swot(swot)\n",
    "        st.success(f'Item adicionado à categoria {category}.')\n",
    "    else:\n",
    "        st.error('Por favor, insira uma descrição para o item.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "961152a2-20ff-4685-934d-2cb2205fdcd9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Mostrar a matriz SWOT\n",
    "st.header('Matriz SWOT Atual')\n",
    "df = swot_to_df(swot)\n",
    "st.dataframe(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "249288fd-9493-4b20-aa7a-243e37641871",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exportar a matriz SWOT como PDF\n",
    "st.header('Exportar Matriz SWOT')\n",
    "if st.button('Exportar como PDF'):\n",
    "    pdf_file = generate_pdf(swot)\n",
    "    with open(pdf_file, 'rb') as f:\n",
    "        st.download_button('Baixar PDF', f, file_name=pdf_file)\n",
    "        st.success('Matriz SWOT exportada como PDF.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "34e9be40-b1bf-41fd-821d-836e1f5ea4d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Instruções para rodar a aplicação\n",
    "st.write('Para rodar esta aplicação, salve este código em um arquivo Python (por exemplo, `app.py`) e execute o comando:')\n",
    "st.code('streamlit run app.py')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
