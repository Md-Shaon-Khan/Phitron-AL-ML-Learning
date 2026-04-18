from groq import Groq
import os 
from dotenv import load_dotenv
import streamlit as st 
load_dotenv()

api_key_groq = os.environ.get("GROQ_API")

# client = Groq.Client(api_key = api_key_genai)

# st.title("Situation Handler")
# st.divider()

# with st.container(): 
#    prompt = st.text_input("Ask any question arise your mind",placeholder="Your question...")
   
   
# response = client.models.generate_content(
#   model="gemini-3-flash-preview",
#   contents=prompt
# )

# st.markdown(response.text)

client = Groq(api_key=api_key_groq)


st.title("Situation Handler")
st.divider()

with st.container(): 
  prompt = st.text_input("Ask any question arise your mind",placeholder="Your question...")
  
completion = client.chat.completions.create(
  model="openai/gpt-oss-120b",
  messages=[{"role": "user", "content": prompt}]
)

with st.container():
  st.markdown(completion.choices[0].message.content)