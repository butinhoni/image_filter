import streamlit as st
from funcoes_img import gerar_foto
import uuid
from pathlib import Path

h1, h2 = st.columns(2)
h1.image('img/logoevvia.png')
h2.title('Faça sua foto')
h2.header('Agosto Lilás')

if 'existe' not in st.session_state:
    st.session_state['existe'] = False

if 'num' not in st.session_state:
    st.session_state['num'] = str(uuid.uuid1())

filepath = f'prontas/{st.session_state["num"]}.png'

#upa foto
foto = st.file_uploader('Selecione sua foto', type=['png','jpg','jpeg'])

overlays_list = {
    'Evvia': 'img/evvia.png',
    'Engevvia-MT':'img/MT lilas.png',
    'Engevvia-163':'img/img_rosa.png',
    'Engevvia-GO': 'img/img_go.png',
    'Gestão PI': 'img/img_pi.png'
}

overlay = st.selectbox('Selecione o Consórcio', overlays_list.keys())

#gera o bagulho
gerar = st.button('Gerar Foto')
if gerar:
    st.session_state['existe'] = True
    gerar_foto(foto, overlays_list[overlay], filepath)

st.divider()
#baixa a foto
if st.session_state['existe']:
    st.image(filepath)
    with open(filepath, 'rb') as f:
        st.download_button('Baixar foto', f, 'FotoEvvia.png')