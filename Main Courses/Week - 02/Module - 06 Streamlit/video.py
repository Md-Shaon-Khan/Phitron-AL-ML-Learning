import streamlit as st 

st.title("Input your files...",anchor=False)
st.divider()

video_file = st.file_uploader("Enter your video...",type=['mp4','mkv'],)

button = st.button("Click to upload")

if button:
  if video_file:
    st.video(video_file)
    st.success("Your file is uploaded.")
  else:
    st.error("You must upload a file.")