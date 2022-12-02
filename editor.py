import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.set_page_config(page_title = 'Image Editor', 
                   page_icon='✏️',
                   layout='wide')

st.markdown('<h1 style ="text-align:center;">Image Editor</h1>',unsafe_allow_html=True)
st.markdown('---')
image = st.file_uploader('Upload your Image',type=['jpg','png','jpeg'])
info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()
if image:
    opn_img = Image.open(image)
    info.markdown('<h2 style ="text-align:center;">Image Details</h2>',unsafe_allow_html=True)
    size.markdown(f'<h6>Size : {opn_img.size}</h6>',unsafe_allow_html=True)
    mode.markdown(f'<h6>Mode : {opn_img.mode}</h6>',unsafe_allow_html=True)
    format_.markdown(f'<h6>Format : {opn_img.format}</h6>',unsafe_allow_html=True)

    st.markdown('<h2 style ="text-align:center;">Resize Image</h2>',unsafe_allow_html=True)
    width = st.number_input('Width',value=opn_img.width)
    height = st.number_input('Height',value=opn_img.height)

    st.markdown('<h2 style ="text-align:center;">Rotate Image</h2>',unsafe_allow_html=True)
    degree = st.number_input('Degree')
    
    st.markdown('<h2 style ="text-align:center;">Filter Image</h2>',unsafe_allow_html=True)
    filter = st.selectbox('Filters',options=('None','Sharp','Smooth','Blur','Detail','Emboss'))

    s_btn = st.button('Submit Changes')

    if s_btn:
        edited = opn_img.resize((width,height)).rotate(degree)
        filtered = edited
        
        if filter != 'None':
            if filter == 'Sharp':
                filtered = edited.filter(SHARPEN)
            elif filter == 'Smooth':
                filtered = edited.filter(SMOOTH)
            elif filter == 'Blur':
                filtered = edited.filter(BLUR)
            elif filter == 'Detail':
                filtered = edited.filter(DETAIL)
            elif filter == 'Emboss':
                filtered = edited.filter(EMBOSS)
        
        col1, col2 = st.columns(2)
        col1.image(opn_img)
        col2.image(filtered)
        
