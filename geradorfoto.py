import streamlit as st
from funcoes_img import gerar_foto

h1, h2 = st.columns(2)
h1.image('img/logoevvia.jpeg')
h2.title('Fotos Evvia')

if 'existe' not in st.session_state:
    st.session_state['existe'] = False

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
    gerar_foto(foto, overlays_list[overlay])

st.divider()
#baixa a foto
if st.session_state['existe']:
    st.image('pronta.png')
    with open('pronta.png', 'rb') as f:
        st.download_button('Baixar foto', f, 'FotoEvvia.png')