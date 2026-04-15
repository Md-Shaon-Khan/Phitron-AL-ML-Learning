import streamlit as st 

st.title("Input your files...",anchor=False)
st.divider()


# st.audio("E:\Down\kakaist-heartbeat-sfx-320981.mp3",loop=True)

audios = st.file_uploader("Enter audio",
                          type=['mp3','ogg','flac'],)


if audios:
  st.audio(audios)