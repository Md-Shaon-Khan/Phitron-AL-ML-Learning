from google import genai
import os
from dotenv import load_dotenv
import streamlit as st 
load_dotenv()

api_key = os.environ.get("Gemini_key_api")

client = genai.Client(api_key=api_key)

msg = st.text_input("Enter the sentence you want to modify", placeholder="Your message...")

if msg:
  with st.spinner("Shaon is writing..."):
    try:
        prompt = f"Improve this sentence professionally:\n{msg}"

      
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        st.markdown(response.text)

    except Exception as e:
        st.error(e)