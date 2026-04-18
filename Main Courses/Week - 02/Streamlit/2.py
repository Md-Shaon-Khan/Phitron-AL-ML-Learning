import streamlit as st 

if st.button("Click me"):
  st.write("Button Clicked!")
  
choise = st.radio("Choose an option:",["Option 1","Option 2","Option 3"])
st.write("You selected: ",choise)

agree = st.checkbox("I agree")
if agree:
  st.write("Thanks for agreeing")

fruit = st.selectbox("Pick a fruit: ",["Apple","Banana","Orange"])
st.write("Your favourite fruit is: ",fruit)

colors = st.multiselect("Select your favourite color: ",['Red','Green','Blue','Yellow'])
st.write("You Choose",colors)

age = st.slider("Select your age: ",0,100,22)
st.write("Age: ",age)

number = st.number_input("Enter a number: ",min_value=0,max_value=100,value=10)
st.write("Number: ",number)

name = st.text_input("Enter your name: ")
st.write("Hello, ",name)

bio = st.text_area("Enter your short bio: ")
st.write("Your bio: ",bio)

date = st.date_input("Pick a time")
st.write("Selected time: ",date)

uploaded_file = st.file_uploader("Upload a text file: ", type=["txt"])

if uploaded_file is not None:
  content = uploaded_file.read().decode("utf-8")
  st.text_area("File content",content,height=300)
  
  