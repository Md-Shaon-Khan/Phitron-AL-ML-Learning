import streamlit as st 
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image


st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes.")

st.divider()

with st.sidebar:
  st.header("Controls")
  images = st.file_uploader(
    "Uploaded the photos of your note",
    type=['jpg','jpeg','png'],
    accept_multiple_files=True
  )
  # images
  
  pil_images = []
  
  for img in images:
    pil_img = Image.open(img)
    pil_images.append(pil_img)
    
  if images:
    if len(images) > 3:
      st.error("Uploaded at max 3 images")
    else:
      st.subheader("Uploaded images successful.")
      col = st.columns(len(images))
      
      for i,img in enumerate(images):
        with col[i]:
          st.image(img)
  
  #difficulty
  
  selected_option = st.selectbox(
    "Enter the difficulty of your quiz",
    ("Easy","Medium","Hard"),
    index=None
  )
  
  # if selected_option:
  #   st.markdown(f"You selected option **{selected_option}**")
  # else:
  #   st.error("You must select a difficulty")
    
  # button
  

  pressed = st.button("Submit",type="primary")
  
if pressed:
  if not images:
    st.error("You have to upload at least 1 image")
  
  if not selected_option:
    st.error("You have to select difficulty.")
    
  if images and selected_option:
    
    # note
    with st.container(border=True):
      st.subheader("Your note")
      
      
      #This portion will be replaced by API Call
      with st.spinner("Shaon is writing notes for you"):
        generate_notes = note_generator(pil_images)
        st.markdown(generate_notes)
      
    
    #Audio transcript
    
    with st.container(border=True):
      st.subheader("Audio Transcription")
      
      
      
      #This portion will be replaced by API Call
      with st.spinner("Shaon is creating a audio notes for you"):
        generate_notes = generate_notes.replace("#","")
        generate_notes = generate_notes.replace("*","")
        generate_notes = generate_notes.replace("-","")
        generate_notes = generate_notes.replace("`","")
        generate_notes = generate_notes.replace("!","")
        generate_notes = generate_notes.replace("$","")
        
        
        audio_transcrip = audio_transcription(generate_notes)
      st.audio(audio_transcrip)
    
    
    #Quiz
    
    with st.container(border=True):
      st.subheader(f"Quiz {selected_option} difficulty")
      
      with st.spinner("Shaon is creating a quizs notes for you"):
        
        quizzes = quiz_generator(pil_images,selected_option)
      st.markdown(quizzes)