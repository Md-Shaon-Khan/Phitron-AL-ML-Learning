# import streamlit as st 

# st.image("F:\Jupyter_Projects\Phitron AL ML\Main Courses\Week - 02\Module - 06 Streamlit\Practice\Files\pexels-nietjuhart-776636.jpg")

# st.image(["F:\Jupyter_Projects\Phitron AL ML\Main Courses\Week - 02\Module - 06 Streamlit\Practice\Files\pexels-nietjuhart-776636.jpg","F:\Jupyter_Projects\Phitron AL ML\Main Courses\Week - 02\Module - 06 Streamlit\Practice\Files\pexels-gustavo-fring-6870412.jpg"])


# st.audio("F:/Jupyter_Projects/Phitron AL ML/Main Courses/Week - 02/Module - 06 Streamlit/Practice/Files/3946077-uhd_4096_2160_25fps.mp4")

# file = st.file_uploader("Upload Image")

# if file:
#   st.image(file)

import streamlit as st 
from PIL import Image

img = Image.open("F:/Jupyter_Projects/Phitron AL ML/Main Courses/Week - 02/Module - 06 Streamlit/Practice/Files/pexels-nietjuhart-776636.jpg")

st.image(img, caption="Loving Person",use_column_width=True)

uploaded = st.file_uploader(
  "Upload the ecg file",
  type=["csv","png"]
)

if uploaded:
  st.write("File is founded.",uploaded.name)