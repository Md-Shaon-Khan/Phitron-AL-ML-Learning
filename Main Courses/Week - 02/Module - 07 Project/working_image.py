import streamlit as st 
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


images = st.file_uploader(
    "Uploaded the photos of your note",
    type=['jpg','jpeg','png'],
    accept_multiple_files=True
)


print(type(images))



if images:
  
  pil_images = []
  for img in images:
    pil_img = Image.open(img)
    pil_images.append(pil_img)
  prompt = """
  Describe the pictures in note without emoji's structured formally and professional easy to read and remember with point, definition and example
  """
  
  response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents=[pil_images,prompt]
  )
  
  st.markdown(response.text)