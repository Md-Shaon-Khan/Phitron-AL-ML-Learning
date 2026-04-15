import streamlit as st 
name = st.text_input("Enter your name...")
st.write("Hello", name)

if st.button("Click Me"):
  st.write("Button Pressed")
  
age = st.slider("Select your age",0,100)
st.write("Your age is", age)

option = st.selectbox("Choose one", ['A','B','C'])

st.write("You selected",option)

if st.checkbox("Show data"):
  st.write("Data is visible")
  
  
st.divider()


st.title("User Info App")
name = st.text_input("Name")
age = st.slider("Age",0,100)
option = st.selectbox("Gender",["Male","Female"])

if st.button("Submit"):
  st.write("Name",name)
  st.write("Age: ",age)
  st.write("Gender: ",option)
  