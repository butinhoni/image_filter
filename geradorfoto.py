import streamlit as st
from funcoes_img import gerar_foto

st.title('Fotos Evvia')

if 'existe' not in st.session_state:
    st.session_state['existe'] = False

#upa foto
foto = st.file_uploader('Selecione sua foto', type=['png','jpg','jpeg'])

#gera o bagulho
gerar = st.button('Gerar Foto')
if gerar:
    st.session_state['existe'] = True
    gerar_foto(foto, 'img/img_rosa.png')

st.divider()
#baixa a foto
if st.session_state['existe']:
    st.image('pronta.png')
    with open('pronta.png', 'rb') as f:
        st.download_button('Baixar foto', f, 'FotoEvvia.png')