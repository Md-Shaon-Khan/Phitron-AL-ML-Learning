from gtts import gTTS
import streamlit as st 
import io

text = "হ্যালো, এই কোর্সে আপনাকে স্বাগতম"

speech = gTTS(text=text, lang='bn', slow=False)

# speech.save("Welcome.mp3")

audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)
st.audio(audio_buffer)
