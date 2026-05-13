import streamlit as st 
st.title("Input your files", anchor=False)
st.divider()

images = st.file_uploader("Enter image",
                 type=['jpg','jpeg','png'],
                 accept_multiple_files=True)


if images:
   col = st.columns(3)
   
   for i, image in enumerate(images):
     with col[i % 3]:
       st.image(image)
       
st.divider()

st.image("G:/Picture/Camera Roll/WIN_20241103_14_26_01_Pro.jpg")

st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6")